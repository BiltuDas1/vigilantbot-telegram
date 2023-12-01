from dotenv import load_dotenv
import os
from . import error
import re

class Environment:
    """
    Loads all the required Environments from the system
    """
    def __init__(self):
        # Loading .env file (If exists)
        load_dotenv()

        # Loading Environments to variables
        self.__load_environ()

        # Verifying
        self.__validate_bot_token()
        self.__validate_web_app_port()


    def __load_environ(self):
        self.TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
        self.SPAMWATCH_API_KEY = os.getenv("SPAMWATCH_API_KEY")
        self.WEB_APP_PORT = os.getenv("PORT")
        
    def __validate_bot_token(self):
        if self.TG_BOT_TOKEN is None or len(self.TG_BOT_TOKEN) == 0:
            raise error.Error('NO_TG_BOT_TOKEN')
        
        if not re.search("^[0-9]{8,10}:[a-zA-Z0-9_-]{35}$", self.TG_BOT_TOKEN):
            raise error.Error('INVALID_TG_BOT_TOKEN')
        
    def __validate_web_app_port(self):
        if self.WEB_APP_PORT is None or len(self.WEB_APP_PORT) == 0:
            raise error.Error('NO_WEB_APP_PORT')
        
        if not self.WEB_APP_PORT.isdigit():
            raise error.Error('INVALID_WEB_APP_PORT')
        
        if int(self.WEB_APP_PORT) > 65535:
            raise error.Error('INVALID_WEB_APP_PORT')
        
        if int(self.WEB_APP_PORT) < 1:
            raise error.Error('INVALID_WEB_APP_PORT')