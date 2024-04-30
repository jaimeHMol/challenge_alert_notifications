from alert_notifications_api.models.notification_dto import NotificationDTO
from sender_sms.main import send_sms


def test_send_sms():
    """ Test the dummy sms sent """
    sms_details = NotificationDTO(
        customer_email="user_test@hotmail.com",
        email=False,
        customer_cellphone=3445556677,
        sms=True,
        offer_message="Test body sms"
    )

    response = send_sms(sms_details)
    assert response == f"Sms sent to {sms_details.customer_cellphone}!"
