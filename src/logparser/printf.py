from colorama import Style, Fore

RED_TEXT = Fore.RED + Style.BRIGHT
GREEN_TEXT = Fore.GREEN + Style.BRIGHT
YELLOW_TEXT = Fore.YELLOW
CYAN_TEXT = Fore.CYAN + Style.BRIGHT
RESET = Style.RESET_ALL


def player(p, verbose):
    if verbose:
        print(f'    Player: {YELLOW_TEXT}{p["name"]}')
        print(f'        UUID: {p["id"]}')
        print(f'        IP address: {CYAN_TEXT}{p["ip"]}')
        print(f'        Time and date: {p["time"]} {p["date"]}')
    else:
        print(f'{p["date"]}  {p["time"]}  {p["id"]}  {p["name"]:21}{p["ip"]}')


def exception(e, filename, ignore_errors):
    if not ignore_errors:
        if isinstance(e, FileNotFoundError):
            print(f'ERROR {filename}:{RED_TEXT} File not found')
        elif isinstance(e, PermissionError):
            print(f'ERROR {filename}:{RED_TEXT} Permission denied')
        else:
            print(f'ERROR {filename}:{RED_TEXT} {str(e)}')


def print_summary(summary):
    s_total = f'{summary["total"]} file(s) searched'
    s_found = f'{RED_TEXT if summary["found"] else GREEN_TEXT}{summary["found"]} file(s) found players {RESET}'
    s_player = f'{RED_TEXT if summary["player"] else GREEN_TEXT}{summary["player"]} player(s) found {RESET}'
    s_error = f'{YELLOW_TEXT if summary["error"] else ""}{summary["error"]} error(s) {RESET}'
    print(f'SUMMARY: {s_total} | {s_found} | {s_player} | {s_error}')
