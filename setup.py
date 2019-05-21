#!/usr/bin/env python
from setuptools import setup, find_packages

with open("requirements/prod", "r") as fh:
    requirements = fh.read().splitlines()

with open("requirements/dev", "r") as fh:
    dev_requirements = fh.read().splitlines()

with open("VERSION", "r") as fh:
    version = fh.read()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="alcali",
    version=version,
    author="Matt Melquiond",
    author_email="matt.LLVW@gmail.com",
    description="Alcali",
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/latenighttales/alcali.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Systems Administration",
    ],
    install_requires=requirements,
    extras_require={
        "dev": [req for req in dev_requirements if not req.startswith("-")]
    },
    entry_points={"console_scripts": ["alcali = alcali:manage"]},
    scripts=["alcali/__init__.py"],
)
