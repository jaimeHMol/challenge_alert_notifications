from alert_notifications_api.models.notification_dto import NotificationDTO
from sender_email.main import send_email


def test_send_email():
    """ Test the dummy email sent """
    email_details = NotificationDTO(
        customer_email="user_test@hotmail.com",
        email=True,
        customer_cellphone=3445556677,
        sms=False,
        offer_message="Test body email"
    )

    response = send_email(email_details)
    assert response == f"Email sent to {email_details.customer_email}!"
