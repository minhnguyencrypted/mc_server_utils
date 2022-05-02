from colorama import Style, Fore

RED_TEXT = Fore.RED + Style.BRIGHT
GREEN_TEXT = Fore.GREEN + Style.BRIGHT
YELLOW_TEXT = Fore.YELLOW
RESET = Style.RESET_ALL
CYAN_TEXT = Fore.CYAN + Style.BRIGHT


def _print_player(p, verbose):
    if verbose:
        print(f'    Player: {YELLOW_TEXT}{p["name"]}')
        print(f'        UUID: {p["id"]}')
        print(f'        IP address: {CYAN_TEXT}{p["ip"]}')
        print(f'        Time: {p["time"]}')
    else:
        print(f'{p["date"]}  {p["time"]}  {p["id"]}  {p["name"]:21}{p["ip"]}')


def print_file_exception(exception, filename, ignore_errors):
    if not ignore_errors:
        if isinstance(exception, FileNotFoundError):
            print(f'"{filename}":{Style.BRIGHT} File not found')
        elif isinstance(exception, PermissionError):
            print(f'"{filename}":{Style.BRIGHT} Permission denied')
        else:
            print(f'"{filename}":{Style.BRIGHT} {str(exception)}')


def print_players_list(players, args):
    if args['only_found'] and not players:
        return
    for p in players:
        _print_player(p, args['verbose'])


def print_summary(summary):
    s_total = f'{summary["total"]} file(s) searched'
    s_found = f'{RED_TEXT if summary["found"] else GREEN_TEXT}{summary["found"]} file(s) found players {RESET}'
    s_player = f'{RED_TEXT if summary["player"] else GREEN_TEXT}{summary["player"]} player(s) found {RESET}'
    s_error = f'{YELLOW_TEXT if summary["error"] else ""}{summary["error"]} error(s) {RESET}'
    print(f'SUMMARY: {s_total} | {s_found} | {s_player} | {s_error}')
