#!/usr/bin/python3
# -*- coding: utf-8 -*-

###################################################
# This is a small list command written in Python3.x.
###################################################

import os, sys
import re
import argparse

import datetime
import pwd, grp, stat

parser = argparse.ArgumentParser(description='Show list.')
parser.add_argument('root_path', action='store', type=str, default='.', nargs='?', help='search path')
parser.add_argument('-a', '--all', action='store_true',help='show dotfiles')
parser.add_argument('-l', '--long', action='store_true',help='show more details')
args = parser.parse_args()


def make_listdir(show_all, listdir):
    """ make file list """
    if show_all is True:
        return listdir # include dotfiles
    else:
        return [filename for filename in listdir if re.match(r'^(?!\..*)', filename)] # exclude dotfiles


def print_permisions(st_mode):
    print( "d" if (stat.S_ISDIR(st_mode)) else "-", end='')
    print( "r" if (st_mode & stat.S_IRUSR) else "-", end='')
    print( "w" if (st_mode & stat.S_IWUSR) else "-", end='')
    print( "x" if (st_mode & stat.S_IXUSR) else "-", end='')
    print( "r" if (st_mode & stat.S_IRGRP) else "-", end='')
    print( "w" if (st_mode & stat.S_IWGRP) else "-", end='')
    print( "x" if (st_mode & stat.S_IXGRP) else "-", end='')
    print( "r" if (st_mode & stat.S_IROTH) else "-", end='')
    print( "w" if (st_mode & stat.S_IWOTH) else "-", end='')
    print( "x" if (st_mode & stat.S_IXOTH) else "-", end=' ')

def main():
    root_dir = make_listdir(args.all, os.listdir(args.root_path))

    for filename in root_dir:
        if args.long is True:
            statinfo = os.stat(args.root_path +"/"+ filename)                    # get statical information of files
            nlink   = statinfo.st_nlink                     # number of link
            pw_name = pwd.getpwuid(statinfo.st_uid).pw_name # get user name
            gr_name = grp.getgrgid(statinfo.st_gid).gr_name # get group name
            size    = statinfo.st_size                      
            time    = datetime.datetime.fromtimestamp(statinfo.st_atime) # convert Unix time to date

            print_permisions(statinfo.st_mode)
            print('{0} {1} {2} {3:4d} {4} {5}'.format(nlink, pw_name, gr_name, size, time, filename))
        else:
            print(filename)

if __name__ == '__main__':
    main()
