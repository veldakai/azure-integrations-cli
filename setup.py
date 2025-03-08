from setuptools import setup, find_packages
from azureintegrationscli import __version__

setup(
    name="azure-integrations-cli",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "azints=azureintegrationscli.__main__:cli",
        ],
    },
    author="Veldak",
    author_email="veldak.video@github.com",
    description="A CLI tool to manage Azure Integration Services code",
    url="https://github.com/veldakai/azure-integrations-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
