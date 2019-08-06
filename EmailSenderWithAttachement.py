#Used for actually sending the email
import smtplib

#Used for the email payload
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Importing the actual scrapper
import Ebay_Scrapper

#Will be used for sending the data
import datetime
date = datetime.datetime.now()
data_today = (date.strftime("%A")+" "+date.strftime("%B")+" "+date.strftime("%d")+" "+date.strftime("%Y"))


def main():
    fromaddr = "EMAIL FROM"
    toaddr = "EMAIL TO"

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Here is your Data for the Day - Python WebScrapper "

    body = "Attached you will find the csv file for", data_today

    #Body of the email
    msg.attach(MIMEText(body, 'plain'))

    
    #Getting the file that you want to send
    filename = "output.csv"
    attachment = open("output.csv", "r")

    
    #
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    
    #Starting local server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    #Change to email password (for the fromaddr)
    server.login(fromaddr, "CHANGE ME")
    text = msg.as_string()
    
    #Sending the email
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
