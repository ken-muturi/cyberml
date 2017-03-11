import boto3
import json

client = boto3.client('machinelearning')

#Sample Dataset
modelid = 'ml-WyHzVJ9rBx4'
endpoint = 'https://realtime.machinelearning.us-east-1.amazonaws.com'

print('Requesting...')

response = client.predict(
    MLModelId=modelid,
    Record={
        'text':'ls -al',
        'catageory':'waiter'
    },
    PredictEndpoint=endpoint
)

print(json.dumps(response))
