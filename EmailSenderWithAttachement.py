import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import Ebay_Scrapper
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

    msg.attach(MIMEText(body, 'plain'))

    filename = "output.csv"
    attachment = open("output.csv", "r")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "CHANGE ME")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()