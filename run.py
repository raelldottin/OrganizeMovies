import argparse
import log
import yts

def main():
    parser = argparse.ArgumentParser(
        description='Retrieve torrent files from yts.mx'
    )
    parser.add_argument(
        '-p',
        '--print-only',
        nargs=0,
        dest="print_only",
        default=1,
        help='Display torrent file URL only.',
    )
    parser.add_argument(
        '-d',
        '--download-torrents',
        nargs=0,
        dest='download_torrents',
        default=0,
        help='Download torrent file to current directory.',
    )
    parser.add_argument(
        '-l',
        '--log-file',
        nargs=0,
        dest='log_filename',
        default="",
        help='Log path and file name',
    )
    args = parser.parse_args()
    with logLogFile()

if __name__ == '__main__':
    main()
