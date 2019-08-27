import os
from boto3 import s3
import botocore

BUCKET_NAME = os.getenv('BUCKET_NAME') or ''
KEY = os.getenv('KEY') or ''

def transfer_resources():
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, '')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] =='404':
            print('The object does not exist')
        else:
            raise

if __name__ == '__main__':
    transfer_resources()