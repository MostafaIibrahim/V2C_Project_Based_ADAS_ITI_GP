import boto3
import json
import csv
import time
from collections import deque

# Specify your AWS credentials
aws_access_key_id = 'AKIAW5XL6GLMXR5MPZWJ'
aws_secret_access_key = 'EMSfHY6UDtt0nzJova4PjvZfqAtxK595rTrCtaSh'

# Initialize the S3 client with your credentials
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Define the bucket name
bucket_name = 'v2c-bucket-v0'
# JSON file to write
json_file = "GUI_data.json"
# CSV file to append to
csv_file = "gps_reading.csv"

while True:
    try:
        # List objects in the bucket
        objects = s3.list_objects_v2(Bucket=bucket_name)
        
        # Sort the objects by their last modification timestamp
        sorted_objects = sorted(objects['Contents'], key=lambda x: x['LastModified'], reverse=True)
        
        if sorted_objects:
            # Get the last (most recent) object
            last_object = sorted_objects[0]
            # Get the key of the last object (file.json)
            last_object_key = last_object['Key']
            

            # Download the content of the last object
            response = s3.get_object(Bucket=bucket_name, Key=last_object_key)

            file_content = response['Body'].read().decode('utf-8')

            data_dict = json.loads(file_content)

            # Send Received data into JSON and open file in write mode
            with open(json_file, mode='w', newline='\n') as file:
                json.dump(data_dict, file)

            # Data to append
            data_to_append = [data_dict['Latitude'], data_dict['longitude']]
            # Open the CSV file in append mode
            with open(csv_file, mode='a', newline='\n') as file:
                writer = csv.writer(file)
                # Write the data to the CSV file
                writer.writerow(data_to_append)
            print("Done")
        else:
            print("Bucket is empty.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    time.sleep(3)

