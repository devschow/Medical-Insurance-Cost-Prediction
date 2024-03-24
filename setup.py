from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements

setup(
    name='Medical Insurance Cost Prediction',
    version='0.0.1',
    author='Devarshi',
    author_email='devarshichoudhury.dc@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)