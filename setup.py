'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages, setup
from typing import List

#HYPEN_E_DOT = "-e ."

def get_requirements() -> List[str]:
    """
    Thiss function will return list of requirements
    
    """
    requirement_lst: List[str] = []

    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()

                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name = "Network security",
    version = "0.01",
    author = " Abhinav sinha ",
    author_email = "abhinavsinha0093@gmail.com",
    packages=find_packages(include=["networksecurity", "networksecurity.*"]),
    install_requires =  get_requirements()
)