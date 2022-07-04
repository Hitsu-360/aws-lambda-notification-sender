from email_handler import email_handler

import json
import boto3
import pandas

# S3
BUCKET = '<aws-lambda-notification-bucket>'

S3 = boto3.resource(
    's3',
    region_name='us-west-2'
)

NOTIFICATION_TEMPLATE = '''
    <html>
        <head>
            <style>
                table, th, td {{
                    font-family: calibri;
                    border: 1px solid black;
                    border-collapse: collapse;
                }}
                th, td {{
                    padding: 8px; 
                }}
                span {{
                    color:red;
                }}
            </style>
        </head>
        <body>
            <h1>{0}</h1>
            <br>
            <div>
                {1}
            </div>
        </body>
    </html>
'''
EMAIL_LIST = [
    'leandro.cavalcanti@email.com'
]

def format_html_content(template, data):
    
    html_content = template.format(*data)
    
    return html_content
    
def load_s3_file_content(s3_path, s3_file_content):
     # Init bucket object
    bucket = S3.Bucket(BUCKET)
    
    # Write to file    
    bucket.put_object(Key=s3_path, Body=s3_file_content)

def handle_notification(email_message):
    
    subject = f'Notification Subject'

    html_content = format_html_content(NOTIFICATION_TEMPLATE, [subject, email_message])    
    
    # Init Email Class
    email = email_handler() 

    # List of contacts to send
    email_group = EMAIL_LIST
    
    # Send email
    email.send_email(email_group, subject, html_content)        

def lambda_handler(request, context):
          
	handle_notification(request['email_message'])
            
	return {}
