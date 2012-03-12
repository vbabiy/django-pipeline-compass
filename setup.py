# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

description = """
django-pipeline compiler for scss and with compass. Does not require the ruby gem.
"""

setup(
    name='django-pipeline-compass',
    version='0.1.0',
    description=description,
    long_description=description,
    author='Vitaly',
    author_email='vbabiy86@gmail.com',
    url='https://github.com/vbabiy/django-pipeline-compass',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['pyScss'],
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)
