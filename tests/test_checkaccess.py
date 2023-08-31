# import time
# import pytest
# from utils.email_utils import EmailUtility

# def test_email_setup():
#     # Configure email utility
#     email_utility = EmailUtility('config/config.ini')

#     # Email details
#     subject = "Test Email"
#     body = "This is a test email to check if email setup is working."
#     recipients = ['internskb21@gmail.com']

#     # Send the email
#     email_utility.send_email(subject, body, recipients)

#     # Sleep to allow time for email to be sent (optional)
#     time.sleep(5)

#     # Check if email was sent successfully (you can add more advanced checks here)
#     # For now, we'll assume that if no exceptions were raised during send_email,
#     # the email was sent successfully.
    
#     # If you want to perform more advanced checks, you can consider using email APIs or libraries.
import time
import pytest
from utils.email_utils import EmailUtility

def test_email_setup():
    # Configure email utility
    email_utility = EmailUtility('config/config.ini')

    # Email details
    subject = "Test Email with Attachments"
    body = "This is a test email to check if email setup with attachments is working."
    recipients = ['internskb21@gmail.com']

    # Attach files
    attachments = ['C:\\Users\\Sharddha K B\\Desktop\\Project\\Report\\mini-project\\HerbId REPORT(fINAL).docx']


    # Send the email with attachments
    email_utility.send_email(subject, body, recipients, attachments)

    # Sleep to allow time for email to be sent (optional)
    time.sleep(5)

    # Check if email was sent successfully (you can add more advanced checks here)
    # For now, we'll assume that if no exceptions were raised during send_email,
    # the email was sent successfully.
    
    # If you want to perform more advanced checks, you can consider using email APIs or libraries.
