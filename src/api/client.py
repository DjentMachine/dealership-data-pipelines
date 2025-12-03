import os
import time
import requests


#
class APIClient:
    def __init__(self, base_url, auth_handler, timeout=10, max_retries=3):
        self.base_url = base_url
        self.auth_handler = auth_handler
        self.timeout= timeout
        self.max_retries= max_retries

    def get(self, endpoint, params=None):
        
        #TODO:Lets build the URLs here

        pass

        #TODO: PAGINATION, TOO MANY REQUEST (429)
        
