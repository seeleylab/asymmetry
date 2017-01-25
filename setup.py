#!/usr/bin/env python

from setuptools import setup
import os

setup(
	name='asymmetry',
	version='0.1',
	packages=['asymmetry'],
	scripts=[os.path.join('scripts', 'fslxmean')],
	install_requires=[],
	author='Jersey Deng',
	author_email='jersey.deng@ucsf.edu',
	description='Collection of scripts used in asymmetry project'
)
