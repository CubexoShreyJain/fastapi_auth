import requests
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.responses import RedirectResponse
import jwt
from jwt import PyJWKClient
import json

server = FastAPI()

AUTH0_DOMAIN = "dev-fsozahwfyqtys1qr.us.auth0.com"
CLIENT_ID = "liNRlvgwS575bxdzidaUYHrAWIuUvjyB"
CLIENT_SECRET = "UR0eqG1BqcvSTAW8XUDZeHoY5oCSEXfJCRdzUG4p3QJhA9FErAgIGgagBiirwkOf"
REDIRECT_URI = "http://localhost:8000/docs"
AUDIENCE = "https://microapi.io/api/orders"
DEFAULT_ROLE_ID = "rol_BCX1ZXvLT75tJ6um"  
EXTENSION_URL = "https://dev-fsozahwfyqtys1qr.us.webtask.run/adf6e2f2b84784b57522e3b19dfc9201/api"

security = HTTPBearer()

# Redirects user to the Auth0 login page
@server.get("/")
def register():
    auth0_url = (
        f"https://{AUTH0_DOMAIN}/authorize?response_type=code&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}&scope=openid profile email&prompt=login&audience={AUDIENCE}"
    )
    return RedirectResponse(url=auth0_url)

# Redirects to the Auth0 login page for getting an authorization code
@server.get("/login")
def login():
    auth_url = (
        f"https://{AUTH0_DOMAIN}/authorize?response_type=code&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}&scope=offline_access openid profile email&audience={AUDIENCE}"
    )
    return RedirectResponse(auth_url)

# Endpoint to exchange the authorization code for an access token
@server.get("/token")
def get_access_token(code: str):
    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }

    headers = {"content-type": "application/x-www-form-urlencoded"}

    response = requests.post(
        f"https://{AUTH0_DOMAIN}/oauth/token", data=payload, headers=headers
    )
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    result = response.json()
    decoded_token = jwt.decode(result["access_token"], options={"verify_signature": False})
    print(result["access_token"])

    user_id = decoded_token.get("sub")
    token=get_authorization_token()
    group_id_data=fetch_groups(token)
    # print(group_id_data)
    group_id = next((group['_id'] for group in group_id_data['groups'] if group['name'] == 'Employee'), None)
    print(user_id) 
    print(group_id) 
    print(token) 
    if user_id:
        assign_role_to_user(user_id, DEFAULT_ROLE_ID)
        assign_user_to_group(user_id,group_id,token)
    return {"access_token": result["access_token"], "decoded_token": decoded_token}

def get_authorization_token():
    url = f"https://{AUTH0_DOMAIN}/oauth/token"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "client_id": "K30Ilu8F1lOQ1mGeBHtIybfQwhpHTJe0",
        "client_secret": "bkGuyeNP2ym-RYjAZueehRpPBVxXypOkO58tU-HIrwfFDsf7HpTe0z7_ZYc0mCpl",
        "audience": "urn:auth0-authz-api",
        "grant_type": "client_credentials"
    } 
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        token_info = response.json()
        return token_info.get("access_token")
    else:
        print(f" Failed to fetch token. Status code: {response.status_code}")
        print("Response:", response.text)

# Endpoint to create a new role in Auth0
@server.post("/role")
def create_role(name: str, description: str, token: str):
    url = f"https://{AUTH0_DOMAIN}/api/v2/roles"

    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {token}",
        "cache-control": "no-cache"
    }
    data = {"name": name, "description": description}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return response.json()

# Endpoint to assign a role to a user
@server.post("/assign-role")
def assign_role(user_id: str, role_id: str):
    assign_role_to_user(user_id, role_id)
    return {"message": "Role assigned successfully"}

# Helper function to assign role to a user
def assign_role_to_user(user_id: str, role_id: str):
    management_token = get_management_api_token()
    url = f"https://{AUTH0_DOMAIN}/api/v2/users/{user_id}/roles"

    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {management_token}",
    }
    data = {"roles": [role_id]}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 204:
        raise HTTPException(status_code=response.status_code, detail=response.text)

# Protected route that requires a valid JWT token to access
@server.get("/protected")
def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    jwks_url = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
    jwks_client = PyJWKClient(jwks_url)
    signing_key = jwks_client.get_signing_key_from_jwt(token).key

    try:
        payload = jwt.decode(
            token,
            signing_key,
            algorithms=["RS256"],
            audience=AUDIENCE,
            issuer=f"https://{AUTH0_DOMAIN}/"
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")

    return {"message": "Access granted", "user": payload}

# Middleware to enforce permissions for accessing protected routes
@server.middleware("http")
async def enforce_permissions(request, call_next):
    if request.url.path.startswith("/protected"):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            raise HTTPException(status_code=401, detail="Authorization header missing")

        token = auth_header.split()[1]
        jwks_url = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
        jwks_client = PyJWKClient(jwks_url)
        signing_key = jwks_client.get_signing_key_from_jwt(token).key

        try:
            payload = jwt.decode(
                token,
                signing_key,
                algorithms=["RS256"],
                audience=AUDIENCE,
                issuer=f"https://{AUTH0_DOMAIN}/"
            )
            if "permissions" not in payload or "read:data" not in payload["permissions"]:
                raise HTTPException(status_code=403, detail="Permission denied")
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired")
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")

    response = await call_next(request)
    return response

# Function to get the management API token for making Auth0 API requests
def get_management_api_token():
    url = f"https://{AUTH0_DOMAIN}/oauth/token"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "audience": f"https://{AUTH0_DOMAIN}/api/v2/",
        "grant_type": "client_credentials"
    }

    headers = {"content-type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return response.json()["access_token"]

@server.get("/fetch-groups")
def fetch_groups(token: str = Query(..., description="JWT access token")):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{EXTENSION_URL}/groups", headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    return response.json()

@server.patch("/assign-user-to-group")
def assign_user_to_group(user_id: str, group_id: str, access_token: str):
    url = f"{EXTENSION_URL}/groups/{group_id}/members"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    data = json.dumps([user_id])
    response = requests.patch(url, headers=headers, data=data)

    if response.status_code != 204:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return {"message": f"User successfully assigned to group "}
