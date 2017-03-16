#!/usr/bin/env python
#
# EXAMPLE
# ============================
# FROM: https://docs.python.org/3.5/library/pty.html
#
# import argparse, os, pty, sys, time
#
# parser = argparse.ArgumentParser()
# parser.add_argument('-a', dest='append', action='store_true')
# parser.add_argument('-p', dest='use_python', action='store_true')
# parser.add_argument('filename', nargs='?', default='typescript')
# options = parser.parse_args()
#
# shell = sys.executable if options.use_python else os.environ.get('SHELL', 'sh')
# filename = options.filename
# mode = 'ab' if options.append else 'wb'
#
# with open(filename, mode) as script:
#     def read(fd):
#         data = os.read(fd, 1024)
#         script.write(data)
#         return data
#
#     print('Script started, file is', filename)
#     script.write(('Script started on %s\n' % time.asctime()).encode())
#
#     pty.spawn(shell, read)
#
#     script.write(('Script done on %s\n' % time.asctime()).encode())
#     print('Script done, file is', filename)

import os, pty

shell = os.environ.get('SHELL', 'sh')

def read(fd):
    data = os.read(fd, 1024)
    return data

pty.spawn(shell, read)
