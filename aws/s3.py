import boto3

session = boto3.session.Session(profile_name='cbc-sandbox-saml')
s3 = session.resource('s3')
iam = session.client('iam')

def find_user_and_groups():
    for userlist in iam.list_users()['Users']:
        userGroups = iam.list_groups_for_user(UserName=userlist['UserName'])
        print("Username: "  + userlist['UserName'])
        print("Assigned groups: ")
        for groupName in userGroups['Groups']:
            print(groupName['GroupName'])
        print("----------------------------")

find_user_and_groups()
#for bucket in s3.buckets.all():
#      print(bucket.name)
