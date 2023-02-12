""" Use to download torrent files from yts.mx website. """
import argparse
import log
import yts


class OptionFlags(object):
    """Class with program flags"""

    print_only: bool
    download_torrents: bool
    log_filename: str
    query_string: str

    print_only = True
    download_torrents = False
    log_filename = ""
    query_string = ""

    def __init__(
        self,
        print_only: bool,
        download_torrents: bool,
        log_filename: str,
        query_string: str,
    ):
        self.print_only = print_only
        self.download_torrents = download_torrents
        self.log_filename = log_filename
        self.query_string = query_string

    def __repr__(self):
        message = "\n".join(
            [
                f"{self.print_only=}",
                f"{self.download_torrents=}",
                f"{self.log_filename=}",
                f"{self.query_string=}",
            ]
        )
        return print(message)


def main():
    """Program entry point"""
    parser = argparse.ArgumentParser(description="Retrieve torrent files from yts.mx")
    parser.add_argument(
        "-p",
        "--print-only",
        action="store_true",
        dest="print_only",
        default=False,
        help="Display torrent file URL only.",
    )
    parser.add_argument(
        "-d",
        "--download-torrents",
        action="store_true",
        dest="download_torrents",
        default=True,
        help="Download torrent file to current directory.",
    )
    parser.add_argument(
        "-l",
        "--log-file",
        action="store",
        dest="log_filename",
        default="",
        help="Log path and file name",
        required=True,
    )
    parser.add_argument(
        "-q",
        "--query",
        action="store",
        dest="query",
        default="",
        help="Query string for YTS",
    )
    args = parser.parse_args()
    with log.LogFile(args.log_filename):
        if args.print_only == args.download_torrents:
            raise SystemExit("Please only use --print-only or --download-torrents.")
        flags = ProgramFlags(args.print_only, args.download_torrents, args.log_filename)
        yts_mx = yts.YTS(flags=flags)
        yts_mx.run()


if __name__ == "__main__":
    main()