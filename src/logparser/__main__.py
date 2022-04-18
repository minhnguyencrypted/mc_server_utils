import sys
import glob
from colorama import init, Fore, Style
from . import logparser
from . import argparser as ap


def print_file_exception(exception, filename, ignore_errors):
    if not ignore_errors:
        if isinstance(exception, FileNotFoundError):
            print(Style.BRIGHT + Fore.RED + '[ERROR] ' + Style.RESET_ALL + filename + Style.BRIGHT + 'File not found')
        elif isinstance(exception, PermissionError):
            print(Style.BRIGHT + Fore.RED + '[ERROR] ' + Style.RESET_ALL + filename + ': ' + Style.BRIGHT + 'Permission denied')
        else:
            print(Style.BRIGHT + Fore.RED + '[ERROR] ' + Style.RESET_ALL + filename + ': ' + Style.BRIGHT + str(exception))


def print_players_list(players, only_found, file):
    if players:
        print(f'"{file}": ' + Style.BRIGHT + Fore.RED + 'Found un-whitelisted player(s)')
        for p in players:
            print('    Player: ' + Style.BRIGHT + Fore.MAGENTA + p['name'])
            print('        UUID: ' + p['id'])
            print('        IP and Port: ' + Fore.YELLOW + p['ip_port'])
            print('        Time: ' + p['time'])
        print(Style.BRIGHT + Fore.RED + 'Total: ' + str(len(players)) + Style.RESET_ALL + ' (' + file + ')')
    elif not only_found:
        print(f'"{file}": ' + Style.BRIGHT + Fore.GREEN + 'No un-whitelisted players found')


def print_summary(summary):
    s_total = f'{summary["total"]} file(s) searched'
    s_found = ((Style.BRIGHT + Fore.RED) if summary['found'] else Fore.GREEN) + f'{summary["found"]} file(s) found players'
    s_player = ((Style.BRIGHT + Fore.RED) if summary['player'] else Fore.GREEN) + f'{summary["player"]} player(s) found'
    s_error = (Fore.YELLOW if summary['error'] else '') + f'{summary["error"]} error(s)'
    print('SUMMARY: ', s_total, ' | ', s_found, ' | ', s_player, ' | ', s_error)


def parse_files(files):
    summary = dict(
        total=len(files),
        found=0,
        player=0,
        error=0
    )
    for f in files:
        try:
            found = logparser.parse(f)
            summary['player'] += len(found)
            summary['found'] += 1 if len(found) != 0 else 0
            print_players_list(found, ap.args['only_found'], f)
        except Exception as e:
            print_file_exception(e, f, ap.args['ignore_errors'])
            summary['error'] += 1
    return summary


if __name__ == "__main__":
    init(autoreset=True)
    if len(sys.argv) == 1:
        ap.parser.print_help()
        sys.exit()

    if ap.args['dir'] is not None:
        # Discover all *.log.gz files in the directory
        discovered = sorted(glob.glob(ap.args['dir'] + '/*.log.gz'))
        if len(discovered) != 0:
            print(Style.BRIGHT + f'Discovered {len(discovered)} log file(s) in "{ap.args["dir"]}"')
            smry = parse_files(discovered)
            print_summary(smry)
            sys.exit()
        else:
            print(f'No log files found in {ap.args["dir"]}')
            sys.exit()

    if len(ap.args['file']) != 0:
        smry = parse_files(ap.args['file'])
        print_summary(smry)
        sys.exit()
