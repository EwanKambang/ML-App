import sys
import logging

def error_message_details(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"\033[91mError occured in python \n\tscript name [\033[93m{file_name}\033[91m]\
                    \n\t\033[91mline number [\033[93m{exc_tb.tb_lineno}\033[91m]\
                    \n\terror message [\033[93m{str(error)}\033[91m]\033[0m"

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)

    def __str__(self):
        return f"\033[91m\033[1m\n[Custom Exception]\033[0m {self.error_message}"

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e: 
        logging.info("Divide by zero")
        raise CustomException(e, sys)
