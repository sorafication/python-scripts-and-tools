import boto3
import json
import os

saml_string = """ Input here the Input of the current XML file
"""


def role_arn_to_session(**args):
    client = boto3.client('sts')
    response = client.assume_role(**args)
    return boto3.Session(
        aws_access_key_id=response['Credentials']['AccessKeyId'],
        aws_secret_access_key=response['Credentials']['SecretAccessKey'],
        aws_session_token=response['Credentials']['SessionToken'])


def update_saml_xml(policy_arn, account_id):
    session = role_arn_to_session(
        RoleArn=policy_arn,
        RoleSessionName='SessionName111')
    client = session.client('sqs')
    iam = session.client('iam')
    s3 = session.resource('s3')
    sts = session.client('sts')
    account_alias = iam.list_account_aliases().get("AccountAliases")
    print("Hi Ich bin im Account: " + str(account_alias))
    response = iam.update_saml_provider(
       SAMLProviderArn='arn:aws:iam::' + str(account_id) + ':saml-provider/Provider.com', # CVhange Provider ARN
       SAMLMetadataDocument=saml_string
    )
    print(response)

# This was used for testing if access to all Accounts is possible.


def s3_list(account_id):
    session = role_arn_to_session(
        RoleArn=policy_arn,
        RoleSessionName='Session')
    client = session.client('sqs')
    iam = session.client('iam')
    s3 = session.resource('s3')
    account_alias = iam.list_account_aliases().get("AccountAliases")
    print("Hi Ich bin im Account: " + str(account_alias))
    for bucket in s3.buckets.all():
        print(bucket.name)

# "MAIN"



f = open('awsaccounts.json')
data = json.load(f)
f.close()


for elem in data['Resource']:
    policy_arn = elem
    account_id = elem.split(":")[4]
    print("ARN der Policy: " + policy_arn)
    print("Account ID: " + account_id)
    update_saml_xml(policy_arn, account_id)
    # s3_list(account_id) This was used for testing if access to all Accounts is possible.
