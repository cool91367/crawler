# -*- coding: utf-8 -*-
import os
import sys
from setuptools import find_packages, setup, Command


def read(fname):
    """Utility function to read the README file into the long_description."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


version_file = "version.py"
with open(version_file) as fp:
    exec(fp.read())

setup(
    name="eyesmediapydb",
    version=__version__,
    author="eyesmedia",
    author_email="developer@eyesmedia.tw",
    description="eyesmedia database common library",
    license="Copyright eyesmedia",
    py_modules=['eyesmediapydb'],
    # zip_safe=False,
    platforms='ubuntu, MacOS, centos',
    install_requires=[
        "pymongo==3.7.2",
        "PyMySQL==0.9.2",
        "pytz>=2018.7",
        "six>=1.11.0"
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6.3',
    ],
    packages=find_packages(exclude=["test"]),
    include_package_data=True
)
