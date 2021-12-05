'''
Created on 
Course work: 
@author: raja
Source:
    https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html
    https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
    https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html
    https://github.com/gnocchixyz/gnocchi/blob/master/gnocchi/common/s3.py
S3 Location:
    s3://tactindia/featurepreneur/
'''

# Import necessary modules
import logging
import boto3
from botocore.exceptions import ClientError
from decouple import config
from botocore.config import Config


def get_connection(conf):

    if boto3 is None:
        raise RuntimeError("boto3 unavailable")

    conn = boto3.client(
        's3',
        # endpoint_url = conf.s3_endpoint_url,
        region_name = conf.s3_region_name,
        aws_access_key_id = conf.s3_access_key_id,
        aws_secret_access_key = conf.s3_secret_access_key,
        config = boto_config.Config(
            max_pool_connections = conf.s3_max_pool_connections
        )
    )

    return conn, conf.s3_region_name, conf.s3_bucket_prefix

def upload_file_with_local_env(file_name, bucket, object_name = None):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # my_config = Config(
    #     s3_region_name = config("LOCAL_AWS_REGION_NAME"),
    #     s3_access_key_id = config("LOCAL_AWS_ACCESS_KEY_ID"),
    #     s3_secret_access_key = config("LOCAL_AWS_SECRET_ACCESS_KEY"),
    #     s3_max_pool_connections = 10
    # )

    my_config = {
        's3_region_name' : config("LOCAL_AWS_REGION_NAME")
    }

    logging.info(my_config)

    # Upload the file
    # s3_client = boto3.client('s3', config = my_config)
    s3_client, conf.s3_region_name, conf.s3_bucket_prefix = get_connection(my_config)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False

    return True

def upload_file(file_name, bucket, object_name = None):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False

    return True

def startpy():
    
    filename    = '/Users/rajacsp/datasets/clown_101.jpg'
    bucket_name = 'tactindia'
    # bucket_name = "firstfileuploadbkt"

    result = upload_file(filename, bucket_name, 'foldername/clown_202.jpg')

    # result = upload_file_with_local_env(filename, bucket_name, 'clown_202.jpg')

    print('finished : ', result)


if __name__ == '__main__':
    startpy()