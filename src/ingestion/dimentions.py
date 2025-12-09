"""
Dimention ingestion. Dimentions are updated seldomly and decent orchestration 
will ensure this runs only when needed
"""

import requests
import dotenv
import os
from ..api.client import APIClient
from ..api.auth import APIKeyAuth

#load .env
dotenv.load_dotenv()

#Different endpoints
ep_makes = "api/makes/v2"
ep_models = "api/models/v2"
ep_submodels = "api/submodels/v2"
ep_attributes = "api/vehicle-attributes"

#API Authentication
handler = APIKeyAuth()
client = APIClient(base_url=os.getenv("API_BASE"), auth_handler=handler)

print(client.base_url)

#URL building
makes_request = client.get(ep_makes)
models_request = client.get(ep_models)
submodels_request = client.get(ep_submodels)
attributes_request = client.get(ep_attributes)

#Test logic so far
#print(makes_request)

#Load dimentions



#TODO: Load into postgres docker 
# something along the lines of
"""
def update_dimensions(client, warehouse):
    raw_dims = fetch_dimension_data(client)
    cleaned_dims = transform_dimensions(raw_dims)
    updated = warehouse.upsert_dimensions(cleaned_dims)
    return updated
"""



