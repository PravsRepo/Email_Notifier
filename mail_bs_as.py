
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging




class Send_mail:

    def __init__(self, **kwargs) -> None:
        """Initiated"""
        print('Send_mail Initiated')
        self.log_filename = kwargs['log_filename']
        self.log_level = kwargs['log_level']
        self.date_format = kwargs['date_format']
        self.log_format = kwargs['log_format']
        logging.basicConfig(filename=self.log_filename, format=self.log_format,
                            level=self.log_level, datefmt=self.date_format)
        self.log = kwargs['mail_log']
        self.log.info("All variable are Initiated")

# Send mail to the LEAP team
    def send_mail_before_session(self,mail_data):
        if mail_data == None:
            email_address = os.environ.get('Email_Address')
            email_password = os.environ.get('Email_Password')
            receiver_email = ["praveenpze7897@gmail.com"]
            # receiver_email = ["hemarani@leap.respark.iitm.ac.in", "usha@leap.respark.iitm.ac.in"]
            cc_email = ["praveenkumarmech7897@gmail.com"]
            with smtplib.SMTP('smtp.office365.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login(email_address, email_password)

                subject = mail_data['Activity'] + ' & ' + \
                    str(mail_data['Planned/Rescheduled_Start_Date'].date())
                body = f"""
    Note: This is a sample mail for testing the automation(send mail). Kindly give your suggestions.
    Dear Team,\n
    The LEAP program LP201 for the Prince Shri Venkateshwara Padmavathy Engineering College, Chennai, is scheduled on {mail_data['Planned/Rescheduled_Start_Date'].date()}\n
    The session details are mentioned below,\n
    Phase: {mail_data['Phase']}
    Session: {mail_data['Activity']}
    Activity type: {mail_data['Activity_Type']}
    Mode: {mail_data['Mode']}
    Duration: {mail_data['Duration']}
    Responisibility: {mail_data['Responsibilities']}
    \nThanks, and Regards,
    Praveenkumar"""

                message = MIMEMultipart()
                message['From'] = email_address
                message['To'] = ', '.join(receiver_email)
                message['Cc'] = ', '.join(cc_email)
                message['Subject'] = subject
                message.attach(MIMEText(body))
                smtp.sendmail(email_address, receiver_email +
                            cc_email, msg=message.as_string())
        else:
            print("There is no session today")

    # Send mail after the session
    def send_mail_as(self):
        pass







