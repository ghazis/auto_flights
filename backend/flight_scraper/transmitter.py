import smtplib
from twilio.rest import Client
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

###Email Library to send simple texts emails. Inputs are sender, password,
### recipient(s), message, subject.

def sendEmail(sndr, pswd, recips, msg, subject, cc=[]):
    email = MIMEMultipart()
    email['From'] = sndr
    email['To'] = ", ".join(recips)
    email['Cc'] = ", ".join(cc)
    email['Subject'] = subject
    email.attach(MIMEText(msg, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(sndr, pswd)
    server.sendmail(sndr, recips, email.as_string())
    server.quit()

def sendSMS(to, frm, msg):
    account = "AC77f746e44960392c3f5d6a244cff8307"
    token = "2ffe18a4881c43044f0f7312d464ec6d"
    client = Client(account, token)
    client.messages.create(to="+1"+to, from_="+1"+frm, body=msg)