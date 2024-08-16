![fastapi](https://github.com/user-attachments/assets/d78b7788-84fa-4f95-bd1d-20a3b84ce87a)# FastAPI-Simple-Blog-API
A basic Blog API built using FastAPI. This API allows you to create, read, update, and delete blog posts. It's designed for easy integration into web and mobile applications.

## Features

- Create new blog posts
- Retrieve all posts or a specific post by ID
- Update existing blog posts
- Delete blog posts

## Installation

1. **Clone the repository:**

     ```bash
     git clone https://github.com/MuhammetEfeSuda/FastAPI-Simple-Blog-API

2. Navigate to the project directory:
  
   ```bash
     cd FastAPI-Simple-Blog-API

4. Set up a virtual environment:
   ```bash
    python -m venv venv

5. Activate the virtual environment:
 - On Windows:
   ```bash
    venv\Scripts\activate

  - On macOS/Linux:
    ```bash
    source venv/bin/activate

6. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

## Usage

1. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload

3. Access the API documentation at:
     - http://127.0.0.1:8000/docs



## API Endpoints
  - GET /posts/ - Retrieve all blog posts
  - GET /posts/{id} - Retrieve a specific blog post by ID
  - POST /posts/ - Create a new blog post
  - PUT /posts/{id} - Update an existing blog post by ID
  - DELETE /posts/{id} - Delete a blog post by ID

  
  ![fastapi](https://github.com/user-attachments/assets/9ac7dd2f-90b5-4cac-8f4b-73fc00459318)



## Testing
  To run tests, make sure you have pytest installed and run:

      pytest








