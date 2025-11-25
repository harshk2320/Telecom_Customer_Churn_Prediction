from setuptools import find_packages, setup

setup(
    
    # This function basically defines your package 
    
    
    name= "src",  # Name of the package
    version= "0.0.1",   # Version number of the package
    author= "Harsh Kumar",  # Author/ Creator of the package 
    author_email= "harshkumarsingh2320@gmail.com",  # Email ID of the author which will be showed in documentation
    packages= find_packages()   # This will find all the modules in the src folder and will include in the package
)