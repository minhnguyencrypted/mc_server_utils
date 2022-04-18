import sys
import glob
from colorama import init, Fore, Style
from . import logparser
from . import argparser as ap


def print_file_exception(exception, filename, ignore_errors):
    if not ignore_errors:
        if isinstance(exception, FileNotFoundError):
            print(Style.BRIGHT + Fore.RED + '[ERROR] ' + Style.RESET_ALL + filename + Style.BRIGHT + ': File not found')
        elif isinstance(exception, PermissionError):
            print(Style.BRIGHT + Fore.RED + '[ERROR] ' + Style.RESET_ALL + filename + ': ' + Style.BRIGHT + 'Permission denied')
        else:
            print(Style.BRIGHT + Fore.RED + '[ERROR] ' + Style.RESET_ALL + filename + ': ' + Style.BRIGHT + str(exception))


def print_players_list(players, only_found):
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
    s_total = f'{summary["total"]} file(s) found'
    s_found = ((Style.BRIGHT + Fore.RED) if summary['found'] else Fore.GREEN) + f'{summary["found"]} file(s) found players'
    s_player = ((Style.BRIGHT + Fore.RED) if summary['player'] else Fore.GREEN) + f'{summary["player"]} player(s) found'
    s_error = (Fore.YELLOW if summary['error'] else '') + f'{summary["error"]} error(s)'
    print('SUMMARY: ', s_total, ' | ', s_found, ' | ', s_player, ' | ', s_error)


if __name__ == "__main__":
    init(autoreset=True)
    if len(sys.argv) == 1:
        ap.parser.print_help()
        sys.exit()

    if ap.args['dir'] is not None:
        # Discover all *.log.gz files in the directory
        discovered = sorted(glob.glob(ap.args['dir'] + '/*.log.gz'))
        if len(discovered) != 0:
            summary = dict(
                player=0,
                error=0,
                found=0,
                total=len(discovered)
            )
            print(Style.BRIGHT + f'Discovered {len(discovered)} log file(s) in "{ap.args["dir"]}"')
            for file in discovered:
                try:
                    found = logparser.parse(file)
                    summary['player'] += len(found)
                    summary['found'] += 1 if len(found) != 0 else 0
                    print_players_list(found, ap.args['only_found'])
                except Exception as e:
                    print_file_exception(e, file, ap.args['ignore_errors'])
                    summary['error'] += 1
            print_summary(summary)
            sys.exit()
        else:
            print(f'No log files found in {ap.args["dir"]}')
            sys.exit(2)

    if len(ap.args['file']) != 0:
        for file in ap.args['file']:
            try:
                found = logparser.parse(file)
                print_players_list(found, ap.args['only_found'])
                sys.exit()
            except Exception as e:
                print_file_exception(e, file, ap.args['ignore_errors'])
                sys.exit(2)
