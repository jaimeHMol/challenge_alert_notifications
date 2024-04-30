from alert_notifications_api.models.notification_dto import NotificationDTO

SENDER_CELLPHONE = "1112223344"


def send_sms(sms_details: NotificationDTO):

    sms_message = {}
    sms_message["From"] = SENDER_CELLPHONE
    sms_message["To"] = sms_details.customer_cellphone
    sms_message["Body"] = sms_details.offer_message

    print(f"Sms sent to {sms_details.customer_cellphone}!")
    return f"Sms sent to {sms_details.customer_cellphone}!"
