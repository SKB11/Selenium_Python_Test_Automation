# import os
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import configparser

# class ConfigParser:
#     def __init__(self, config_file_path):
#         self.config_file_path = config_file_path
#         self.config = configparser.ConfigParser()
#         self.config.read(self.config_file_path)

#     def get_value(self, section, key):
#         try:
#             return self.config.get(section, key)
#         except (configparser.NoSectionError, configparser.NoOptionError):
#             return None

# class EmailUtility:
#     def __init__(self, config_file_path='config/config.ini'):
#         self.config_parser = ConfigParser(config_file_path)
#         self.smtp_server = os.environ.get('EMAIL_SMTP_SERVER')
#         self.smtp_port = os.environ.get('EMAIL_SMTP_PORT')
#         self.username = os.environ.get('EMAIL_USERNAME')
#         self.password = os.environ.get('EMAIL_PASSWORD')
#         self.sender = os.environ.get('EMAIL_SENDER')

#     def send_email(self, subject, body, recipients):
#         if self.smtp_server and self.smtp_port and self.username and self.password and self.sender:
#             message = MIMEMultipart()
#             message['From'] = self.sender
#             message['To'] = ', '.join(recipients)
#             message['Subject'] = subject
#             message.attach(MIMEText(body, 'plain'))

#             try:
#                 smtp = smtplib.SMTP(self.smtp_server, self.smtp_port)
#                 smtp.starttls()
#                 smtp.login(self.username, self.password)
#                 smtp.sendmail(self.sender, recipients, message.as_string())
#                 smtp.quit()
#                 print("Email sent successfully!")
#             except Exception as e:
#                 print("Failed to send email:", str(e))
#         else:
#             print("Email configuration values are missing or incomplete.")

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import configparser

class ConfigParser:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_path)

    def get_value(self, section, key):
        try:
            return self.config.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return None

class EmailUtility:
    def __init__(self, config_file_path='config/config.ini'):
        self.config_parser = ConfigParser(config_file_path)
        self.smtp_server = os.environ.get('EMAIL_SMTP_SERVER')
        self.smtp_port = os.environ.get('EMAIL_SMTP_PORT')
        self.username = os.environ.get('EMAIL_USERNAME')
        self.password = os.environ.get('EMAIL_PASSWORD')
        self.sender = os.environ.get('EMAIL_SENDER')

    def send_email(self, subject, body, recipients, attachments=None):
        if self.smtp_server and self.smtp_port and self.username and self.password and self.sender:
            message = MIMEMultipart()
            message['From'] = self.sender
            message['To'] = ', '.join(recipients)
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            if attachments:
                for attachment in attachments:
                    with open(attachment, 'rb') as file:
                        attach = MIMEApplication(file.read(), Name=os.path.basename(attachment))
                    attach['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment)}"'
                    message.attach(attach)

            try:
                smtp = smtplib.SMTP(self.smtp_server, self.smtp_port)
                smtp.starttls()
                smtp.login(self.username, self.password)
                smtp.sendmail(self.sender, recipients, message.as_string())
                smtp.quit()
                print("Email with attachments sent successfully!")
            except Exception as e:
                print("Failed to send email:", str(e))
        else:
            print("Email configuration values are missing or incomplete.")
