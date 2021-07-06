from pprint import pprint
import sys
from json import dumps

class Logger:
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    NC = '\033[0m'

    BOLD = '\033[1m'
    END_BOLD = '\033[0m'

    def __init__(self):
        pass

    def debug(self, message: str, data=None):
        sys.stdout.write(self.NC)
        print(message)
        if data:
            if type(data) == dict:
                print(dumps(data, indent=4))
            else:
                pprint(data)
        sys.stdout.write(self.NC)

    def error(self, message: str, data=None):
        sys.stdout.write(self.RED)
        print('===============LowDB ERROR===============')
        sys.stdout.write(self.BOLD)
        print(message)
        if data:
            if type(data) == dict:
                print(dumps(data, indent=4))
            else:
                pprint(data)
        sys.stdout.write(self.END_BOLD)
        sys.stdout.write(self.RED)
        print('===============LowDB ERROR===============')
        sys.stdout.write(self.NC)

    def warning(self, message: str, data=None):
        sys.stdout.write(self.YELLOW)
        print(message)
        if data:
            if type(data) == dict:
                print(dumps(data, indent=4))
            else:
                pprint(data)
        sys.stdout.write(self.NC)
    
    def info(self, message: str, data=None):
        sys.stdout.write(self.BLUE)
        print(message)
        if data:
            if type(data) == dict:
                print(dumps(data, indent=4))
            else:
                pprint(data)
        sys.stdout.write(self.NC)

    def success(self, message: str, data=None):
        sys.stdout.write(self.GREEN)
        sys.stdout.write(self.BOLD)
        print(message)
        if data:
            if type(data) == dict:
                print(dumps(data, indent=4))
            else:
                pprint(data)
        sys.stdout.write(self.END_BOLD)
        sys.stdout.write(self.NC)