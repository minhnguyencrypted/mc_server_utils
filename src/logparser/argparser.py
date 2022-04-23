import argparse

parser = argparse.ArgumentParser(prog='logparser',
                                 description='Minecraft Log parser',
                                 epilog='DATE format: DD/MM/YYYY',
                                 exit_on_error=False)

parser.add_argument('file', help='Log file(s) to parse', nargs='*')
parser.add_argument('--only-found', help='only display files that players were found in', action='store_true')
parser.add_argument('--ignore-errors', help='do not display error messages', action='store_true')

args = vars(parser.parse_args())
