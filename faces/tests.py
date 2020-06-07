import boto3

client = boto3.client("sns",
                      aws_access_key_id="AKIAZ2HF5Q4PHK6IMUWA",
                      aws_secret_access_key="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",
                      region_name="us-east-1")
client.publish(
    PhoneNumber="+918923108736",
    Message="Hello jay"
)