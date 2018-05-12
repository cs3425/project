#!/usr/bin/env python

from setuptools import setup, find_packages


# parse version string from the __init__ file
with open("project/__init__.py", "r") as initfile:
    lines = initfile.readlines()
    for line in lines:
        if "__version__" in line:
            # get version line and strip white space and quotations
            version = line.strip().split()[-1].strip("'").strip('"')


# build command
setup(
    name="project",
    version=version,
    packages=find_packages(),
    author="Cecilia Sena",
    author_email="cs3425@columbia.edu",
    license="GPLv3",
    description="A package for displaying PAR and CHLA data",
    classifiers=["Programming Language :: Python :: 3"],
)
