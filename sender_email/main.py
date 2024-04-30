import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from alert_notifications_api.models.notification_dto import NotificationDTO

SENDER_EMAIL = "usertest@gmail.com"
SUBJECT = "Promo from your real state company :)"
PASSWORD = "Dante Aligerry" #os.environ["EMAIL_PASSWORD"]
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587 # Standard SMTP port


def send_email(email_details: NotificationDTO):

    email_message = MIMEMultipart()
    email_message['From'] = SENDER_EMAIL
    email_message['To'] = email_details.customer_email
    email_message['Subject'] = SUBJECT
    email_message.attach(MIMEText(email_details.offer_message, 'plain'))

    print(f"Email sent to {email_details.customer_email}!")
    return f"Email sent to {email_details.customer_email}!"


    # with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    #     server.starttls()
    #     server.login(SENDER_EMAIL, PASSWORD)  
    #     server.send_message(email_message)


# def main():
#     receiver_email = 'herranmolano@gmail.com'  # Cambia 'recipient@example.com' a la dirección de correo del destinatario
#     subject = 'Prueba de correo electrónico'
#     message = 'Hola, este es un mensaje de prueba enviado desde Python.'

#     send_email(receiver_email, subject, message)


# if __name__ == "__main__":
#     main()

