#!/usr/bin/python3

import re, sys, argparse

def handler(inp,out):
    # Define Variables
    input_file_name = inp
    output_file_name = out
    flag = False
    arg_flag = False
    pipe_flag = False
    prev_flag = False
    prev_arg_flag = False
    prev_pipe_flag = False

    # Open Files
    try:
        file = open(input_file_name,'r')
    except:
        print('Error opening the input file, please try again.')

    try:
        output = open(output_file_name,'w')
    except:
        print('Error opening the output file, please try again.')

    # Setup Regex
    try:
        r = re.compile('-[a-zA-Z0-9_]*\n')
        n = re.compile('<[\w]>\n')
        g = re.compile('<GENSYM:[0-9]>/[\w]*\n')
    except:
        print('An error has occured involving the regular expressions, please try again.')

    # Examine each line and write to output
    for line in file:
        # Remove unnessecary delimiters
        if line not in ('**EOF**\n', '**SOF**\n') and n.match(line) is None and g.match(line) is None:

            # Check to see what we got
            if r.match(line) is not None:
                arg_flag = True
            elif line in ('|\n'):
                pipe_flag = True
            else:
                flag = True

            # if first line of file
            if prev_flag is False and prev_arg_flag is False and prev_pipe_flag is False and flag is True:
                output.write(line.rstrip() + ' ')

            # if you just had a regular command and this is a regular command then new line
            elif prev_flag is True and flag is True:
                output.write(',normal\n')
                output.write(line.rstrip() + ' ')

            # if you just had a regular command and this is either a pipe or arg then hold up
            elif prev_flag is True and arg_flag is True:
                output.write(line.rstrip() + ' ')
            elif prev_flag is True and pipe_flag is True:
                output.write(line.rstrip() + ' ')

            # if you just had an arg and this is a regular command then new line
            elif prev_arg_flag is True and flag is True:
                output.write(',normal\n')
                output.write(line.rstrip() + ' ')

            # if you just had an arg and this is a pipe or an arg then hold up
            elif prev_arg_flag is True and arg_flag is True:
                output.write(line.rstrip() + ' ')
            elif prev_arg_flag is True and pipe_flag is True:
                output.write(line.rstrip() + ' ')

            # if you just had a pipe and this is a command then hold up
            elif prev_pipe_flag is True and flag is True:
                output.write(line.rstrip() + ' ')

            # Reset variables
            flag = False
            arg_flag = False
            pipe_flag = False
            prev_flag = False
            prev_arg_flag = False
            prev_pipe_flag = False

            # Let ourselves know what we had
            if r.match(line) is not None:
                prev_arg_flag = True
            elif line in ('|\n'):
                prev_pipe_flag = True
            else:
                prev_flag = True
    sys.exit()

parser = argparse.ArgumentParser()
parser.add_argument("input", help="this goes first, the name of the file you want to read")
parser.add_argument("output", help="this comes second, the name of the file you want to write")
args = parser.parse_args()

try:
    handler(args.input,args.output)
except KeyboardInterrupt:
    print("\nProgram terminated.")
    sys.exit()
except (RuntimeError, TypeError, NameError, IOError):
    print("\nOh no! An error has occured!", sys.exc_info()[0])
    raise
