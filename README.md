# Simple microservice for managing posts
 
This is a simple microservice API created in Django with simple CRUD functions.

### SETUP:
The project is meant to be run as a Docker container - to initialise it, make sure you have installed Docker from https://www.docker.com/products/docker-desktop/. Next, just run run the following command in the project's main directory: 

> docker-compose up

Docker will then grab all the required packages and will start a server at http://localhost:8000.

Next, I recommend creating a superuser account by running the following command in the project directory

> python manage.py createsuperuser

You will then be able to set your superuser name and password - this is handy for accessing the admin.

This is just the API without any frontend, therefore I recommend using Postman (https://web.postman.co/) or an alternative service to see the data and manage  requests.

The endpoints are:

> /admin

for accessing the admin dashboard,

> /api/posts

for retrieving a list of all the posts from the database with a GET request, or creating a new post with a POST request, and

> /api/[ID]

which retrieves the details of a specific post with the given ID with a GET request, edits the post at that ID with a PUT request, or deletes the selected post from the database with a DELETE request.
