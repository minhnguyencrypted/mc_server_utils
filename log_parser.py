import gzip


def parse(file_name):
    found = []
    f = gzip.open(file_name, 'rb')
    for l in f:
        line = l.strip().decode('utf-8')
        if 'lost connection: You are not whitelisted on this server!' in line:
            splits1 = line.split('[')
            # Stripping time from the line
            time = splits1[1].split(']')[0]
            # Stripping player name from the line
            splits2 = splits1[3].split('=')
            player_id = splits2[1].split(',')[0]
            player_name = splits2[2].split(',')[0]
            # Stripping IP address and port number from the line
            ip_port = splits2[4].split('/')[1].split(')')[0]
            found.append(f'{time} {player_id} {player_name} {ip_port}')
    return found
