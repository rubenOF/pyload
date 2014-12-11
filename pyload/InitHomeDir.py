# -*- coding: utf-8 -*-
# @author: RaNaN

""" This modules inits working directories and global variables, pydir and homedir """

from os import makedirs, path, chdir
from os.path import join
import sys
from sys import argv, platform

import __builtin__

__builtin__.owd = path.abspath("")  # original working directory
__builtin__.pypath = path.abspath(path.join(__file__, "..", ".."))

sys.path.append(join(pypath, "pyload", "lib"))

homedir = ""

if platform == 'nt':
    homedir = path.expanduser("~")
    if homedir == "~":
        import ctypes

        CSIDL_APPDATA = 26
        _SHGetFolderPath = ctypes.windll.shell32.SHGetFolderPathW
        _SHGetFolderPath.argtypes = [ctypes.wintypes.HWND,
                                     ctypes.c_int,
                                     ctypes.wintypes.HANDLE,
                                     ctypes.wintypes.DWORD, ctypes.wintypes.LPCWSTR]

        path_buf = ctypes.wintypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        result = _SHGetFolderPath(0, CSIDL_APPDATA, 0, 0, path_buf)
        homedir = path_buf.value
else:
    homedir = path.expanduser("~")

__builtin__.homedir = homedir

args = " ".join(argv[1:])

# dirty method to set configdir from commandline arguments
if "--configdir=" in args:
    for aa in argv:
        if aa.startswith("--configdir="):
            configdir = aa.replace("--configdir=", "", 1).strip()
elif path.exists(path.join(pypath, "pyload", "config", "configdir")):
    f = open(path.join(pypath, "pyload", "config", "configdir"), "rb")
    c = f.read().strip()
    f.close()
    configdir = path.join(pypath, c)
else:
    if platform in ("posix", "linux2"):
        configdir = path.join(homedir, ".pyload")
    else:
        configdir = path.join(homedir, "pyload")

if not path.exists(configdir):
    makedirs(configdir, 0700)

__builtin__.configdir = configdir
chdir(configdir)

# print "Using %s as working directory." % configdir