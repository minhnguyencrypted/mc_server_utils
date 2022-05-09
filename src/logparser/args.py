import argparse

parser = argparse.ArgumentParser(prog='logparser',
                                 description='Minecraft Log parser',
                                 epilog='DATE format: DD/MM/YYYY',
                                 exit_on_error=False)

parser.add_argument('file', help='Log file(s) to parse', nargs='*')
parser.add_argument('-t', '--date', help='parse specific date(s)', dest='dates', metavar='DATE', nargs='*')
parser.add_argument('-s', '--summary', help='print summary', action='store_true')
parser.add_argument('--ignore-errors', help='do not display error messages', action='store_true')

args = vars(parser.parse_args())
