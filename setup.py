from setuptools import find_packages, setup
from typing import List

HED='-e .'

def get_requires(filename:str)->List[str]:
    '''
        this function returns a list of requirements for this project
    '''
    req = []
    with open(filename) as f:
        req=f.readlines()
        req = [r.replace("\n", "") for r in req]
        if HED in req:
            req.remove(HED)

    return req


setup(
    name = 'Resume_Mentor',
    version = '1.0.0',
    packages=find_packages(),
    install_requires=get_requires('requirements.txt'),
       
)