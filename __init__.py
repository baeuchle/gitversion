#!/usr/bin/python3

from pathlib import Path
from subprocess import Popen, PIPE

"""Module for simple git information tasks"""

class Git:
    def __init__(self, cwd=Path(__file__).parents[1]):
        self.cwd = cwd
        self.popen_kwargs = {
            'stdout': PIPE,
            'cwd': self.cwd,
            'universal_newlines': True
            }

    def _gitlines(self, *git_args):
        result = []
        cmd_args = ['git']
        for arg in git_args:
            cmd_args.append(arg)
        with Popen(cmd_args, **self.popen_kwargs) as proc:
            for line in proc.stdout:
                result.append(line)
        return result

    def _gitoutput(self, *git_args):
        result = ""
        for line in self._gitlines(*git_args):
            result += line
        return result.strip()

    def describe(self):
        return self._gitoutput('describe', '--always')

    def hash(self, *args):
        return self._gitoutput('log', '--pretty=%H', '-1', *args)

    def changelog(self, old_version=None):
        result = ""
        if old_version == None or old_version.strip() == '':
            old_version = self._gitlines('log', '--pretty=%H')[-1].strip()
        for line in self._gitlines('log', '{}..HEAD'.format(old_version)):
            trimmed = line.strip()
            if len(trimmed) <= len('CHANGELOG'):
                continue
            if trimmed[0:9] != 'CHANGELOG':
                continue
            result += '•' + trimmed[9:] + '\n'
        return result
