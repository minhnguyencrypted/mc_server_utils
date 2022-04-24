from colorama import Style, Fore


def print_file_exception(exception, filename, ignore_errors):
    msg = f'{Style.BRIGHT}{Fore.RED}[ERROR] {Style.RESET_ALL}"{filename}":'
    if not ignore_errors:
        if isinstance(exception, FileNotFoundError):
            print(msg + f'{Style.BRIGHT} File not found')
        elif isinstance(exception, PermissionError):
            print(msg + f'{Style.BRIGHT} Permission denied')
        else:
            print(msg + f'{Style.BRIGHT} {str(exception)}')


def print_players_list(players, file, only_found):
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
