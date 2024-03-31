import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import requests
import os


def send_mail(recipient_email, subject, message):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'pricepulseindia@gmail.com'
    password = 'vybgifphaalzmlul'

    # Download the image from the URL and save it locally
    response = requests.get("https://t3.ftcdn.net/jpg/02/91/52/22/360_F_291522205_XkrmS421FjSGTMRdTrqFZPxDY19VxpmL.jpg")
    cwd = os.getcwd()
    image_path = os.path.join(cwd, 'PIH_Pune_Price_Pulse', 'static', 'assets', 'img', 'image.jpg')
    with open(image_path, 'wb') as f:
        f.write(response.content)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))



    with open(image_path, 'rb') as image_file:
        image = MIMEImage(image_file.read(), name='image.jpg')
        msg.attach(image)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")

# Example usage of the send_mail function
