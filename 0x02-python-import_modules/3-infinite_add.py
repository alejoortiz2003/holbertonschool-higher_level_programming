#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    c = 0
    for i in argv[1:]:
        c += int(i)
    print(c)
