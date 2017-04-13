#!/usr/bin/env python

from setuptools import setup

setup(
	name='asymmetry',
	version='0.1',
	packages=['asymmetry'],
	setup_requires=['numpy'],
	install_requires=['numpy', 'nibabel', 'pandas'],
	author='Jersey Deng',
	author_email='jersey.deng@ucsf.edu',
	description='Collection of functions and scripts used in asymmetry project'
)
