import os
from dotenv import load_dotenv

load_dotenv()
class Data:
    """Забирает данные с файла .env и присваивает к переменным"""
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
    INVALID_LOGINS = os.getenv("INVALID_LOGIN")
    INVALID_PASSWORDS = os.getenv("INVALID_PASSWORDS")
    SECRET_COMMENT = os.getenv("SECRET_COMMENT")