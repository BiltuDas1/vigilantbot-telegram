class Error(Exception):
    """
    Exception Class for any kind of Error encounter in the Telegram bot
    """
    
    __ERR_MSG_LIST = {
        0: "Something unexpected happened into the code, please contact the developer",
        1: "TG_BOT_TOKEN Environment have Invalid Bot Token, Please provide the correct token and try again",
        2: "TG_BOT_TOKEN Environment can't be empty",
        3: "PORT Environment can't be empty",
        4: "PORT Environment variable contains invalid port number, Please provide a correct port number and try again"
    }

    __ERR_CODE_LIST = {
        "UNEXPECTED_EXCEPTION": 0,
        "INVALID_TG_BOT_TOKEN": 1,
        "NO_TG_BOT_TOKEN": 2,
        "NO_WEB_APP_PORT": 3,
        "INVALID_WEB_APP_PORT": 4
    }

    def __init__(self, ERR_CODE: str, MSG=None):
        if type(ERR_CODE) == str:
            self.__ERR_CODE = int(self.__ERR_CODE_LIST[ERR_CODE])
        else:
            self.__ERR_CODE = int(0)

        if type(MSG) == str:
            self.__MSG = MSG
        else:
            self.__MSG = self.__ERR_MSG_LIST[self.__ERR_CODE]

    def __str__(self):
        return self.__MSG
    
    def ErrorCode(self):
        """
        Returns the Error Code (in int)
        """
        return self.__ERR_CODE
    