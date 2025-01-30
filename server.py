import requests
from fastapi import FastAPI, Security
from starlette.responses import RedirectResponse
import jwt
import json
import os 
from config import DOMAIN,CLIENT_ID,CLIENT_SECRET,CLIENT_ID_APP,CLIENT_SECRET_APP,DEFAULT_ROLE_ID,REDIRECT_URI_TOKEN,REDIRECT_URI_DOCS,URL_EXTENTION

#create a app of fastapi
server = FastAPI()

#login from the autho0 login page
@server.get('/')
def login():
    return RedirectResponse(
        f"https://{DOMAIN}/authorize"
        "?response_type=code"
        f"&client_id={CLIENT_ID_APP}"
        f"&redirect_uri={REDIRECT_URI_TOKEN}"
        "&scope= openid profile email&prompt=login"
        "&audience=https://microapis.io/api/orders"
    )

#redirect to the fastapi docs page
@server.get("/login")
def register():
    return RedirectResponse(
        f"https://{DOMAIN}/authorize"
        "?response_type=code"
        f"&client_id={CLIENT_SECRET_APP}"
        f"&redirect_uri={REDIRECT_URI_DOCS}"
        "&scope=offline_access openid profile email"
        "&audience=https://microapis.io/api/orders"
    )

#redirect to the fastapi docs page
@server.get("/token")
def get_access_token_and_get_roles_permission(code: str):
    payload = (
        "grant_type=authorization_code"
        f"&client_id={CLIENT_ID_APP}"
        f"&client_secret={CLIENT_SECRET_APP}"
        f"&code={code}"
        f"&redirect_uri=http://localhost:8000/docs"
    )
    access_token = {code}
    headers = {"content-type": "application/x-www-form-urlencoded",'Authorization': f"Bearer {access_token}"}
    response = requests.post(f"https://{DOMAIN}/oauth/token", payload, headers=headers)

    #excpetion handling
    if response.status_code == 200:

    #call my custumer middleware for extrating user informations
        extract_user(response)
    else:
        print(f" Failed to fetch token. Status code: {response.status_code}")
        print("Response:", response.text)

    #excpetion handling
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch groups. Status code: {response.status_code}")
        print(response.text)

# create middleware to extract the user informations using jwt tokens
def extract_user(resp):
    # decode the access_token using jwt.decode
    res = resp.json()['access_token']
    decode_info = jwt.decode(res, options={"verify_signature": False})

    #print the roles and permission
    print('Role: ',decode_info['your_name_space/roles'])
    print('Permissions: ',decode_info['permissions'])

    #get authorization token to call get-authorization_token function
    token =get_authorization_token() 
    group = get_groups(token)
    group_id=group["groups"][0]['_id']

    #add the current user to the groups member
    add_group_member(group_id,token,decode_info['sub'])

    #call the asssign_default_role and add default role to the login user
    assign_default_role(decode_info['sub'])

# get authorizations token 
def get_authorization_token():
    url = f"https://{DOMAIN}/oauth/token"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "client_id": f"{CLIENT_ID}",
        "client_secret": f"{CLIENT_SECRET}",
        "audience": "urn:auth0-authz-api",
        "grant_type": "client_credentials"
    }
    response = requests.post(url, headers=headers, json=data)

    #excpetion handling
    if response.status_code == 200:
        token_info = response.json()
        return token_info.get("access_token")
    else:
        print(f" Failed to fetch token. Status code: {response.status_code}")
        print("Response:", response.text)

#create roles for user
@server.post('/create_roles')
def create_roles(name,description,token):
    url = f"https://{DOMAIN}/api/v2/roles"
    headers = {
            "cache-control": "no-cache",
            "content-type": "application/json",
            "Authorization": f"Bearer {token}"
        }
    data = {
            "name": f"{name}",
            "description": f"{description}"
        }
    response = requests.post(url, headers=headers, json=data)

    #excpetion handling
    if response.status_code == 200:
        t = response.json().get("access_token")
        return t
    else:
        print(f"Failed to create roles. Status code: {response.status_code}")
        print(response.text)

#assign default role to the user
def assign_default_role(user_id):
    payload_token  = {"client_id":f"{CLIENT_ID}","client_secret":f"{CLIENT_SECRET}","audience":f"https://{DOMAIN}/api/v2/","grant_type":"client_credentials"}
    response_token = requests.post(f"https://{DOMAIN}/oauth/token", payload_token)
    access_token = response_token.json()['access_token']
    response_token.raise_for_status()

    # Assign role to user
    assign_role_url = f"https://{DOMAIN}/api/v2/users/{user_id}/roles"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {"roles": [DEFAULT_ROLE_ID]}

    #excpetion handling
    try:
        response = requests.post(assign_role_url, json=data, headers=headers)
        response.raise_for_status()
        print("Role assigned successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error assigning role: {e}")

#get groups from the authorization      
def get_groups(token):
    api_url = f"{URL_EXTENTION}/groups"
    auth_token = token
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(api_url, headers=headers)

    #excpetion handling
    if response.status_code == 200:
        groups = response.json()
        return groups
    else:
        print(f"Failed to fetch groups. Status code: {response.status_code}")
        print(response.text)

# add member in groups
@server.patch('/add-member')
def add_group_member(group_id,token,user_id):
    url = f"{URL_EXTENTION}/groups/{group_id}/members"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = json.dumps([user_id])

    #excpetion handling
    try:
        response = requests.patch(url, headers=headers, data=data)
        
        if response.status_code == 204:
            print("Member added successfully! (204 No Content)")
        elif response.status_code == 200:
            print("Member added successfully:", response.json())
        else:
            print(f"Failed to update members. Status code: {response.status_code}")
            print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
