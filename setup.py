from setuptools import setup, find_packages
import os

def parse_requirements(filename):
    """ Load requirements from a pip requirements file. """
    with open(filename, "r") as file:
        return file.read().splitlines()

requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
install_requires = parse_requirements(requirements_path) if os.path.exists(requirements_path) else []

setup(
    name="aicovergen",
    version="1.0.0",
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "aicovergen=aicovergen.main:main",
        ],
    },
)