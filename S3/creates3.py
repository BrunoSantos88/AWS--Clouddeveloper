import boto3

session = boto3.session.Session(profile_name='dev')
s3 = session.resource('s3')

s3.create_bucket(Bucket='my-bucket13131lab12')

for bucket in s3.buckets.all():
    print(bucket.name)
    print("bucket criado")