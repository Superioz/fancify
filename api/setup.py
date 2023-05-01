from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="fancify-api",
    version="0.1.0",
    description="API backend for the Fancify application",
    long_description=long_description,
    install_requires=[
        "flask==2.3.2",
        "flask_limiter==1.2.1",
        "requests==2.23.0",
        "flask-cors==3.0.10"
    ],
)
