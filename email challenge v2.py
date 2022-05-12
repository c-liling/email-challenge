# Import modules
import smtplib, ssl
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define the HTML document
# Insert your own tracker here
html = '''
    <html>
        <body>
            <img src="https://pastepixel.com/image/NTqTSnYkYwaMTtCN55Wg.png" alt=""/>
        </body>
    </html>
    '''

# Set up the email addresses and password. Please replace below with your email address and password
email_from = 'youremail@gmail.com'
password = input("Please enter your password: ")
email_to = 'receiver@gmail.com'

# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = f'Test email'

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
email_message.attach(MIMEText(html, "html"))
# Convert it as a string
email_string = email_message.as_string()

# Connect to the Gmail SMTP server and Send Email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email_from, password)
    server.sendmail(email_from, email_to, email_string)