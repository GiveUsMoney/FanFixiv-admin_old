from os import path
import sys


def imp():
    sys.path.append(
        path.dirname(path.abspath(path.dirname(path.abspath(path.dirname(__file__)))))
    )
