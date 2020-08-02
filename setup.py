"""
For references of this file, see
    * https://github.com/pypa/sampleproject
    * https://packaging.python.org/en/latest/distributing.html
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file.
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="iutils",
    version="0.0.9",
    description="""A collection of my utility modules""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bqbn/iutils",
    author="bqbn",
    author_email="bqbn@openken.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
    ],
    keywords="devops utility utils",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    python_requires=">=3, <4",
    install_requires=[
        "awscli==1.18.102",
        "boto3==1.14.25",
        "botocore==1.17.25",
        "click==7.1.2",
        "colorama==0.4.3; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "docutils==0.15.2; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "jmespath==0.10.0",
        "pyasn1==0.4.8",
        "python-dateutil==2.8.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "pyyaml==5.3.1",
        "rsa==4.5; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4' and python_version < '4'",
        "s3transfer==0.3.3",
        "six==1.15.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "urllib3==1.25.9; python_version != '3.4'",
    ],
    # Additional groups of dependencies. They can be install by using
    # the "extras" syntax, for example:
    #
    #   $ pip install <module-name>[dev]
    extras_require={
        "dev": [
            "appdirs==1.4.4",
            "attrs==19.3.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "black==19.10b0; python_version >= '3.6'",
            "bleach==3.1.5; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "cached-property==1.5.1",
            "cerberus==1.3.2",
            "certifi==2020.6.20",
            "chardet==3.0.4",
            "click==7.1.2",
            "colorama==0.4.3; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "distlib==0.3.1",
            "docutils==0.15.2; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "idna==2.10; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "importlib-metadata==1.7.0; python_version < '3.8'",
            "keyring==21.2.1; python_version >= '3.6'",
            "orderedmultidict==1.0.1",
            "packaging==20.4; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "pathspec==0.8.0",
            "pep517==0.8.2",
            "pip-shims==0.5.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "pipenv-setup==3.1.1",
            "pipfile==0.0.2",
            "pkginfo==1.5.0.1",
            "plette[validation]==0.2.3; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "pygments==2.6.1; python_version >= '3.5'",
            "pyparsing==2.4.7; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "python-dateutil==2.8.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "readme-renderer==26.0",
            "regex==2020.7.14",
            "requests==2.24.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "requests-toolbelt==0.9.1",
            "requirementslib==1.5.12; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "rfc3986==1.4.0",
            "six==1.15.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "toml==0.10.1",
            "tomlkit==0.6.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "tqdm==4.48.0; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "twine==3.2.0",
            "typed-ast==1.4.1",
            "urllib3==1.25.9; python_version != '3.4'",
            "vistir==0.5.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "webencodings==0.5.1",
            "wheel==0.34.2",
            "zipp==3.1.0; python_version < '3.8'",
        ],
        "test": [],
    },
    project_urls={
        "Bug Reports": "https://github.com/bqbn/iutils/issues",
        "Source": "https://github.com/bqbn/iutils",
    },
    # Needed by the pipenv-setup tool.
    dependency_links=[],
    entry_points="""
        [console_scripts]
        qaws=qaws.qaws:cli
    """,
)
