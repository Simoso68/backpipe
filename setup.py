from setuptools import setup
from backpipe import __version__

def requires_mod():
    raw = open("dev-requirements/python.txt", "r").read()
    return raw.splitlines()

setup(
    name="backpipe",
    version=__version__,
    description="A backend HTTP framework for Python.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Simoso68",
    maintainer="Simoso68",
    license="GNU GPL v3",
    install_requires=requires_mod(),
    packages=["backpipe"],
    keywords=[
        "framework",
        "http",
        "web",  
        "api", 
        "server"
    ],
    url="https://github.com/Simoso68/backpipe",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Natural Language :: English"
    ]
)