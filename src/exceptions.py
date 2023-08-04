import sys


def error_msg_details(error, error_details: sys):
    # Returns on the error information, like on which file on which line the error occurred
    exc = error_details.exc_info()[2]
    err_msg = "\nError occured in python script [{0}] \nline Number: [{1}]\nThe error message: [{2}]".format(
        exc.tb_frame.f_code.co_filename,
        exc.tb_lineno,
        str(error)
    )
    return err_msg


class CustomException(Exception):
    def __init__(self, error_msg, error_details: sys):
        super().__init__(error_msg)
        self.error_msg = error_msg_details(error_msg, error_details=error_details)
 
    def __str__(self):
        return self.error_msg


# Just for checking purpose
if __name__ == '__main__':
    try: 
        a = 1/0
    except Exception as e:
        raise CustomException(e, sys)