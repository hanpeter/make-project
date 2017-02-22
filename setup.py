# -*- coding: utf-8 -*-

from __future__ import absolute_import
from setuptools import setup
from make_project import Application


# We use the version to construct the DOWNLOAD_URL.
VERSION = Application.VERSION

# URL to the repository on Github.
REPO_URL = 'https://github.com/hanpeter/make-project'

# Github will generate a tarball as long as you tag your releases, so don't
# forget to tag!
DOWNLOAD_URL = ''.join((REPO_URL, '/tarball/', VERSION))


setup(
    name='make-project',
    version=VERSION,
    author='@hanpeter',
    description='CLI that returns a list of users in a GitHub organization',
    url=REPO_URL,
    download_url=DOWNLOAD_URL,
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    py_modules=['make_project'],
    install_requires=[
        'click',
        'simplejson'
    ],
    entry_points={
        'console_scripts': [
            'make-project=make_project:main',
        ],
    },
)
