from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyapt',
    version='0.1.dev0',
    description='Python Awesome Parallel Toolbox',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/willowsierra/PyAPT',  # Optional
    packages=find_packages(),
)
