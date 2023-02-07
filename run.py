import argparse
import log
import yts


'''
global print_only, download_torrents, log_filename

print_only = False
download_torrents = False
log_filename = ""
'''


def main():
    '''Program entry point'''
    parser = argparse.ArgumentParser(
        description='Retrieve torrent files from yts.mx'
    )
    parser.add_argument(
        '-p',
        '--print-only',
        action='store_true',
        dest="print_only",
        default=False,
        help='Display torrent file URL only.',
    )
    parser.add_argument(
        '-d',
        '--download-torrents',
        action='store_true',
        dest='download_torrents',
        default=False,
        help='Download torrent file to current directory.',
    )
    parser.add_argument(
        '-l',
        '--log-file',
        action="store",
        dest='log_filename',
        default="",
        help='Log path and file name',
        required=True,
    )
    args = parser.parse_args()
    with log.LogFile(args.log_filename):
        if args.print_only and args.download_torrents:
            raise SystemExit('Please only --print_only or --download_torrents.')

        
            print_only
            download_torrents
            log_filename
if __name__ == '__main__':
    main()
