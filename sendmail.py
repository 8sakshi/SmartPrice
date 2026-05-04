import os
import smtplib

def sendmail(msg, recipients ):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()


    # email and the 16-digit App Password here
    server.login(os.getenv("EMAIL_USER"), os.getenv('EMAIL_PASSWORD'))
    server.sendmail(os.getenv("EMAIL_USER"), to_addrs=recipients, msg=msg)

    print("Sent Mail!")
    server.quit()
