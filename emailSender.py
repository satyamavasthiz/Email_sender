import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart

def sendEmail(senderEmail, senderPassword, receiverEmail, subject, body): # FUNCTION CREATE TO SEND EMAIL
    message = MIMEMultipart()
    message['From'] = senderEmail
    message['To'] = receiverEmail
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(senderEmail, senderPassword)
        server.sendmail(senderEmail, receiverEmail,message.as_string)
        print(f"Email sent successfully to {receiverEmail}")
        server.quit()
        
    except Exception as e:
        print(f"Failed to send Email. Error: {e}")
        
senderEmail = ""
senderPassword = ""
receiverEmail = ""
subject = ""
body = ""

sendEmail(senderEmail, senderPassword, receiverEmail, subject, body)
        