# Auth0 implementation in FastAPI

## Description

This project integrates authentication and authorization using **Auth0** in a **FastAPI** application. It implements group-based access control, ensuring users can be assigned to groups with specific permissions.

## Objective

- Implement **Auth0 authentication** in FastAPI.
- Enable **group-based permission management**.

## Features

- **Auth0 integration** for user authentication.
- **JWT-based authentication** middleware.
- **Group-based access control** with permissions.
- **Route-level permission checks**.
- **Dynamic user-group assignments**.
- **Comprehensive error handling** for unauthorized access.

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Auth0 credentials**

   ```
   AUTH0_DOMAIN=your-auth0-domain
   API_IDENTIFIER=your-api-identifier
   CLIENT_ID=your-client-id
   CLIENT_SECRET=your-client-secret
   ```
## API Endpoints

Login from the Auth0 login page
```
@server.get('/')
```

Redirect to the FastAPI docs page
```
@server.get("/login")
```

Redirect to the FastAPI docs page
```
@server.get("/token")
```

Create roles for users
```
@server.post('/create_roles')
```

Add member to a role
```
@server.patch('/add-member')
```
## Usage

1. **Run the FastAPI server**

   ```bash
   uvicorn main:app --reload
   ```

2. **Access API documentation**

   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Deliverables

- **Authentication & Authorization Flow**

  - User logs in via Auth0.
  - Auth0 assigns user to a group based on predefined rules.
  - JWT token is issued with user role and permissions.
  - FastAPI verifies JWT and extracts user details.
  - Access to routes is controlled based on user permissions.

- **Middleware & Security**

  - JWT Middleware for token validation.
  - Role-based access control (RBAC) enforcement.
  - Exception handling for unauthorized access.

## Acceptance Criteria

- **Auth0 authentication** works seamlessly for all API endpoints.

- **Users are assigned to groups dynamically based on the application logic.**

- **Permissions are enforced at the group level to restrict access to specific routes.**

- **Appropriate error handling is implemented for unauthorized and unauthenticated access.**

- **Detailed documentation is provided on how to configure Auth0 for the application, including tenant setup, application creation, and group/permission management.**