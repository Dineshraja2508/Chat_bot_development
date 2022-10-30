#from email.message import EmailMessage
#import ssl
#import os
import smtplib
print("PLease Enter the emailid :")
ab=input()

fromaddr = 'dannadurai@denodo.com'
toaddrs  = ab
msg = "www.askpython.com/python-modules/python-pywhatkit-send-whatsapp-messages"
subject="sample mail"
username = 'dannadurai@denodo.com'
password = 'Tiger@5678'
message = 'Subject: {}\n\n{}'.format(subject,msg)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddrs, message)
server.quit()
print("Mail sent")