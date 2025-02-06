import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Auth0 Configuration from environment variables
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")  
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET") 
REDIRECT_URI = os.getenv("REDIRECT_URI")
AUDIENCE = os.getenv("AUDIENCE")
DEFAULT_ROLE_ID = os.getenv("DEFAULT_ROLE_ID")
EXTENSION_URL = os.getenv("EXTENSION_URL")

client_id=os.getenv("API_CLIENT_ID")
client_secret= os.getenv("API_CLIENT_SECRET")
audience= os.getenv("API_AUDIENCE")