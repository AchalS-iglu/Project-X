import os
from dotenv import load_dotenv

load_dotenv()

IMGUR_CLIENT_ID =  os.environ.get("IMGUR_CLIENT_ID")
IMGUR_CLIENT_SECRET = os.environ.get("IMGUR_CLIENT_SECRET")

import configparser

authParser = configparser.ConfigParser()
authParser.read('auth.ini')


MEDIAFIRE_EMAIL = authParser['MEDIAFIRE']['EMAIL']
MEDIAFIRE_PASS = authParser['MEDIAFIRE']['PASS']