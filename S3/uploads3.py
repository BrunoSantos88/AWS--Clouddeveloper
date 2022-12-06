import boto3

session = boto3.session.Session(profile_name='dev')
s3 = session.resource('s3')


filename = 'index.html'
bucket_name = 'my-bucket13131lab12'


    