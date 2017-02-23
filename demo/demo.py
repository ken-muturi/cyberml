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
        'age':'21',
        'job':'waiter',
        'marital':'single',
        'education':'college',
        'default':'none',
        'housing':'rent',
        'loan':'none',
        'contact':'phone',
        'month':'march',
        'day_of_week':'monday',
        'duration':'1',
        'campaign':'1',
        'pdays':'1',
        'previous':'1',
        'poutcome':'none',
        'emp_var_rate':'1',
        'cons_price_idx':'1',
        'cons_conf_idx':'1',
        'euribor3m':'1',
        'nr_employed':'1',
        'y':'1'
    },
    PredictEndpoint=endpoint
)

print(json.dumps(response))
