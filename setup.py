"""
For references of this file, see
    * https://github.com/pypa/sampleproject
    * https://packaging.python.org/en/latest/
"""

from setuptools import setup, find_packages


setup(
    # packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=[
        "awscli~=2.17",
        "boto3~=1.21",
        "click~=8.1",
        "jmespath~=1.0",
        "requests~=2.27",
    ],
    # Additional groups of dependencies. They can be install by using
    # the "extras" syntax, for example:
    #
    #   $ pip install <module-name>[dev]
    extras_require={
        "dev": [
            "build~=1.2",
            "pipenv-setup~=3.2",
            "twine~=5.1",
            "wheel~=0.34",
        ],
        "test": [],
    },
    # Needed by the pipenv-setup tool.
    dependency_links=[],
    entry_points={
        "console_scripts": [
            "pcolrm=pcolrm.pcolrm:main",
            "qaws=qaws.qaws:cli",
            "webhook=webhook.webhook:main",
        ],
    },
)
