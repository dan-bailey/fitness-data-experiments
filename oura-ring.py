import os
from dotenv import load_dotenv
from oura_ring import OuraClient

# Load the .env file
load_dotenv()

# Get the access token from the environment
access_token = os.getenv("OURA_RING_ACCESS_TOKEN")

# Let's connect to the Oura API
# Using a traditional constructor
client = OuraClient(access_token)

# Get basic user info
user_info = client.get_personal_info()
print(user_info)


