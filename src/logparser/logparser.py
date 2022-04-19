import gzip


def parse(file_name):
    found = []
    f = gzip.open(file_name, 'rb')
    for l in f:
        line = l.strip().decode('utf-8')
        if line.endswith('lost connection: You are not whitelisted on this server!') and line[12:30] == 'Server thread/INFO':
            # Extract time
            time = line[1:9]
            idname_splits = line.split('=')
            # Extract UUID and name
            uuid = idname_splits[1].split(',')[0]
            name = idname_splits[2].split(',')[0]
            # Extract IP and port
            ip_port = idname_splits[4].split('/')[1].split(')')[0]
            found.append({
                'time': time,
                'id': uuid,
                'name': name,
                'ip_port': ip_port
            })
    return found
