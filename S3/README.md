# Desafio

Tarefa 1: Preparar o laboratório

Pegar credencias Lab e criar um arquivo .aws/credential

[dev]
aws_access_key_id= AcceKey
aws_secret_access_key=SecretKey
aws_session_token=Secrettoken

.aws/config

[default]
region = us-east-1
output = json

para usar no parametro boto3
exemplo:

import boto3 
session = boto3.session.Session(profile_name='dev')

criar bucket S3 boto3

Python (3.6.8)	https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.create_bucket


Tarefa 2 Criar um arquivo HTML

Arquivo HTML exemplo.

Nesse arquivo, cole as seguintes linhas de HTML:
<!DOCTYPE html>
<html>
<head>
    <title>Cat Lost and Found</title>
</head>
<body>
    <h1>Lost Cat</h1>
    <h2>Call me if this is your cat</h2>
    <p>My number is 000 000 0000</p>
    <img alt="this is a picture of a lost cat" src="cat.jpg" /> 
</body>
</html>

Salve o arquivo. Para fazer isso, no menu File (Arquivo), escolha Save As... (Salvar como...). Verifique se a pasta raiz s3-lab está selecionada e salve o arquivo como index.html.

Python (3.6.8)	https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.upload_file

Tarefa 3: Usar o SDK da AWS para aplicar uma política de bucket do S3

Exemplo:
{
  "Version":"2012-10-17",
  "Statement":[{
    "Sid":"PublicReadGetObject",
        "Effect":"Allow",
      "Principal": "*",
      "Action":["s3:GetObject"],
      "Resource":["arn:aws:s3:::2019-04-11-er-catlostandfoundwebsite/*"
      ]
    }
  ]
}

https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_bucket_policy

Tarefa 4: Usar o SDK da AWS para habilitar a hospedagem de sites no bucket do S3

https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_bucket_website