from importlib.resources import Package
from setuptools import setup
from typing import List

#Declaring Variables for setup functions 
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Harish Seenivasan"
DESCRIPTION = "This is my first Project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description : This function is going to return list of requirement mention in requirement.txt file

    return This function is going to return a list which will contain name of libraries mentioned in the requirement.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name = PROJECT_NAME,
version  = VERSION,
author = AUTHOR,
description = DESCRIPTION,
packages = PACKAGES,
install_requires = get_requirements_list()

)

if __name__=='__main__':
    print(get_requirements_list())