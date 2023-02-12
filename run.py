""" Use to download torrent files from yts.mx website. """
from typing import NamedTuple
import argparse
import log
import yts


class ProgramFlags(NamedTuple):
    """Program flags"""

    print_only: bool
    download_torrents: bool
    log_filename: str


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
        default=False,
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
    args = parser.parse_args()
    with log.LogFile(args.log_filename):
        if args.print_only == args.download_torrents:
            raise SystemExit("Please only use --print-only or --download-torrents.")

        flags = ProgramFlags(args.print_only, args.download_torrents, args.log_filename)
        yts_mx = yts.YTS(flags=flags)
        yts_mx.run()


if __name__ == "__main__":
    main()
