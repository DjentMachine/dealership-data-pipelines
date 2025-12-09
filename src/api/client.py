import os
import time
import requests
import dotenv


class APIClient:
    def __init__(self, base_url, auth_handler, timeout=10, max_retries=3):
        self.base_url = base_url
        self.auth_handler = auth_handler
        self.timeout= timeout
        self.max_retries= max_retries
        
    def get(self, endpoint, params=None):
        #TODO:Lets build the URLs here, add headers and rety logic
        r=requests.get(self.base_url+endpoint,
                     headers = self.auth_handler.get_headers(),
                     params=params)
        
        if r.status_code == 200:
            print(f"API request sucessful for the endpoint {endpoint}")
        else:
            print("ERROR: network error")


        
        #TODO: PAGINATION, TOO MANY REQUEST (429)
        
