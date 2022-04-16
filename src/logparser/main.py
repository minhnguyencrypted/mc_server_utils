import sys
import getopt
import log_parser


def print_help():
    print("""Usage:
    -h, --help: show this help message and exit
    -f, --file: specify the log file to parse""")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print_help()
        sys.exit()
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "file="])
    except getopt.GetoptError as err:
        print("Error: " + str(err))
        print_help()
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            print_help()
        elif o in ("-f", "--file"):
            try:
                found = log_parser.parse(a)
                if found:
                    print(f'Found {len(found)} un-whitelisted player(s)')
                    for player in found:
                        print(player)
                else:
                    print('No un-whitelisted players found')
            except FileNotFoundError:
                print(f'{a}: No such file or directory')
            except PermissionError:
                print(f'{a}: Permission denied')
            except Exception as e:
                print(f'{a}: Unknown error')
