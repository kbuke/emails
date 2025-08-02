import smtplib # creates an smtp server that allows emails
from email.message import EmailMessage # Python's built in 
from dotenv import load_dotenv
import os

email = EmailMessage() # this is our email object

load_dotenv() # load environment variables from .env file
env_email = os.getenv("my_email")
env_password = os.getenv("my_password")

# create email key-value pairs
email["from"] = "Kaan Buke"
email["to"] = "kbuke1301@gmail.com"
email["subject"] = "You won $1,000,000!!!!"

email.set_content("I am a Python Master") # what's the content of email

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp: #this is specific for email providers
    smtp.ehlo() # part of protocal of smtp
    smtp.starttls() # an encryption mechanism to connect securely to server
    smtp.login(env_email, env_password) # login to server
    smtp.send_message(email)
    print("all good boss")