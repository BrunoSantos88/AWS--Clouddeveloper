import boto3

session = boto3.session.Session(profile_name='dev')
s3 = session.resource('s3')

website_configuration = {
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Suffix': 'index.html'},
}

print("website static create")