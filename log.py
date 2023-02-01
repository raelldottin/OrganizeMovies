import sys

class LogFile:
    def __init__(self, filename):
        self.logfile = open(filename, 'w')
        self.previous_stdout = sys.stdout
        sys.stdout = self

    def write(self, text):
        self.previous_stdout.write(text)
        self.logfile.write(text)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):     # type: ignore
        sys.stdout = self.previous_stdout

