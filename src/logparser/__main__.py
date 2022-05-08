import sys
import glob
from os.path import basename, isdir
from colorama import init
from natsort import natsorted
from . import log
from . import args
from . import util
from . import printf


def parse_files(files):
    found = dict()
    for f in files:
        try:
            found[basename(f)] = log.parse(f)
        except Exception as e:
            found[basename(f)] = e
    return found


if __name__ == "__main__":
    init(autoreset=True)
    if len(sys.argv) == 1:
        args.parser.print_help()
        sys.exit()

    files = []
    if args.args['file']:
        for file in args.args['file']:
            if isdir(file):
                files += glob.glob(file + '*.log.gz') if file.endswith('/') else glob.glob(file + '/*.log.gz')
            else:
                files.append(file)
    files = natsorted(files)

    if args.args['dates']:
        files = filter(lambda f: util.filter_date(f, args.args['dates']), files)

    found = parse_files(files)
    for k, v in found.items():
        if type(v) == list:
            for p in v:
                printf.player(p)
        else:
            printf.exception(v, k, args.args['ignore_errors'])

    if args.args['summary']:
        printf.summary(found)
