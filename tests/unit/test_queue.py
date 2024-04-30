from alert_notifications_api.models.customer import Customer
from alert_notifications_api.models.notification_dto import NotificationDTO
from queue_tasks.main import queue_completed, queue_notification_task


def test_queue():
    """ Basic test of the implemented queue. """

    # Send two or more tasks
    test_tasks = [
        NotificationDTO(offer_message="Test offer.", dummy=True, email=True, customer_email="maximo@hotmail.com", sms=False, customer_cellphone=3112223344),
        NotificationDTO(offer_message="Test offer.", dummy=True, email=False, customer_email="yeison@hotmail.com", sms=True, customer_cellphone=3998887766),
    ]
    response = queue_notification_task(test_tasks)
    
    # Confirm tasks received
    assert response == {"message": f"All the {len(test_tasks)} tasks were queued."}

    # Confirm all tasks processed
    assert queue_completed()
