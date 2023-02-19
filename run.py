""" Use to download torrent files from yts.mx website. """
import argparse
import log
import yts


ProgramFlags = {
    "print_only": False,
    "download_torrents": True,
    "log_filename": "",
    "query_string": "",
    "verbose": False,
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
        dest="query_string",
        default="",
        help="Query string for YTS",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        dest="verbose",
        default=False,
        help="Display debugging messages",
    )
    args = parser.parse_args()
    with log.LogFile(args.log_filename):
        if args.print_only == args.download_torrents:
            raise SystemExit("Please only use --print-only or --download-torrents.")

        ProgramFlags["print_only"] = args.print_only
        ProgramFlags["download_torrents"] = args.download_torrents
        ProgramFlags["log_filename"] = args.log_filename
        ProgramFlags["query_string"] = args.query_string
        ProgramFlags["verbose"] = args.verbose
        yts_mx = yts.YTS(flags=ProgramFlags)
        yts_mx.run()


if __name__ == "__main__":
    main()
