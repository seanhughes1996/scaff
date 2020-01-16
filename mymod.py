# this is a module - I want to stop people from executing it directly.

import sys


if __name__ == '__main__':

def myfunc():
    pass

print(__name__)

