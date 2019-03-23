#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from import_csv import __author__, __version__, __license__
 
setup(
        name             = 'import_csv tools',
        version          = __version__,
        description      = 'import csv file with header and create database, table',
        license          = __license__,
        author           = __author__,
        author_email     = 'YuHori.Main@gmail.com',
        url              = 'https://github.com/YuHori/import_csv/sql.git',
        keywords         = 'import csv',
        packages         = find_packages(),
        install_requires = [],
)
