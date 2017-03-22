#!/usr/bin/python3
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

def wait_key():
    ''' Wait for a key press on the console and return it. '''
    result = None
    import termios, sys
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    try:
        result = sys.stdin.read(1)
    except IOError:
        pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result

with open('typescript', 'w') as script:
    def read(fd):
        data = os.read(fd, 1024)
        # Parse on the hashtag
        cmd = data.decode()
        before, sep, after = cmd.rpartition("#")
        script.write(after)
        # wait_key()
        return data

    pty.spawn(shell, read)
