from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """Read requirements.txt and return a list of packages, ignoring -e ."""
    requirements = []
    with open(file_path, 'r') as file_object:
        # read all lines, strip newline and whitespace
        requirements = [line.strip() for line in file_object.readlines()]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    author='Yugal',
    author_email='yugalsoni2005@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
