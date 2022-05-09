from colorama import Style, Fore
RED_TEXT = Fore.RED + Style.BRIGHT
GREEN_TEXT = Fore.GREEN + Style.BRIGHT
YELLOW_TEXT = Fore.YELLOW
CYAN_TEXT = Fore.CYAN + Style.BRIGHT
RESET = Style.RESET_ALL


def player(p):
    print(f'{p["date"]}  {p["time"]}     {p["name"]:21}{p["ip"]:19}{p["id"]}')


def exception(e, filename, ignore_errors):
    if not ignore_errors:
        if isinstance(e, FileNotFoundError):
            print(f'{RED_TEXT}ERROR{RESET} {filename}: File not found')
        elif isinstance(e, PermissionError):
            print(f'{RED_TEXT}ERROR{RESET} {filename}: Permission denied')
        else:
            print(f'{RED_TEXT}ERROR{RESET} {filename}: {str(e)}')


def summary(found_dict):
    total = 0
    totalerr = 0
    for value in found_dict.values():
        if type(value) == list:
            total += len(value)
        else:
            totalerr += 1
    print(f'Parsed {len(found_dict)} file(s): {total} player(s) found and {totalerr} error(s)')
