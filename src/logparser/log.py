import gzip
from os.path import basename


def _get_date(file_name):
    parsed_date = basename(file_name).split('-')
    return f'{parsed_date[2]}/{parsed_date[1]}/{parsed_date[0]}'


def parse(file_name):
    found = []
    f = gzip.open(file_name, 'rb')
    date = _get_date(file_name)
    for l in f:
        line = l.strip().decode('utf-8')
        if line.endswith('lost connection: You are not whitelisted on this server!') and line[12:30] == 'Server thread/INFO':
            # Extract time
            time = line[1:9]
            idname_splits = line.split('=')
            # Extract UUID and name
            id_ = idname_splits[1].split(',')[0]
            name = idname_splits[2].split(',')[0]
            # Extract IP and port
            ip = idname_splits[4].split('/')[1].split(')')[0].split(':')[0]
            found.append({
                'date': date,
                'time': time,
                'id': id_,
                'name': name,
                'ip': ip
            })
    return found
