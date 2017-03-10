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
        # Remove unnessecary stuff
        before, sep, after = line.rpartition(";")
        output.write(after)

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
