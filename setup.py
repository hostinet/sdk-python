#!/usr/bin/env python3
import codecs
import os
import re
from setuptools import setup, find_packages

META_PATH = os.path.join("hostinet", "__version__.py")
HERE = os.path.abspath(os.path.dirname(__file__))
PACKAGES = find_packages()
KEYWORDS = ["hostinet", "sdk", "developers"]
CLASSIFIERS = [
    "Programming Language :: Python",
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
INSTALL_REQUIRES = ['requests']


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    author="Hostinet, SL.",
    author_email="desarrollo@hostinet.com",
    description="Hostinet - Software Development Kit for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=find_meta("license"),
    name="sdk-python",
    url="https://github.com/hostinet/sdk-python",
    version=find_meta("version"),
    classifiers=CLASSIFIERS,
    packages=PACKAGES,
    install_requires=INSTALL_REQUIRES,
    entry_points={}
)
