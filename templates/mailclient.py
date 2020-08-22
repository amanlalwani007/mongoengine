import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server=smtplib.SMTP('smtp.gmail.com',25)
server.ehlo()
#to start a process
msg=MIMEMultipart()
msg['from']='amanlalwani'
msg['to']='aman.lalwani_cs16@gla.ac.in'
msg['subject']='just a text'

msg.attach(MIMEText("this is a test email",'plain'))
filename="/home/am.lalwani/PycharmProjects/Basic/templates/aman.jpg"
attachment=open(filename,'rb')

p=MIMEBase('application','octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment;filename={filename}')
msg.attach(p)
text=msg.as_string()

server.sendmail("amanlalwani0807@gmail.com","aman.lalwani_cs16@gla.ac.in",msg)


