#!/usr/bin/python3
# -*- coding: utf-8 -*-

###################################################
# This is a small cat command written in Python3.x.
###################################################

import os, sys
import re
import argparse

import datetime
import pwd, grp, stat

parser = argparse.ArgumentParser(description='concatenate files')
parser.add_argument('file', action='store', type=str, nargs='+', help='files of concatenate')
parser.add_argument('-n', '--number', action='store_true',help='number all output lines')
args = parser.parse_args()


def main():
    line_number = 1

    for filename in args.file:
        f=open(filename)
        if args.number is True:
            for line in f:
                print(line_number, line, end='')
                line_number += 1
        else:
            for line in f:
                print(line, end='')

if __name__ == '__main__':
    main()
