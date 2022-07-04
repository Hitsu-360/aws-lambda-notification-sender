import boto3

class email_handler():  
    
    def __init__(self):
        
        self.ses_client = boto3.client("ses", region_name="us-west-2")
        self.source_email = 'Notification <domain@email.com>'

    def verify_email_identity(self):
        
        response = self.ses_client.verify_email_identity(
            EmailAddress="leandro.cavalcanti@email.com"
        )
        print(response)
    
    def send_email(self, addresses, subject, content):
    
        CHARSET = "UTF-8"
    
        response = self.ses_client.send_email(
            Destination={
                "ToAddresses":addresses,
            },
            Message={
                "Body": {
                    "Html": {
                        "Charset": CHARSET,
                        "Data": content,
                    }
                },
                "Subject": {
                    "Charset": CHARSET,
                    "Data": subject,
                },
            },
            Source=self.source_email,
        )
        
        return response
