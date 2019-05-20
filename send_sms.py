""" This is my wedding invitation script since
    I couldn't find a free alternative to send mass individualized text messages"""
import smtplib
import csv
import os
import re
import sys
import time

os.system('cls')

#these are the major cellphone companies, I need these to create the gateway for phone numbers
SMSGATEWAYS = [
    'tmomail.net',             #tmobile
    'mms.att.net',             # at&t
    'vtext.com',               # verizon
    'page.nextel.com',         # sprint
    'sms.mycricket.com',       # cricket
    'vmobl.com',               # virgin mobile US
    'sms.myboostmobile.com'    # boost mobile
    ]

def readcsv():
    """this function reads a CSV of guest list returns
    a list of names and the associated phone numbers"""
    phone_numbers = []
    try:
        #with open('ENTER CSV PATH ON YOUR COMPUTER') as csv_file:
        with open('C:\\Users\\mhammond4\\Desktop\\spexport.csv') as csv_file:
            csv_v = csv.reader(csv_file, delimiter=',')
            next(csv_v)
            for i in csv_v:
                name = i[3] + ' ' + i[4]
                number = ''.join(re.findall(r'\d+', i[12]))
                phone_numbers.append([name, number if number[0] != '1' else number[1:]])
    except FileNotFoundError:
        print("\nERROR: CSV could not be found please verify path")

    return phone_numbers

def createnumbers(gate, numbers):
    """this function takes the list of possible gateways
    and each gateway is appended to each phone number
    the function then calls send text function with each
    permutation of gateway since we don't know the phone company for each number
    a timestamp is also printed with each name for review"""

    for name, num in numbers:
        for i in gate:
            contact = num +'@'+ i
            sendtext(contact)

        print(name, 'received message at:', time.ctime())
        print('\n')

def sendtext(contact):
    """this function uses my email as the server to send
    the email to phone numbers with the specified message
    google has a LESS SECURE APPS safety feature that must be turned off"""

    email = environ.get('username')
    password = environ.get('password')

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)

        
        msg = " " #INSERT MESSAGE HERE
        server.sendmail(email, contact, msg)
    except smtplib.SMTPAuthenticationError as e:
        print("\nERROR: Turn ON google's 'Allow Less Secure Apps' for your email account\n\n", e)
        sys.exit(1)

if __name__ == "__main__":
    createnumbers(SMSGATEWAYS, readcsv())
