import sys

from .clioptions import CLIOptions


def main():
    options = CLIOptions(sys.argv[1:])
