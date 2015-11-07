#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pkg_resources
import subprocess

class Package(object):
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.license = None
        self.author = None
        self.homepage = None

    def get_package_information(self):
        try:
            pkgs = pkg_resources.require(self.name)
        except:
            return

        if len(pkgs) == 0:
            return

        pkg = pkgs[0]
        try:
            for line in pkg.get_metadata_lines('PKG-INFO'):
                try:
                    (k, v) = line.split(': ', 1)
                    if k == 'License':
                        self.license = v
                    elif k == 'Author':
                        self.author = v
                    elif k == 'Home-page':
                        self.homepage = v
                except ValueError as e:
                    pass

        except IOError as e:
            pass

    def write(self):
        self.get_package_information()

        # Print the information if it exists.
        if self.name:
            sys.stdout.write('# {}\n'.format(self.name))
        if self.license is not None:
            sys.stdout.write('# License: {}\n'.format(self.license))
        if self.homepage is not None:
            sys.stdout.write('# Homepage: {}\n'.format(self.homepage))
        if self.author is not None:
            sys.stdout.write('# Author: {}\n'.format(self.author))

        if self.name and self.version:
            sys.stdout.write('{0}=={1}\n\n'.format(self.name, self.version))


def get_packages():
    freeze = subprocess.check_output(['pip', 'freeze'])
    packages = []

    for package in freeze.split('\n'):
        splitted = package.split('==')

        # Don't include this package in the freeze.
        if len(splitted) > 0 and splitted[0] == 'pretty-freeze':
            continue

        if len(splitted) == 1:
            packages.append(Package(splitted[0], None))
        elif len(splitted) == 2:
            packages.append(Package(splitted[0], splitted[1]))

    return packages

def run():
    for package in get_packages():
        package.write()
