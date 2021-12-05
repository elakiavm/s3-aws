'''
Created on 
Course work: 
@author: raja
Source:
    https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html
    
'''

# Import necessary modules
from flask import Flask, request
from flask import render_template
import boto3


app = Flask(__name__)


@app.route('/')
def home():
    return  render_template('index.html')


@app.route('/upload', methods = ['GET','POST'])
def upload_file():

    botos3   = boto3.resource('s3')
    file_obj = request.files['file']
    
    botos3.Bucket('firstfileuploadbkt').put_object(
        Key  = file_obj.filename, 
        Body = file_obj
    )

    return "File saved to S3"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000') 