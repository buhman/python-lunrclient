#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='python-lunrclient',
    version='1.1.0',
    description='LunrClient',
    license='Apache License (2.0)',
    author='Rackspace US, Inc.',
    packages=find_packages(exclude=['test']),
    test_suite='nose.collector',
    install_requires=['requests', 'prettytable>=0.7'],
    entry_points={
        'console_scripts': ['storage = lunrclient.storage_shell:main',
                            'lunr = lunrclient.lunr_shell:main']
    }
)
