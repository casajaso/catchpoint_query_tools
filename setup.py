#!/usr/bin/env python

from setuptools import setup


# We use the version to construct the DOWNLOAD_URL.
VERSION = '0.1.1'

# URL to the repository on Github.
REPO_URL = 'WILL_ADD_LATER'

# Github will generate a tarball as long as you tag your releases, so don't
# forget to tag!
DOWNLOAD_URL = ''.join((REPO_URL, '/tarball/release/', VERSION))

setup(
    name='catchpoint_query_tools',
    version=VERSION,
    author='Jason Casas',
    author_email='jason.c.casas@gmail.com',
    url=REPO_URL,
    download_url=DOWNLOAD_URL,
    license='Getty Images - INTERNAL USE',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        "datetime>=4.1",
        "pytz",
        "requests",
        "argparse",
        "numpy"
    ],
    description="Python module for query Catchpoint REST API",
#    dependency_links=['https://github.com/jasonarewhy/catchpoint-api-python.git#egg=catchpoint-api-python'],
    test_suite='nose.collector',
    tests_require=['nose'],
    scripts=['bin/get_testids.py'],
)