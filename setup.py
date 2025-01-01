from setuptools import setup, find_packages

setup(
    name="httpconverter",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4",
        "autopep8",
    ],
    entry_points={
        "console_scripts": [
            "httpconverter=httpconverter.cli:main",
        ],
    },
    author="Netzha Belmonte",
    description="A tool to convert files with HTTP messages into requests functions",
    python_requires=">=3.9",
)
