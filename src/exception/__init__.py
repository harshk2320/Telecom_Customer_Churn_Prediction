"""
✅ Overall Purpose of This Code

This code does two main things:

1. Extract detailed error information

Such as:

Which file caused the error

Which line number

What the actual error message is

2. Create a custom exception class

Your custom class MyException makes sure every time an error occurs, it automatically generates a meaningful, readable, and full traceback-style error message.

This is VERY useful in big projects like MLOps or ML pipelines.
"""

## Libraries
import sys  # This module will give the exact traceback information
import logging    # This allows error message to be recorded inside logs(file or console)

def error_message_details(error: Exception, error_details: sys) -> str:
        """
        Extracts detailed error information including file name, line number and the error message.

        : parametre -> error: The exception/ error that occured.
        : parametre -> error_details: The sys module to access traceback details.
        : returns -> formatted string of error message.   
        """

        ## Getting traceback information
        _, _, exc_tb = error_details.exc_info()

        # Whenever error happens, python stores details about it. exc_info() returns three values:
            # 1. type of error (Ex ValueError)
            # 2. Error message (Ex: "invalid value")
            # 3. Traceback (where the error happened)

        # Here we ignore the first two and only use 3rd value i,e exc_tb.

        ## Getting the file name where the error happened.
        file_name = exc_tb.tb_frame.f_code.co_filename

            # exc_tb → tells us where the error happened

            # .tb_frame → inside which code frame?

            # .f_code → get info about that code

            # .co_filename → the file name

        ## Getting the line number of the error
        line_number = exc_tb.tb_lineno


        ## Create a detailed error message
        error_message = f"Error occured in python script: [{file_name}] at line number [{line_number}]: {str(error)}"

        ## Log the error for better tracking
        logging.error(error_message)

        ## Return the message
        return error_message


class MyException(Exception):   # Inheriting from python's default Exception class.
        """
        Custom exception class for handling errors in the telecom customer churn prediction application.
        """

        ## Constructor
        def __init__(self, error_message: str, error_details: sys):     # When this occurs, python will run this method
            
            # Call the base class constructor with the error message
            super().__init__(error_message)     # This sets the initial message
        
            # Format the detailed error message using the error_message_details() 
            self.error_message = error_message_details(error_message, error_details)

        def __str__(self) -> str:
               
               """
               Returns the string repsentation of the error message.
               """
               return self.error_message

               