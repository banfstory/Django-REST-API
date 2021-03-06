# Django-REST-API

The RESTful API allows users to create their own forums which gives a place for other users to create post

FLASK RESTFUL API INSTRUCTIONS: To run the Flask API, it needs to run on a local server and it will be running the application from a virtual environment so that all packages will be already pre-installed within the whole folder itself.

To run the virtual environment do the following (instructions for windows OS only), start with going into command prompt:

1.Go to root directory of this folder <br />
2.Enter '.\Scripts\activate' to activate the virtual <br />
3.Go to src folder <br />
4.Enter 'python manage.py runserver 127.0.0.1:8000' to run the local server or choose whatever address or port number you want <br />

RESTFUL API AUTHENTICATION
In order to access certain resources or perform certain actions, the user needs to authenticate themselves by providing their username and password where they will be given an access token and a refesh token. The access token provides authorization for the user to access to resources and perform actions that are otherwised restricted if no access token was provided. The refresh token will be required to refresh the access token that has expired (access token expires in 7 days but can be changed in the settings.py file located in the django_api folder). These tokens are represented as JSON web tokens (JWT) and these tokens are separated by period in between representing encoded header data and payload data with the signature to ensures that no one can create their own tokens and pretend to be someone else.

To authenticate a user and get the tokens use http:<span></span>//127.0.0.1:8000/api/token/ as a POST method with the header as 'Content-Type: application/json' and data as '{"username":"your username","password":"your password"}', for example in curl you can use 'curl -X POST -H 'Content-Type: application/json' -d '{"username":"admin","password":"pass"}' http:<span></span>//127.0.0.1:8000/api/token/' to authenticate. 

To refresh an expired token, you can use http:<span></span>//127.0.0.1:8000/api/token/refresh/ as a POST method with the header 'Content-Type: application/json' and data as '{"refresh":"your refresh token"}', for example in curl you can use 'curl -X POST -H 'Content-Type: application/json' -d '{"refresh":"your refresh token"}' http:<span></span>//127.0.0.1:8000/api/token/refresh/'

Certain endpoints are only accessible if you provide the access token. To provide an access token, provide the header with "Authorization: Bearer *Your access token*", for example in curl you can use 'curl -X PUT -H 'Content-Type: application/json' -H "Authorization: Bearer *Your access token*" -d '{"username":"admin", "email":"admin@gmail.<span></span>com"}' http:<span></span>//127.0.0.1:8000/api/users/1/'

NOTE: You can authenticate as admin with the username 'admin' and password 'pass'

RESTFUL API ENDPOINTS

The API endpoints are broken down into catrgories, these are USERS, FORUMS, POSTS, COMMENTS, REPLYS

NOTE: Endpoints that return multiple results will only show 10 results per page. To navigate through each page, add the query param 'page' with the page number into URL endpoint
NOTE: When sending files with data, both the files and data must be sent as form data with header Content-Type: multipart/form-data instead of Content-Type: application/json, for example in curl you can use curl -X PUT -H 'Content-Type: multipart/form-data' -H "Authorization: Bearer *Your access token*" -F 'image=@*your file path*' -F 'username=admin' -F 'email=admin@gmail.<span></span>com' http:<span></span>//127.0.0.1:8000/api/users/1/
 
--- USERS ENDPOINTS ---

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/users/ <br/>
METHOD: GET <br/>
DESCRIPTION: Get details of all users accounts <br/>
QUERY PARAMS: q, username, page <br/>

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/users/ <br/>
METHOD: POST <br/>
DESCRIPTION: Register a user account <br/>
HEADER: Content-Type: application/json <br/>
DATA: username, email, password <br/>

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/users/<int:pk>/ <br/>
METHOD: GET <br/>
DESCRIPTION: Get a user account <br/>

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/users/<int:pk>/ <br/>
METHOD: PUT <br/>
DESCRIPTION: Update user account details <br/>
HEADER: Content-Type: application/json (without image file), 'Content-Type: multipart/form-data' (with image file), Authorization: Bearer *Your access token* <br/>
FILE: image <br/>
DATA: username, email <br/>

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/users/followers/ <br/>
METHOD: GET <br/>
DESCRIPTION: Get followers list of which users are following which forums <br/>
PARAM: user, forum <br/>

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/users/followers/ <br/>
METHOD: POST <br/>
DESCRIPTION: User follows a forum <br/>
HEADER: Content-Type: application/json, Authorization: Bearer *Your access token* <br/>
DATA: forum <br/>

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/users/<int:pk>/followers/ <br/>
METHOD: GET <br/>
DESCRIPTION: Get a instance of a user who is following a forum <br/>
DATA: forum <br/>

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/users/<int:pk>/followers/ <br/>
METHOD: DELETE <br/>
DESCRIPTION: User unfollows a forum <br/>

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/users/default-image/ <br/>
METHOD: PUT <br/>
DESCRIPTION: Set user image to default image <br/>
HEADER: Authorization: Bearer *Your access token* <br/>

--- FORUMS ENDPOINTS ---

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/forums/ <br/>
METHOD: GET <br/>
DESCRIPTION: Get details of all forums <br/>
QUERY PARAMS: q, name, owner, page <br/>

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/forums/ <br/>
METHOD: POST <br/>
DESCRIPTION: Create forum <br/>
HEADER: Content-Type: application/json <br/>
DATA: name, about <br/>

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/forums/<int:pk>/ <br/>
METHOD: GET <br/>
DESCRIPTION: Get a user account <br/>

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/forums/<int:pk>/ <br/>
METHOD: PUT <br/>
DESCRIPTION: Update user's forum details <br/>
HEADER: Content-Type: application/json (without image file), 'Content-Type: multipart/form-data' (with image file), Authorization: Bearer *Your access token* <br/>
FILE: image <br/>
DATA: name, about <br/>

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/forums/<int:pk>/ <br/>
METHOD: DELETE <br/>
DESCRIPTION: Delete forum <br/>
HEADER: Authorization: Bearer *Your access token* <br/>

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/forums/<int:pk>/default-image/ <br/>
METHOD: PUT <br/>
DESCRIPTION: Set forum image to default image <br/>
HEADER: Authorization: Bearer *Your access token* <br/>

--- POSTS ENDPOINT ---

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/posts/
METHOD: GET
DESCRIPTION: Get details of all posts
QUERY PARAMS: forum, user

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/posts/
METHOD: POST
DESCRIPTION: Create post for the forum
HEADER: Content-Type: application/json, Authorization: Bearer *Your access token*
DATA: title, content, forum

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/posts/<int:pk>/
METHOD: GET
DESCRIPTION: Get details of a post

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/posts/<int:pk>/
METHOD: PUT
DESCRIPTION: Update user's post details
HEADER: Content-Type: application/json, Authorization: Bearer *Your access token*
DATA: title, content

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/posts/<int:pk>/
METHOD: DELETE
DESCRIPTION: Delete user's post
HEADER: Authorization: Bearer *Your access token*

--- COMMENTS ENDPOINT ---

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/comments/
METHOD: GET
DESCRIPTION: Get details of all comments
QUERY PARAMS: post, user

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/comments/
METHOD: POST
DESCRIPTION: Create comment for the post
HEADER: Content-Type: application/json, Authorization: Bearer *Your access token*
DATA: content, post

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/comments/<int:pk>/
METHOD: GET
DESCRIPTION: Get details of a comment

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/comments/<int:pk>/
METHOD: PUT
DESCRIPTION: Update user's comment details
HEADER: Content-Type: application/json, Authorization: Bearer *Your access token*
DATA: content

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/comments/<int:pk>/
METHOD: DELETE
DESCRIPTION: Delete user's comment
HEADER: Authorization: Bearer *Your access token*

--- REPLYS ENDPOINT ---

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/replys/
METHOD: GET
DESCRIPTION: Get details of all replys
QUERY PARAMS: comment, user

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/replys/
METHOD: POST
DESCRIPTION: Create reply for the comment
HEADER: Content-Type: application/json, Authorization: Bearer *Your access token*
DATA: content, comment

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/replys/<int:pk>/
METHOD: GET
DESCRIPTION: Get details of a reply

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/comments/<int:pk>/
METHOD: PUT
DESCRIPTION: Update user's reply details
HEADER: Content-Type: application/json, Authorization: Bearer *Your access token*
DATA: content

ENDPOINT: http:<span></span>//127.0.0.1:8000/api/replys/<int:pk>/
METHOD: DELETE
DESCRIPTION: Delete user's reply
HEADER: Authorization: Bearer *Your access token*

