import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER_EMAIL = "herranmolano@gmail.com"
PASSWORD = "Mephisto" #os.environ["EMAIL_PASSWORD"]
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587 # Standard SMTP port


def send_email(receiver_email: str, subject: str, message: str):

    email_message = MIMEMultipart()
    email_message['From'] = SENDER_EMAIL
    email_message['To'] = receiver_email
    email_message['Subject'] = subject
    email_message.attach(MIMEText(message, 'plain'))

    print(f"Email sent to {receiver_email}!")
    return f"Email sent to {receiver_email}!"
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

