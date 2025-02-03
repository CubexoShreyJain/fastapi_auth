import requests
from fastapi import FastAPI, Depends, HTTPException, Header, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.responses import RedirectResponse
import jwt
from jwt import PyJWKClient
import config

main = FastAPI()
security = HTTPBearer()

# Redirects user to the Auth0 login page
@main.get("/")
def register():
    auth0_url = (
        f"https://{config.AUTH0_DOMAIN}/authorize?response_type=code&client_id={config.CLIENT_ID}"
        f"&redirect_uri={config.REDIRECT_URI}&scope=openid profile email&prompt=login&audience={config.AUDIENCE}"
    )
    return RedirectResponse(url=auth0_url)

# Endpoint to exchange the authorization code for an access token
@main.get("/token")
def get_access_token(code: str):
    payload = {
        "grant_type": "authorization_code",
        "client_id": config.CLIENT_ID,
        "client_secret": config.CLIENT_SECRET,
        "code": code,
        "redirect_uri": config.REDIRECT_URI,
    }

    headers = {"content-type": "application/x-www-form-urlencoded","Authorization": f"Bearer {code}"}

    response = requests.post(
        f"https://{config.AUTH0_DOMAIN}/oauth/token", data=payload, headers=headers
    )
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    result = response.json()
    decoded_token = jwt.decode(result["access_token"], options={"verify_signature": False})
    print(result["access_token"])

    user_id = decoded_token.get("sub")
    token=get_authorization_token()
    group_id_data=fetch_groups(token)
    group_id = next((group['_id'] for group in group_id_data['groups'] if group['name'] == 'Employee'), None)

    if user_id:
        assign_user_to_group_helper(user_id,group_id,token)
        assign_role_to_user(user_id, config.DEFAULT_ROLE_ID)

    return {"access_token":token, "decoded_token": decoded_token}

def get_authorization_token():
    url = f"https://{config.AUTH0_DOMAIN}/oauth/token"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "client_id": config.client_id,
        "client_secret": config.client_secret,
        "audience": config.audience,
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
@main.post("/role")
async def create_role(request:Request,token=Header(None)):
    body = await request.json()
    name = body['name']
    description = body['description']

    url = f"https://{config.AUTH0_DOMAIN}/api/v2/roles"

    headers = {
        "cache-control": "no-cache",
        "content-type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    data = {"name": name, "description": description}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return response.json()

# Endpoint to assign a role to a user
@main.post("/assign-role")
def assign_role(user_id: str, role_id: str):
    assign_role_to_user(user_id, role_id)
    return {"message": "Role assigned successfully"}

# Helper function to assign role to a user
def assign_role_to_user(user_id: str, role_id: str):
    management_token = get_management_api_token()
    url = f"https://{config.AUTH0_DOMAIN}/api/v2/users/{user_id}/roles"

    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {management_token}",
    }
    data = {"roles": [role_id]}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 204:
        raise HTTPException(status_code=response.status_code, detail=response.text)

# Protected route that requires a valid JWT token to access
@main.get("/protected")
def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    jwks_url = f"https://{config.AUTH0_DOMAIN}/.well-known/jwks.json"
    jwks_client = PyJWKClient(jwks_url)
    signing_key = jwks_client.get_signing_key_from_jwt(token).key

    try:
        payload = jwt.decode(
            token,
            signing_key,
            algorithms=["RS256"],
            audience=config.AUDIENCE,
            issuer=f"https://{config.AUTH0_DOMAIN}/"
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")

    return {"message": "Access granted", "user": payload}

# Middleware to enforce permissions for accessing protected routes
@main.middleware("http")
async def enforce_permissions(request, call_next):
    if request.url.path.startswith("/protected"):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            raise HTTPException(status_code=401, detail="Authorization header missing")

        token = auth_header.split()[1]
        jwks_url = f"https://{config.AUTH0_DOMAIN}/.well-known/jwks.json"
        jwks_client = PyJWKClient(jwks_url)
        signing_key = jwks_client.get_signing_key_from_jwt(token).key

        try:
            payload = jwt.decode(
                token,
                signing_key,
                algorithms=["RS256"],
                audience=config.AUDIENCE,
                issuer=f"https://{config.AUTH0_DOMAIN}/"
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
    url = f"https://{config.AUTH0_DOMAIN}/oauth/token"
    payload = {
        "client_id": config.CLIENT_ID,
        "client_secret": config.CLIENT_SECRET,
        "audience": f"https://{config.AUTH0_DOMAIN}/api/v2/",
        "grant_type": "client_credentials"
    }

    headers = {"content-type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return response.json()["access_token"]

@main.get("/fetch-groups")
def fetch_groups(token: str):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{config.EXTENSION_URL}/groups", headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    return response.json()

# Endpoint to assign a user to a group
@main.patch("/assign-user-to-group")
async def assign_user_to_group(request: Request, Authorization: str = Header(None)):
    body = await request.json()
    user_id = body["user_id"]
    group_id = body["group_id"]

    response = assign_user_to_group_helper(user_id, group_id, Authorization)

    if response.status_code != 204:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return {"message": "User successfully assigned to group"}

def assign_user_to_group_helper(user_id: str, group_id: str, token: str):
    url = f"{config.EXTENSION_URL}/groups/{group_id}/members"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    data = [user_id]
    return requests.patch(url, headers=headers, json=data)

# Endpoint to assign a role to a group
@main.patch("/assign-role-to-group")
async def assign_role_to_group(request:Request,Authorization: str=Header(None)):
    body=await request.json()
    group_id=body["group_id"]
    role_id=body["role_id"]

    url = f"{config.EXTENSION_URL}/groups/{group_id}/roles"

    headers = {
        "Content-Type": "application/json",
        "Authorization": Authorization
    }

    data=[role_id]
    response = requests.patch(url, headers=headers, json=data)

    if response.status_code != 204:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return {"message": f"Role successfully assigned to group "}
