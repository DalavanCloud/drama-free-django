#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name="drama-free-django",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'no-drama=no_drama.__main__:main'
        ]
    },
    install_requires=[
        'wheel>=0.29.0,<0.32',
        'pip>=8.1.1,<=9.0.3',
        'setuptools>=20.2.2',
    ],
    tests_require=[
        'mock',
    ],
    test_suite='tests',
)
