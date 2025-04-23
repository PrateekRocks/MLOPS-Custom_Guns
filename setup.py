from setuptools import setup,find_packages

with open("req.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="CUSTOM-GUN-DETECTION",
    version="0.1",
    author="PRATEEK",
    packages=find_packages(),
    install_requires = requirements,
)