#!/usr/bin/python3

from pathlib import Path
from subprocess import Popen, PIPE

"""Module for simple git information tasks"""

def describe():
    """
        Return a description of the current git version of one directory up
    """
    result = ""
    with Popen(['git', 'describe', '--always'],
        stdout=PIPE,
        cwd=Path(__file__).parents[1],
        universal_newlines=True
        ) as proc:
        for line in proc.stdout:
            result += line
    return result.strip()
