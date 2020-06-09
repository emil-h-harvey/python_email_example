import atexit
from smtpd import SMTPServer, DebuggingServer
import asyncore
import smtplib
from multiprocessing import Process
import email.utils
from email.mime.text import MIMEText

DEFAULT_PORT = 1028

def send_mail(
    sender, sender_email, 
    recipient, recipient_email, 
    subject, message):
    
    with smtplib.SMTP("localhost", DEFAULT_PORT) as connection:
        msg = MIMEText(message)
        msg['To'] = email.utils.formataddr(('Recipient', recipient_email))
        msg['From'] = email.utils.formataddr(('Author', sender_email))
        msg['Subect'] = subject
        msg["Body"] = message
        connection.sendmail(sender_email, [recipient_email], msg.as_string())


def start_server():
    server = DebuggingServer(('localhost', DEFAULT_PORT), None)
    asyncore.loop()


def stop_server():
    server_process.terminate()


# Set up a local email server on DEFAULT_PORT
server_process = Process(target=start_server)
server_process.start()
atexit.register(stop_server)
# Set up a connection to default server
#connection = smtplib.SMTP("localhost", DEFAULT_PORT)
