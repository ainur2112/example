import os
from dotenv import load_dotenv

load_dotenv()
class Data:

    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
    INVALID_LOGINS = os.getenv("INVALID_LOGIN")
    INVALID_PASSWORDS = os.getenv("INVALID_PASSWORDS")