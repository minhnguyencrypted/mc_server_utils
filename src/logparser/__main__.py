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


def print_players_list(players):
    for p in players:
        print(f"""    Player: {p['name']}
        UUID: {p['id']}
        IP and Port: {p['ip_port']}
        Time: {p['time']}""")


if __name__ == "__main__":
    # print(ap.args)
    if len(sys.argv) == 1:
        ap.parser.print_help()
        sys.exit()

    if len(ap.args['file']) != 0:
        try:
            for file in ap.args['file']:
                found = logparser.parse(file)
                if found:
                    print(f'[{file}]: Found un-whitelisted player(s)')
                    print_players_list(found)
                    print(f'Total: {len(found)} ({file})')
                else:
                    print(f'[{file}]: No un-whitelisted players found')
            sys.exit()
        except Exception as e:
            file_exception_handler(e, ap.args['file'])
            sys.exit(2)

    # if ap.args['dir'] is not None:
    #     # Discover all *.log.gz files in the directory
    #     for file in glob.glob(ap.args['dir'] + '/*.log.gz'):
    #         print(file)
