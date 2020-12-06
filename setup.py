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
    version="0.0.10",
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
    install_requires=["boto3>=1.14.33", "click>=7.1.2",],
    # Additional groups of dependencies. They can be install by using
    # the "extras" syntax, for example:
    #
    #   $ pip install <module-name>[dev]
    extras_require={"dev": ["twine>=3.2.0", "wheel>=0.34.2",], "test": [],},
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
