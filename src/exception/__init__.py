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

