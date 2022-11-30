import boto3

session = boto3.session.Session(profile_name='dev')
s3 = session.resource('s3')


filename = 'index.html'
bucket_name = 'my-bucket13131lab12'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.

    