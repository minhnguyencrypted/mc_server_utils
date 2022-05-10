from os.path import basename


def get_date(file):
    # YYYY-MM-DD
    s = basename(file)[:10].split('-')
    if len(s) == 3:
        # DD/MM/YYYY
        return f'{s[2]}/{s[1]}/{s[0]}'
    else:
        return None


def filter_date(file, dates):
    return get_date(file) in dates
