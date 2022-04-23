import sys
import os
import glob
from colorama import init, Fore, Style
from . import logparser
from . import argparser as ap


def print_file_exception(exception, filename, ignore_errors):
    msg = f'{Style.BRIGHT}{Fore.RED}[ERROR] {Style.RESET_ALL}"{filename}":'
    if not ignore_errors:
        if isinstance(exception, FileNotFoundError):
            print(msg + f'{Style.BRIGHT} File not found')
        elif isinstance(exception, PermissionError):
            print(msg + f'{Style.BRIGHT} Permission denied')
        else:
            print(msg + f'{Style.BRIGHT} {str(exception)}')


def print_players_list(players, only_found, file):
    if players:
        print(f'"{file}": ' + Style.BRIGHT + Fore.RED + 'Found un-whitelisted player(s)')
        for p in players:
            print(f'    Player: {Style.BRIGHT + Fore.MAGENTA}{p["name"]}')
            print(f'        UUID: {p["id"]}')
            print(f'        IP and Port: {Fore.YELLOW}{p["ip_port"]}')
            print(f'        Time: {p["time"]}')
        print(f'{Style.BRIGHT + Fore.RED}Total: {str(len(players))}{Style.RESET_ALL}')
    elif not only_found:
        print(f'"{file}": {Style.BRIGHT + Fore.GREEN}No un-whitelisted players found{Style.RESET_ALL}')


def print_summary(summary):
    s_total = f'{summary["total"]} file(s) searched'
    s_found = ((Style.BRIGHT + Fore.RED) if summary['found'] else Fore.GREEN) + f'{summary["found"]} file(s) found players'
    s_player = ((Style.BRIGHT + Fore.RED) if summary['player'] else Fore.GREEN) + f'{summary["player"]} player(s) found'
    s_error = (Fore.YELLOW if summary['error'] else '') + f'{summary["error"]} error(s)'
    print('SUMMARY: ', s_total, s_found, s_player, s_error, sep=' | ')


def parse_files(files):
    summary = init_summary(total=len(files))
    for f in files:
        basef = os.path.basename(f)
        try:
            found = logparser.parse(f)
            summary['player'] += len(found)
            summary['found'] += 1 if len(found) != 0 else 0
            print_players_list(found, ap.args['only_found'], basef)
        except Exception as e:
            print_file_exception(e, basef, ap.args['ignore_errors'])
            summary['error'] += 1
    return summary


def update_summary(sum1, sum2):
    return dict(
        total=sum2['total'] + sum1['total'],
        found=sum2['found'] + sum1['found'],
        player=sum2['player'] + sum1['player'],
        error=sum2['error'] + sum1['error']
    )


def init_summary(**kwargs):
    return dict(
        total=kwargs.get('total', 0),
        found=kwargs.get('found', 0),
        player=kwargs.get('player', 0),
        error=kwargs.get('error', 0)
    )


if __name__ == "__main__":
    init(autoreset=True)
    if len(sys.argv) == 1:
        ap.parser.print_help()
        sys.exit()

    if len(ap.args['file']) != 0:
        summary = init_summary()
        for file in ap.args['file']:
            if os.path.isdir(file):
                files = glob.glob(file + '*.log.gz') if file.endswith('/') else glob.glob(file + '/*.log.gz')
                print(f'"{file}": discovered {len(files)} file(s)')
                fsummary = parse_files(files)
                summary = update_summary(fsummary, summary)
            else:
                fsummary = parse_files([file])
                summary = update_summary(fsummary, summary)
        print_summary(summary)
