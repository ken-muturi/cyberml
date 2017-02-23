import boto3

client = boto3.client('machinelearning')

#define modelid
#record=name:value
#define endpoint

response = client.predict(
    MLModelId='string',
    Record={
        'string': 'string'
    },
    PredictEndpoint='string'
)

#handle response
