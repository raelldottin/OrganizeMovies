""" Use to download torrent files from yts.mx website. """
import argparse
import log
import yts


flags = {
    "print_only": False,
    "download_torrents": True,
    "log_filename": "",
    "query_string": "",
}


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
        flags["print_only"] = args.print_only
        flags["download_torrents"] = args.download_torrents
        flags["log_filename"] = args.log_filename
        yts_mx = yts.YTS(flags=flags)
        yts_mx.run()


if __name__ == "__main__":
    main()
