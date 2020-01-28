#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="aiocached",
    version="0.3",
    description="Simple decorator to cache coroutine function results",
    long_description=open('README.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    platforms="all",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 5 - Production/Stable",
    ],
    license="Apache License, Version 2.0",
    author="Alexander Tikhonov",
    author_email="random.gauss@gmail.com",
    url='https://github.com/Fatal1ty/aiocached',
    packages=find_packages(exclude=("tests",)),
    python_requires=">=3.5",
)
