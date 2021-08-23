from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="fancify-dictionary",
    version="0.1.0",
    description="Dictionary service for the Fancify application",
    long_description=long_description,
    install_requires=["flask==1.1.2", "flask_limiter==1.2.1", "pyyaml==5.4.1"],
)
