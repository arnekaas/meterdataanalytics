print "test has not been tested"

import os
import sys

from setuptools import setup, find_packages

VERSION = '0.1'

install_reqs = ['pyserial']

setup(name='meterdatanalytics', 
    version=VERSION,
    description='Disaggregation of smart meter data',
    author='Arne Kaas',
    author_email='info@arnekaas.nl',
    url='https://github.com/arnekaas/meterdataanalytics',
    license='GPL',
    packages=find_packages(),
    install_requires=install_reqs,
    scripts=['test.py'],
)
