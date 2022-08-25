from email import message
import os
import random
import smtplib

def automatic_email():
    user = input("Enter your Name >>: ")
    email = input("Enter your Email >>: ")
    message = (f"Dear {user}, welcome to Nimish Programming")

    s =smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login("testnimishapp@gmail.com","kwoixotyjxunostq")
    s.sendmail("&&&&&&&",email,message)
    print("Email Sent")

automatic_email()