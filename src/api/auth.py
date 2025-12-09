##
# Authentication handler.
# Assumes an API key is passed.
## 
import os
from dotenv import load_dotenv

#load the .env file
load_dotenv()

class APIKeyAuth:
    def __init__(self):
        self.api_key= os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError("API_KEY not found!")
    
    #returns a dictionary with the headers, including auth 
    def get_headers(self):
        return  {
            'Authorization': f'Bearer {self.api_key}',
            'Accept': 'application/json'
        }
