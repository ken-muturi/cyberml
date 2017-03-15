#!/usr/bin/env python

import boto3
import json

client = boto3.client('machinelearning')

# Sample Dataset
# modelid = 'ml-WyHzVJ9rBx4'
# endpoint = 'https://realtime.machinelearning.us-east-1.amazonaws.com'

def get_prediction(request):

    print('Requesting...')

    response = client.predict(
        MLModelId=modelid,
        Record=request,
        PredictEndpoint=endpoint
    )

    print(json.dumps(response))
