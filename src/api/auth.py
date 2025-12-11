##
# Authentication handler.
# Assumes an API key is passed.
## 
import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

#load the .env file
load_dotenv()

class APIAuth:

    def __init__(self):
        self.api_token = os.getenv("API_TOKEN")
        self.api_secret = os.getenv("API_SECRET")
        self.jwt = None
        
        if not self.api_token or not self.api_secret:
            raise ValueError("API_TOKEN or API_SECRET not found! Is .env well configured?")

    #Is the current JWT valid? Returns a boolean
    def jwt_valid(self):
        if not self.jwt:
            return False
        else:
            return True        

    #Gets a jwt for authentication. If token expired or about to, creates a new one         
    def request_new_jwt(self):
        url = "https://carapi.app/api/auth/login"
        headers = {"Content-Type": "application/json", "accept": "text/plain"}

        #post request to the service, including API token and secret
        response = requests.post(url, json={"api_token": self.api_token, "api_secret": self.api_secret}, headers=headers)
        self.jwt=response.text #storing the token

    def get_jwt(self):
        if self.jwt_valid():    
            return self.jwt
        else:
            self.request_new_jwt()
            return self.jwt

    #returns a dictionary with the headers, including auth 
    def get_headers(self):
        return  {
            'Authorization': f'Bearer {self.jwt}',
            'Accept': 'application/json'
        }
