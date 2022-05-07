from os.path import basename


def _ftodate(file):
    # YYYY-MM-DD
    s = basename(file)[:10].split('-')
    if len(s) == 3:
        # DD/MM/YYYY
        return f'{s[2]}/{s[1]}/{s[0]}'
    else:
        return None


def filter_date(file, dates):
    return _ftodate(file) in dates


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
