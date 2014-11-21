from setuptools import setup, find_packages


setup(
    name="fabric-virtualenv",
    version="0.2.1",
    author='Daniel Pope',
    author_email='ext-dan.pope@vertu.com',
    url='http://pypi.python.org/pypi/fabric-virtualenv/',
    description=(
        "Some additional functions for working with remote virtualenvs "
        "in Fabric."
    ),
    long_description=open('README').read(),
    packages=find_packages(),
    install_requires=[
        'Fabric'
    ]
)
