
# Import smtplib for the actual sending function
import smtplib
'''
# Import the email modules we'll need
from email.mime.text import MIMEText


# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open("/Desktop/jazz/textfile.txt", 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = "amos.ro7@gmail.com"
msg['To'] = "amos.ro7@gmail.com"


msg="""From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""
# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()
'''

sender = 'amos.ro7@gmail.com'
receivers = ['amos.ro7@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""



print"here1"
smtpObj = smtplib.SMTP('Smtp.gmail.com')
print("here2")
smtpObj.sendmail(sender, receivers, message)         
print "Successfully sent email"
