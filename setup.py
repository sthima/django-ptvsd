import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ptvsd',
    version='0.0.1',
    description='A Wrapper to Visual Studio remote debugging server for python',
    long_description=README,
    url='https://github.com/sthima/django-ptvsd',
    author='Daniel Beckert',
    author_email='daniel@sthima.com',
    packages=find_packages(),
    license='MIT',
    install_requires=[
        'ptvsd==3.0.0',
    ]
)
