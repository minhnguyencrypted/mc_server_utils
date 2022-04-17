import argparse

parser = argparse.ArgumentParser(prog='logparser', description='Minecraft Log parser')
parser.add_argument('file', help='Log file(s) to parse', nargs='*')
parser.add_argument('-d', '--dir', help='discover and parse all log files in a directory')
args = vars(parser.parse_args())
