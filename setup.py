from distutils.core import setup
from setuptools import find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def find_packages_in(where, **kwargs):
    return [where] + ['%s.%s' % (where, package) for package in find_packages(where=where, **kwargs)]

setup(
    name = 'django-currency',
    version = '0.2.0',
    author = 'Allan Lei',
    author_email = 'allanlei@helveticode.com',
    description = 'Tools to display currencies',
#    long_description=open('README.md').read(),
    license=open('LICENSE.txt').read(),
    keywords = 'django currency',
    url = 'https://github.com/allanlei/django-currency',
    packages=find_packages_in('currencies'),
)
