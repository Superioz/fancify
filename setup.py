from setuptools import setup, find_packages

# setup the modules for me
setup(
    name="api",
    version="1.0",
    packages=find_packages(),
    scripts=["api/idfancy.py"]
)
