# Blog API with JWT Authentication (Django REST Framework)

## Introduction

This project is a **Blog REST API** built using **Django REST Framework (DRF)** with **JSON Web Token (JWT)** based authentication.  
It allows users to securely register, log in, and manage blog posts using token-based access control.  
This API is suitable for learning, backend practice, and portfolio showcase.

---

## Features

- User registration and login using **JWT authentication**
- Secure token-based access for protected APIs
- Create, read, update, and delete (CRUD) blog posts
- Public access to view blog posts
- Clean RESTful API architecture
- Role-based access for authenticated users

---

## Authentication Flow (JWT)

1. User registers or logs in using credentials
2. Server returns a **JWT access token**
3. Token is sent in the request header for protected APIs
4. Server validates token before allowing access


---

## API Capabilities

### User APIs
- Register new user
- Login user and generate JWT token

### Blog APIs
- Create blog post (Authenticated)
- Update blog post (Authenticated)
- Delete blog post (Authenticated)
- View all blog posts (Public)

---

## Tech Stack

- **Backend Framework:** Django REST Framework
- **Language:** Python
- **Authentication:** JSON Web Token (JWT)
- **Database:** Django-supported database (PostgreSQL)
- **API Format:** REST (JSON)

---

## Use Cases

- Learning JWT authentication in Django REST Framework
- Understanding secure REST API design
- Backend developer portfolio project
- Practice for authentication & authorization concepts

---

## Project Repository

GitHub Repository:  
https://github.com/Dileepkumarpatelpalamu/blog-api-jwt

---

## Conclusion

This project demonstrates a **secure and scalable backend API** using Django REST Framework and JWT authentication.  
It highlights practical implementation of authentication, authorization, and RESTful API design, making it a strong backend portfolio project.
