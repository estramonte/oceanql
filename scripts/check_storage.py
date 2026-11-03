import os

import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    endpoint_url=os.getenv("S3_ENDPOINT_URL") or None,
    region_name=os.getenv("S3_REGION"),
    aws_access_key_id=os.getenv("S3_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("S3_SECRET_ACCESS_KEY"),
)

bucket = os.getenv("S3_BUCKET")

#creating the bucket if it doesn't exist yet (i think harmless)
existing = [b["Name"] for b in s3.list_buckets()["Buckets"]]
if bucket not in existing:
    s3.create_bucket(Bucket=bucket)

s3.put_object(Bucket=bucket, Key="healthcheck.txt", Body=b"ok")
print("Wrote healthcheck.txt to", bucket)
print([o["Key"] for o in s3.list_objects_v2(Bucket=bucket).get("Contents", [])])