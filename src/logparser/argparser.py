import argparse

parser = argparse.ArgumentParser(description='Minecraft Log parser')
parser.add_argument('file', help='Log file(s) to parse', nargs='*')
parser.add_argument('-d', '--dir', help='discover and parse all log files in a directory (WIP)')
args = vars(parser.parse_args())
