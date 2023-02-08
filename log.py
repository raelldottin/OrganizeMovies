""" Use to write output to the log file and standard output """
import sys


class LogFile:
    """Output to logfile and stdout"""

    def __init__(self, filename):
        self.logfile = open(filename, "w")
        self.previous_stdout = sys.stdout
        sys.stdout = self

    def write(self, text):
        self.previous_stdout.write(text)
        self.logfile.write(text)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        sys.stdout = self.previous_stdout
