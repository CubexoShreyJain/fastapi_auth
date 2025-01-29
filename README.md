# Auth0 Implementation in FastAPI
This project integrates FastAPI with Auth0 for authentication and authorization.

## To start the server follow below steps:
create virtual environment: python -m venv venv
activate virtual environment: ./venv/Scripts/activate
Install dependencies: pip install -r requirements.txt
Run the FastAPI server: uvicorn server:server --reload

## Configuration:
Set up Auth0 Tenant
AUTH0_DOMAIN = "your-auth0-domain"
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
REDIRECT_URI = "http://localhost:8000/docs"
AUDIENCE = "your-audience"
DEFAULT_ROLE_ID = "your-default-role-id"
EXTENSION_URL = "your-extension-url"

## Endpoints:
GET / - Redirects to Auth0 login
GET /login - Starts Auth0 login flow
GET /token - Exchanges authorization code for JWT token
GET /protected - Protected route requiring valid JWT
POST /role - Creates a new role in Auth0
POST /assign-role - Assigns role to a user
GET /fetch-groups - Fetches available Auth0 groups
PATCH /assign-user-to-group - Assigns user to a group