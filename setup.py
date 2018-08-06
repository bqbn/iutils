"""
For references of this file, see

https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='iutils',
    version='0.0.1',
    description='''A collection of utility modules''',

    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/bqbn/iutils',
    author='bqbn',
    author_email='bqbn@openken.com',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
    ],

    keywords='utility utils devops',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
    ],

    # Additional groups of dependencies. They can be install by using
    # the "extras" syntax, for example:
    #
    #   $ pip install <module-name>[dev]
    extras_require={
        'dev': ['wheel', 'twine'],
        'test': [],
    },

    project_urls={
        'Bug Reports': 'https://github.com/bqbn/iutils/issues',
        'Source': 'https://github.com/bqbn/iutils',
    },
)

