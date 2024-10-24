from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    
    '''
    this function will return a list of requirements 
    '''
    
    requirements=[]

    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirement]
    
    return requirements


setup(
name='MLProject',
version='0.0.1',
author='Santanu',
author_email='sanssarkar@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)