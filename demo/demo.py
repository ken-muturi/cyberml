#!/usr/bin/python3

# Created by Joshua Bowen as a part of a NAU sponsered research project.
# No License, as-is, use as you wish. 3/21/2017

import boto3, json, os, subprocess, sys

# Set up Amazon Web Services connection
client = boto3.client('machinelearning')

# Get username, hostname, and working dir from local env
username = os.environ.get('USER')
hostname = os.environ.get('HOSTNAME')
wdir = os.environ.get('PWD')

# Machine Learning Endpoint
modelid = 'ml-lttAZ5X4uU8'
endpoint = 'https://realtime.machinelearning.us-east-1.amazonaws.com'

def get_input():

    # Update username, hostname, and working dir from terminal
    username = os.environ.get('USER')
    hostname = os.environ.get('HOSTNAME')
    wdir = os.environ.get('PWD')

    # Build command prompt
    prompt = str(username).rstrip() + '@' + str(hostname).rstrip() + ':' + str(wdir).rstrip() + '# '

    # Get user input
    cmd = input(prompt)

    # Convert to and understndable string
    cmds = str(cmd)

    return cmds

def get_prediction(request):

    # Correctly format request
    request = {"Var1":str(request)}

    # Send JSON-formatted request
    response = client.predict(
        MLModelId=modelid,
        Record=request,
        PredictEndpoint=endpoint
    )

    return response


def evaluate(command):

    # Get prediction from AWS-ML
    results = get_prediction(command)

    # Make results understandbale
    malicious = results['Prediction']['predictedScores']['malicious']
    mistake = results['Prediction']['predictedScores']['mistake']
    normal = results['Prediction']['predictedScores']['normal']

    # TODO add logic that makes sense and some actual calculations
    if malicious >= 0.2:
        evaluation = 0.1
    elif mistake >= 0.1:
        evaluation = 0.6
    elif normal >= 0.95:
        evaluation = 0.9
    else:
        # for testing purposes
        print("\nValue out of bounds:\n" + str(malicious) + "\n" + str(mistake) + "\n" + str(normal) + "\n")
        evaluation = 0

    return evaluation

try:
    while 2+2 == 4:
        # Get user input
        com = get_input()

        # Send input for evaluation
        ev = evaluate(com)

    # Decide what to do based on evaluation
        # if good, allow command
        if ev > 0.75:
            os.system(com)

        # if mistake, do not execute command
        elif ev <= 0.75 and ev >= 0.25:
            print('\nI think your command may be or contain a mistake, please try agian.')

        # if determined malicious, stop session
        elif ev < 0.25 and ev >= 0:
            print('\nIntruder detected!')
            sys.exit(1)

except KeyboardInterrupt:
    # TODO for high fidelity tests, do not allow keyboard interrups
    print("\nProgram Terminated by " + username)
    sys.exit(0)

except SystemExit:
    pass

except:
    # TODO need to capture and handle specific exceptions
    print("\nOh no! An error has occured!")
    raise

else:
    # If no exceptions, make a clean getaway
    sys.exit(0)
