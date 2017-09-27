#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import datetime
import smtplib
import base64
from six.moves import input
import config
from email.header import Header, decode_header, make_header

# Add a nice helper description
DESCRIPTION = """Send an email using smtp and python. 
SMTP settings can be added on a config.py file inside the same folder of script.
 The subject and email can be set on user input."""
parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument('-t', '--template', help='Custom template file to be used.')
args = parser.parse_args()


def get_subject(subject):
    # subject_base64 = subject.encode('ascii').strip()
    # subject_base64 = base64.encodebytes(bytes(subject)).strip()
    # return "=?UTF-8?B?%s?=" % subject_base64
    subject_content = make_header(decode_header(subject))
    return str(subject_content)

def get_file(template_file):
    try:
        file = open(template_file, 'r')
    except IOError:
        print('Template file does not exist.')
        exit()
    return file

def get_template_file(custom_template):
    if custom_template == None or custom_template == '':
        return config.smtp_template
    else:
        return custom_template

def get_message(subject, mail_to, custom_template):
    file_name = get_template_file(custom_template)
    file = get_file(file_name)
    msg = file.read()
    msg = msg.replace('{{FROM_MAIL}}', config.smtp_mail) \
        .replace('{{FROM_NAME}}', config.smtp_name) \
        .replace('{{SUBJECT}}', subject) \
        .replace('{{TO_MAIL}}', mail_to)
    return msg

def smtp_mail(mail_to, message):
    smtpObj = smtplib.SMTP(config.smtp_address, config.smtp_port)
    smtp_login(smtpObj)
    sendmail(smtpObj, mail_to, message)

def smtp_login(smtp):
    try:
        smtp.login(config.smtp_mail, config.smtp_password)
    except smtplib.SMTPHeloError:
        print('HELO error')
        exit()
    except smtplib.SMTPAuthenticationError:
        print('Could not authenticate on smtp server, please check config file')
        exit()
    except smtplib.SMTPException:
        print('Error while logging on smtp server')
        exit()

def sendmail(smtp, mail_to, message):
    try:
        smtp.sendmail(config.smtp_mail, mail_to, message)
    except smtplib.SMTPRecipientsRefused:
        print('All email recipients were refused. Double-check the mail input')
        exit()
    except smtplib.SMTPHeloError:
        print('HELO error')
        exit()
    except smtplib.SMTPSenderRefused:
        print('The sender email was refused, verify your config parameters')
        exit()
    except smtplib.SMTPDataError:
        print('An error happened while trying to send the email. Try again')
        exit()

def writelog(a):
    f = open("send_log.txt", 'a')
    f.write(a + "\n")
    f.close()


mail = ('c-choi@outlook.com', 'c.cloudy@me.com')
group = {'c-choi@outlook.com': 'group1', 'c.cloudy@me.com': 'group2'}

subject = get_subject(input('Subject: ')) #.encode('utf-8'))

for g in range(len(group)):
    for i in range(1, 10):
        mail_list = mail[g]
        group_list = group[mail_list]
        mail_to = mail_list
        if group_list == "group" + str(i):
            custom_template = "email_template" + str(i) + ".txt"
            message = get_message(subject, mail_to, custom_template) #args.template)
            smtp_mail(mail_to, message)

            writelog('Success sending mail to: '+mail_to+' with ' + custom_template + '-- '+str(datetime.datetime.now()))
            print('Success sending mail to: '+mail_to+' with ' + custom_template + '-- '+str(datetime.datetime.now()))
        else:
            print('Failed sending mail to: ' + mail_to + '-- '+ str(datetime.datetime.now()))