# Library Management System Using FASTAPI


This is a simple library management system's api created using FastAPI for the endpoint, SQLAlchemy for ORM and PostgreSQL for the backend database.



## How to run this code?

1. Clone the repo and move to the file

   Clone this repo or you can download the zip file from above. To clone using terminal, go to your required file loation and open terminal there, then enter following commands.

   ```bash
      git clone https://github.com/GR00th/Library-API-try.git
      ```

      This will create make a directory `. Now we need to move inside the folder, i.e

      ```bash
      cd library_management_system_fastAPI
      ```

2. Create a .env file
 The file must follow this format

   ```bash
   host=database_host
   database=database_name
   user=database_username
   password=database_password
   secret=AccessToken_secret_key
   algorithm=Token_algorithm
   secret_refresh = RefreshToken_secret_key
   ```

3. Install requirements

   Run `pip install -r requirements.txt`

4. Run the script

   Run the script with `uvicorn main:app --reload`

   The `--reload` flag as the name suggest will watch your file for change and reload the endpoint. One of the important flag is `--host 0.0.0.0` that will host the endpoint to your local ip.

## Docs

   To know more about the endpoint and expected format you can got to `localhost/docs`(that is if you are hosting the api in your localhost)
   You can also use that swaager API docs to test the api.

## Login and Authorization

   I have use simple JWT token i.e Access token and Refresh token. You need to login as an librarian to get access to the access and refresh token at `/login` endpoint with post method with the email and password in body. Curently the access token is set to expire in 20 minutes and the refresh token is valid till about one week. Once you have sucessfully login, you need to save the both access refresh token. Once the access token expires, you need to hit the `/refresh` endpoint with get method and the saved refresh token as the query parameter, i.e `/refresh?refreshToken=savedrefreshtoken`.

   In this way you can have prescistance login for a librarian.

## Access the protected route/endpoints

   Once you got access to the access token, you need to send it in each requests header as a bearer token. Here is a sample curl command with dummy access token.

   ```bash
   curl -X 'GET' \
  'http://localhost:8000/user/test' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySUQiOiJhZG1pbkBsbXMuY29tIiwiZXhwaXJ5IjoxNzEwMTMyMDk2LjAzODc5MX0.Hz1JLerxq8fmsDL0U82m7DU1l8e04QPIzfpJJs8jKE4'
   ```

   And it will return a JSON data as

   ```JSON
   {
     "User": {
       "user_details": {
         "username": "Test",
         "expiry_date": "2024-04-28T00:00:00",
         "fine": 0,
         "id": 1,
         "email": "email1",
         "date_created": "2024-02-28T00:00:00",
         "address": "address",
         "phone_number": 5678910111213
       }
     }
   }
   ```
5. Aditional questions
Additional Strategies

Authentication: Use OAuth2PasswordBearer to secure endpoints.
Pagination: Implement limit and skip in queries.
Security: Use SQLAlchemy to prevent SQL injection; validate inputs with Pydantic.






## TODO

- [ ] Add option to update or remove members and books or magazines.
- [ ]  Testing
- [X] ~~User login (Maybe)~~
  
## Conclusion

   This is a simple FastApi example and it is nowhere near complete, This is created with sole purpose of understanding the fast api, router and authentication using JWT token, also im rusted AF.
