##
# Authentication handler.
# Assumes an API key is passed.
## 

class APIKeyAuth:

    def __init__(self, api_key: str):
        self.api_key= api_key
    
    #returns a dictionary with the  
    def add_auth(self,headers: dict) -> dict:
        headers["Authorization"] = f"Bearer {self.api_key}"
        return  headers
