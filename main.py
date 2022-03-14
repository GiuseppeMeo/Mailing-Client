import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
""" 
For testing and security purposes credentials have not been used as 
this will be publicly available
"""
server = smtplib.SMTP('smtp.gmail.com', 25) #running on port 25

server.ehlo() # start process

with open('password.txt', 'r') as f:
    password = f.read()

server.login('youremail@mail.com', password)

msg = MIMEMultipart()
msg['From'] = 'from@mail.com'
msg['To'] = 'to@mail.com'
msg['Subject'] = 'this is a test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))
filename = 'kali.jpeg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('to@mail.com','from@mail.com', text)


