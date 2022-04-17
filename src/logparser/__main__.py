import sys
from . import logparser
from . import argparser as ap


def file_exception_handler(exception, filename):
    if isinstance(exception, FileNotFoundError):
        print(f'{filename}: File not found')
    elif isinstance(exception, PermissionError):
        print(f'{filename}: Permission denied')
    else:
        print(f'{filename}: {e}')


if __name__ == "__main__":
    if len(sys.argv) == 1:
        ap.parser.print_help()
        sys.exit()
    if ap.args['file'] is not None:
        try:
            for file in ap.args['file']:
                found = logparser.parse(file)
                if found:
                    print(f'{file}: Found {len(found)} un-whitelisted player(s)')
                    for player in found:
                        print(f"""Player: {player['name']}
    UUID: {player['id']}
    IP and Port: {player['ip_port']}
    Time: {player['time']}""")
                else:
                    print(f'{file}: No un-whitelisted players found')
            sys.exit()
        except Exception as e:
            file_exception_handler(e, ap.args['file'])
            sys.exit(2)
