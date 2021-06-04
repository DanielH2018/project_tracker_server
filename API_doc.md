# Project Tracker Server API

## Models

### Model: User (Django built-in)
```
{
    username: string,
    email: string,
    password: string,
}
```

### Model: Project
```
{
    id: int,
    name: string,
    description: string,
    owner: string, (username),
}
```

### Model: Project Membership
```
{
    id: int,
    project: int,
    owner: string, (username),
    location: int
    permission_level: int,
}
```

### Model: Task
```
{
    id: int,
    project: int,
    owner: string, (username),
    name: string,
    description: string, (Max length 200),
    category: string, (Max length 20),
    priority: int,
    status: int,
}
```

## Endpoints

### Auth Endpoints
```
See [Djoser Docs](https://djoser.readthedocs.io/en/latest/base_endpoints.html) for authorization endpoints
```

### User Endpoints

#### GET
```
GET /users/
Authorization: Token
{
    none
}
Body:
    None
Returns:
    List of users
```

#### GET
```
GET /users/<id>/
Authorization: Token
{
    none
}
Body:
    None
Returns:
    Username, if exists
```

### Project Endpoints

#### GET
```
GET /projects/
Authorization: Token

{
    id: int,
    name: string,
    description: string,
    owner: string, (username),
    location: int,
    membership: int,
    permission_level: int,
}
Body:
    Any fields to filter on
Returns:
    List of models based on field filters
```

#### GET
```
GET /projects/<id>/
Authorization: Token

{
    none
}
Body:
    None
Returns:
    Model, if it exists, with location, membership id, and permission level associated with requesting user and project
```

#### POST
```
POST /projects/
Authorization: Token
{
    name: string,
    description: string,
}
Body:
    Required model fields(name, description)
Returns:
    The created model on success
```

#### PATCH
```
PATCH /projects/<id>/
Authorization: Token
{
    name: string,
    description: string,
    owner: string, (username),
}
Body:
    The desired fields to update
Returns:
    The updated model on success
```

#### DELETE
```
DELETE /projects/<id>/
Authorization: Token
{
    none
}
Body:
    none
Returns:
    HTTP Response Code
```

### Project Membership Endpoints

#### GET
```
GET /projectmemberships/
Authorization: Token
{
    id: int,
    project: int,
    owner: string, (username),
    location: int,
    permission_level: int,
    
}
Body:
    Any fields to filter on
Returns:
    List of memberships based on field filters
```

#### GET
```
GET /projectmemberships/<id>/
Authorization: Token
{
    none
}
Body:
    None
Returns:
    Model, if it exists
```

#### POST
```
POST /projectmemberships/
Authorization: Token
{
    project: int,
    owner: string, (username),
    location: int, (default 1)
    permission_level: int,
}
Body:
    All model fields
Returns:
    The created model on success
```

#### PATCH
```
PATCH /projectmemberships/<id>/
Authorization: Token
{
    project: int,
    location: int,
    permission_level: int,
}
Body:
    The desired fields to update
Returns:
    The updated model on success
```

#### DELETE
```
DELETE /projectmemberships/<id>/
Authorization: Token
{
    none
}
Body:
    none
Returns:
    HTTP Response Code
```

### Task Endpoints

#### GET
```
GET /tasks/
Authorization: Token
{
    id: int,
    project: int,
    owner: string, (username),
    name: string,
    description: string, (Max length 200),
    category: int,
    priority: int,
    status: int,
}
Body:
    Any fields to filter on
Returns:
    List of models based on field filters
```

#### GET
```
GET /tasks/<id>/
Authorization: Token
{
    none
}
Body:
    None
Returns:
    Model, if it exists
```

#### POST
```
POST /tasks/
Authorization: Token
{
    project: int,
    description: string, (Max length 200),
    category: int,
    priority: int,
    status: int,
}
Body:
    All model fields
Returns:
    The created model on success
```

#### PATCH
```
PATCH /tasks/<id>/
Authorization: Token
{
    project: int,
    owner: string, (username),
    description: string, (Max length 200),
    category: int,
    priority: int,
    status: int,
}
Body:
    The desired fields to update
Returns:
    The updated model on success
```

#### DELETE
```
DELETE /tasks/<id>/
Authorization: Token
{
    none
}
Body:
    none
Returns:
    HTTP Response Code
```
