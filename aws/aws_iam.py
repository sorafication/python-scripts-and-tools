import boto3
from pprint import pprint
import secrets
import string
import sys
dic_pass = {}
anz_accounts = 15
task = ""


def aws_profile(aws_profile_name):
    return boto3.session.Session(profile_name=aws_profile_name)
    print(f"Hallo Ich bin im Account {aws_profile_name}")


def aws_check_user(aws_profile_name):
    try:
        resp = iam.get_user(UserName=aws_profile_name)
        pprint(resp)
        return True
    except iam.exceptions.NoSuchEntityException:
        return False
#    except BotoServerError as e:
#        print(e.message)


def aws_create_user(aws_profile_name):
    aws_password = ''.join(secrets.choice(string.ascii_uppercase +
                           string.digits +
                           string.ascii_lowercase) for _ in range(18))
    iam.create_user(
        UserName=aws_profile_name
    )
    response = iam.create_login_profile(
        UserName=aws_profile_name,
        Password=aws_password,
        PasswordResetRequired=False
    )
    pprint(response)
    response = iam.attach_user_policy(
        UserName=aws_profile_name,
        PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
    )
    pprint(response)
    return aws_password


def aws_delete_user(aws_profile_name):
    iam.delete_login_profile(
        UserName=aws_profile_name
    )
    iam.detach_user_policy(
        UserName=aws_profile_name,
        PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
    )
    response = iam.delete_user(
        UserName=aws_profile_name
    )
    pprint(response)


print("Account loeschen oder erstellen?")
answer = input("1=erstellen, 2= loeschen: ")
if answer == "1":
    task = "create"
elif answer == "2":
    task = "delete"
else:
    print("Keine Antwort Gueltig. Beende.")
    sys.exit()

for i in range(1, anz_accounts + 1):
    if i < 10:
        aws_profile_name = "cbc-training-" + "0" + str(i)
    else:
        aws_profile_name = "cbc-training-" + str(i)

    session = boto3.session.Session(profile_name=aws_profile_name)
    s3 = session.resource('s3')
    iam = session.client('iam')
    print("Hallo Ich bin im Account ", aws_profile_name)
    if task == "create":
        if not aws_check_user(aws_profile_name):
            aws_password = aws_create_user(aws_profile_name)
            print("User erstellt")
            dic_pass.update({aws_profile_name: aws_password})
        else:
            print("User exisistiert bereits")
    elif task == "delete":
        if aws_check_user(aws_profile_name):
            aws_delete_user(aws_profile_name)
            print("User entfernt")
        else:
            print("User exisitert nicht. Gehe zum nachsten")
if dic_pass:
    print("Passwortliste: ")
    for key in dic_pass:
        print("Account: ", key, "     Passwort: ", dic_pass[key])
