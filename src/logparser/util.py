def fname_to_datestr(file):
    # YYYY-MM-DD
    splits = file[:10].split('-')
    if len(splits) == 3:
        # DD/MM/YYYY
        return f'{splits[2]}/{splits[1]}/{splits[0]}'
    else:
        return None


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
