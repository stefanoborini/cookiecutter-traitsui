from __future__ import print_function
import sys

from . import app


def _usage():
    print("Please specify the directory of the metadata info")
    sys.exit(1)


def main():
    try:
        directory = sys.argv[1]
    except IndexError:
        _usage()

    a = app.App(directory=directory)
    a.configure_traits()
