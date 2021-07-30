##Student of Mister Kaff SIR

import argparse
import os


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


parser = argparse.ArgumentParser(description='broccoli archive', epilog="see you next time")
parser.add_argument('--a', '--archive', type=dir_path, help='used to scan all directrories')

args = parser.parse_args()
