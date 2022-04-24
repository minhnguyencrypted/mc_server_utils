import sys
import os
import glob
from colorama import init
from . import log
from . import args
from . import util
from . import printf


def parse_files(files, args):
    summary = util.init_summary(total=len(files))
    for f in files:
        basef = os.path.basename(f)
        try:
            found = log.parse(f)
            summary['player'] += len(found)
            summary['found'] += 1 if len(found) != 0 else 0
            printf.print_players_list(found, basef, args['only_found'])
        except Exception as e:
            printf.print_file_exception(e, basef, args['ignore_errors'])
            summary['error'] += 1
    return summary


if __name__ == "__main__":
    init(autoreset=True)
    if len(sys.argv) == 1:
        args.parser.print_help()
        sys.exit()

    if len(args.args['file']) != 0:
        summary = util.init_summary()
        for file in args.args['file']:
            if os.path.isdir(file):
                files = glob.glob(file + '*.log.gz') if file.endswith('/') else glob.glob(file + '/*.log.gz')
                if args.args['dates']:
                    files = [f for f in files if util.fname_to_datestr(os.path.basename(f)) in args.args['dates']]
                    print(f'"{file}": discovered {len(files)} file(s) matched the date(s)')
                else:
                    print(f'"{file}": discovered {len(files)} file(s)')
                fsummary = parse_files(sorted(files), args.args)
                summary = util.update_summary(fsummary, summary)
            else:
                if args.args['dates'] and util.fname_to_datestr(os.path.basename(file)) not in args.args['dates']:
                    continue
                fsummary = parse_files([file], args.args)
                summary = util.update_summary(fsummary, summary)
        printf.print_summary(summary)
