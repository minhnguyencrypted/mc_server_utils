import sys
import glob
from . import logparser
from . import argparser as ap


def file_exception_handler(exception, filename):
    if isinstance(exception, FileNotFoundError):
        print(f'[ERROR] [{filename}]: File not found')
    elif isinstance(exception, PermissionError):
        print(f'[ERROR] [{filename}]: Permission denied')
    else:
        print(f'[ERROR] [{filename}]: {e}')


def print_players_list(players):
    if players:
        print(f'[{file}]: Found un-whitelisted player(s)')
        for p in players:
            print(f"""    Player: {p['name']}
        UUID: {p['id']}
        IP and Port: {p['ip_port']}
        Time: {p['time']}""")
        print(f'Total: {len(found)} ({file})')
    else:
        print(f'[{file}]: No un-whitelisted players found')


if __name__ == "__main__":
    print(ap.args)
    if len(sys.argv) == 1:
        ap.parser.print_help()
        sys.exit()

    if ap.args['dir'] is not None:
        # Discover all *.log.gz files in the directory
        discovered = glob.glob(ap.args['dir'] + '/*.log.gz')
        if len(discovered) != 0:
            print(f'Discovered {len(discovered)} log file(s) in "{ap.args["dir"]}"')
            total_players = 0
            total_error = 0
            total_found = 0
            for file in discovered:
                try:
                    found = logparser.parse(file)
                    total_players += len(found)
                    total_found += 1 if len(found) != 0 else 0
                    print_players_list(found)
                except Exception as e:
                    file_exception_handler(e, file)
                    total_error += 1
            print(f'SUMMARY: {len(discovered)} file(s) discovered, {total_found} file(s) found players, \
{total_players} player(s) found, {total_error} error(s)')
            sys.exit()
        else:
            print(f'No log files found in {ap.args["dir"]}')
            sys.exit(2)

    if len(ap.args['file']) != 0:
        for file in ap.args['file']:
            try:
                found = logparser.parse(file)
                print_players_list(found)
                sys.exit()
            except Exception as e:
                file_exception_handler(e, file)
                sys.exit(2)
