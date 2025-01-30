import os
from dotenv import load_dotenv
#load env file
load_dotenv()


# Set up Auth0 credentials
DOMAIN = os.getenv('DOMAIN') #dev-vgwol4rrkbyri5sm.us.auth0.com 
CLIENT_ID = os.getenv('CLIENT_ID_API') #LiRWtm33Heceqw7K833qdUC2qOQJTbJW
CLIENT_SECRET = os.getenv('CLIENT_SECRET_API') #HiW4jGOwmShbMN1Kl7MfH19BGgQznNht9pmrNYpR1eVnNf7TGwNKVWHod92Xr3Er
DEFAULT_ROLE_ID = os.getenv('DEFAULT_ROLE_ID')
CLIENT_ID_APP = os.getenv('CLIENT_ID_APP')
CLIENT_SECRET_APP = os.getenv('CLIENT_SECRET_APP')
REDIRECT_URI_TOKEN = os.getenv('REDIRECT_URI_TOKEN')
REDIRECT_URI_DOCS = os.getenv('REDIRECT_URI_DOCS')
URL_EXTENTION = os.getenv('URL_EXTENTION')