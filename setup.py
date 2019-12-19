#! /usr/bin/env python
#-*- coding: utf-8 -*-
 
#####################################################
# Copyright (c) 2019 Sogou, Inc. All Rights Reserved
#####################################################
# File:    setup.py
# Author:  root
# Date:    2019/12/18 21:26:53
# Brief:
#####################################################

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="myseg",
    version="0.0.1",
    author="roeexu",
    author_email="roeexu@sogou-inc.com",
    description="A segment tool modified from jieba.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/roeexu/myseg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)

# vim: set expandtab ts=4 sw=4 sts=4 tw=100
