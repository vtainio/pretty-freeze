#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

def get_long_description():
    with open('README.rst', 'rb') as f:
        return f.read().decode('utf-8')

def setup_package():
    setup(
        name='pretty-freeze',
        description='Pip freeze that shows detailed descriptions of the packages.',
        long_description=get_long_description(),
        version='0.0.1',
        url='https://github.com/Wisheri/pretty-freeze',
        author='Ville Tainio',
        author_email='tainio.ville@gmail.com',
        license='MIT',
        keywords='freeze pip pretty information meta',
        packages=['pretty_freeze'],
        entry_points={
            'console_scripts': ['pretty-freeze = pretty_freeze.freeze:run']
        },
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
        ]
    )

if __name__ == '__main__':
    setup_package()
