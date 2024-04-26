from setuptools import setup

def requires_mod():
    raw = open("dev-requirements/python.txt", "r").read()
    return raw.splitlines()

def get_version():
    raw = open("backpipe/__init__.py", "r").read()
    for ln in raw.splitlines():
        if ln.startswith("__version__ = "):
            return ln[15:-1]

setup(
    name="backpipe",
    version=get_version(),
    description="A backend HTTP framework for Python.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Simoso68",
    maintainer="Simoso68",
    license="GNU GPL v3",
    install_requires=requires_mod(),
    include_package_data=True,
    packages=["backpipe", 
        "backpipe.presets",
        "backpipe.tools",
        "backpipe.tools.base64",
        "backpipe.tools.file",
        "backpipe.tools.hash",
        "backpipe.tools.html",
        "backpipe.tools.json",
        ],
    keywords=[
        "framework",
        "http",
        "web",  
        "api", 
        "server",
    ],
    url="https://github.com/Simoso68/backpipe",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Environment :: Console",
    ],
    entry_points={
        "console_scripts": ["backpipe = backpipe.__main__:main"]
    }
)