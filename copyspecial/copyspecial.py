#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import re
import os
import shutil
import subprocess
from pathlib import Path

"""Copy Special exercise
"""


# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
    dir_list = os.listdir(dir)
    l = []
    for d in dir_list:
        names = "_(.*?)_"
        name_l = re.findall(names, d)
        if name_l:
            print(os.path.abspath(d))
            l.append(d)
    return l

def copy_to(paths, dir):
    list_dir = get_special_paths(paths)
    for l in list_dir:
        shutil.copy(l,dir)

def zip_to(paths, zippath):
    list_dir = get_special_paths(paths)
    for l in list_dir:
        shutil.make_archive(l,'zip',zippath)

def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]");
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    print(args)
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]
        #print(sys.argv[1])
        copy_to('.',todir)
    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]
        zip_to('.',tozip)
    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()

