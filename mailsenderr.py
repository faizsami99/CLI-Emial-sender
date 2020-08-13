import argparse
import smtplib
import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def single_mail(info):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = info.email[0]
    with open(info.email[1], "r") as my_file:
        password = my_file.read()
    recievermail = info.email[2]
    with open(info.email[3],"r") as my_file:
        message = my_file.read()
    
    server = smtplib.SMTP(smtp_server,port)
    server.starttls() # Secure the connection
    server.login(sender_email, password)
    server.sendmail(sender_email, recievermail, message)
    print ("send")
    server.quit()

def multiple_mail(info):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = info.Email[0]
    with open(info.Email[1], "r") as my_file:
        password = my_file.read()
    with open(info.Email[2], "r") as my_file:
        i = my_file.read()
        recievermails = i.split("\n")
        recievermails.pop()
    with open(info.Email[3],"r") as my_file:
        message = my_file.read()
    server = smtplib.SMTP(smtp_server,port)
    server.starttls() # Secure the connection
    server.login(sender_email, password)
    for i in recievermails:
        server.sendmail(sender_email, i, message)
        print ("send")
    server.quit()

def single_mail_docu(info):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = info.file[0]
    with open(info.file[1], "r") as my_pass:
        pas = my_pass.read()
        pa = pas.split("\n")
        password = pa[0]
    
    recievermail = info.file[2]
    
    with open(info.file[3], "r") as my_file:
        body = my_file.read()
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recievermail
    message["Subject"] = "Hello"
    message["Bcc"] = recievermail
    
    part = MIMEText(body, "plain")
    message.attach(part)

    filename = info.file[4]

    with open(filename, "rb") as my_document:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(my_document.read())
    
    encoders.encode_base64(part)

    message.attach(part)


    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)
    text = message.as_string()

    server = smtplib.SMTP(smtp_server,port)
    server.starttls() # Secure the connection
    server.login(sender_email, password)
    server.sendmail(sender_email, recievermail, text)

    server.quit()

def multiple_mail_docu(info):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = info.File[0]
    with open(info.File[1], "r") as my_pass:
        pas = my_pass.read()
        pa = pas.split("\n")
        password = pa[0]
    
    with  open(info.File[2], "r") as mails:
        recievermail = mails.read().split("\n")
        recievermail.pop()

    with open(info.File[3], "r") as my_file:
        body = my_file.read()
    
    message = MIMEMultipart()
    message["From"] = sender_email
    #message["To"] = recievermail
    message["Subject"] = "Hello"
    #message["Bcc"] = recievermail
    
    part = MIMEText(body, "plain")
    message.attach(part)

    filename = info.File[4]

    with open(filename, "rb") as my_document:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(my_document.read())
    
    encoders.encode_base64(part)

    message.attach(part)


    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)
    text = message.as_string()

    server = smtplib.SMTP(smtp_server,port)
    server.starttls() # Secure the connection
    server.login(sender_email, password)
    for i in recievermail:
        message["To"] = recievermail
        message["Bcc"] = recievermail
        server.sendmail(sender_email, i, text)

    server.quit()

parser = argparse.ArgumentParser(description="Use to send Emails")

parser.add_argument("-e", "--email", type=str, nargs=4, metavar=("mymail", "mypass", "recievermail", "message"), help="Use to send to single emial")
parser.add_argument("-E", "--Email", type=str, nargs=4, metavar=("mymail", "mypass", "all_email_file", "message"), help="Use to send to multiple email")
parser.add_argument("-f", "--file", type=str, nargs=5, metavar=("mymail", "mypass", "recievermail", "message", "file"), help="Use to send to single email with Document")
parser.add_argument("-F", "--File", type=str, nargs=5, metavar=("mymail", "mypass", "all_email_file", "message", "file"), help="Use to send to multiple email with Document")

args =  parser.parse_args()

if args.email != None:
    single_mail(args)

elif args.Email != None:
    multiple_mail(args)

elif args.File != None:
    multiple_mail_docu(args)

elif args.file != None:
    single_mail_docu(args)