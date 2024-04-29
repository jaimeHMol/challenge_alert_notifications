from sender_email.main import send_email


def test_send_email():
    receiver_email = 'herranmolano@gmail.com'  # Cambia 'recipient@example.com' a la dirección de correo del destinatario
    subject = 'Prueba de correo electrónico'
    message = 'Hola, este es un mensaje de prueba enviado desde Python.'

    response = send_email(receiver_email, subject, message)
    assert response == f"Email sent to {receiver_email}!"
