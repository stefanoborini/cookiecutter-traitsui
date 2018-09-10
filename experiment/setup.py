import os

from setuptools import setup, find_packages

# Setup version
VERSION = '0.1.0.dev0'


# Read description
with open('README.rst', 'r') as readme:
    README_TEXT = readme.read()


def write_version_py():
    filename = os.path.join(
        os.path.dirname(__file__),
        '{{cookiecutter.project_name}}',
        'version.py')
    ver = "__version__ = '{}'\n"
    with open(filename, 'w') as fh:
        fh.write(ver.format(VERSION))


write_version_py()

# main setup configuration class
setup(
    name='{{cookiecutter.project_name}}',
    version=VERSION,
    author='{{cookiecutter.author}}',
    description='{{cookiecutter.description}}',
    long_description=README_TEXT,
    install_requires=[
        'traitsui~=5.1',
    ],
    packages=find_packages(),
    entry_points={
        'gui_scripts': [
            ('{{cookiecutter.project_name}} =
              {{cookiecutter.project_name}}.run:main')
        ]
    },
)
