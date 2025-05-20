from setuptools import find_packages,setup
from typing import List

HPYEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the requirements
    
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HPYEN_E_DOT in requirements:
            requirements.remove(HPYEN_E_DOT)

    return requirements



setup(
    name='project1',
    version='0.0.1',
    author='D yellesh',
    author_email='yelleshdeshmukh26@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'))