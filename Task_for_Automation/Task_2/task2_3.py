import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = input("Enter you Email Address:  ")
print()
toaddr = input("Enter Email Address of receiver:  ")
print()
psw = getpass.getpass(prompt="Enter your password.. ")
print()
#Create the MIMEMultipart message object and load it with appropriate headers for From, To,and Subject fields
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = input("Enter the subject:  ")
print()
body = input("Enter the text you want to send:  ")
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, psw)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()