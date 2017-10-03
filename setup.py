"""
writes setup.py in distutils to create a zip file
command to run this python setup.py sdist --format zip
"""
from distutils.core import setup

setup(
    name="Sample Flask Webapp",
    version='1.0',
    packages = ['Webapplication','Webapplication/Test','Webapplication/utilities'],
    data_files = ['circle.yml','README.md','Webapplication/static/css/*.css'],

    #metadata
    author='Ritesh Kumar',
    author_email='rithu.ritesh@gmail.com',
    description='A Simple Python Flask Webapp.',
    license='Public Domain',
)