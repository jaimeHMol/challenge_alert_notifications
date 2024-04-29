from alert_notifications_api.models.customer import Customer
from alert_notifications_api.models.notification_preference import \
    NotificationPreference
from queue_tasks.main import queue_completed, queue_notification_task


def test_queue():
    """ Basic test of the implemented queue. """

    # Send two or more tasks
    test_tasks = [
        NotificationPreference(notification_preference_id=1, customer_id=1111, dummy=True, email=True, sms=False, created_by="test_user"),
        NotificationPreference(notification_preference_id=2, customer_id=2222, dummy=True, email=True, sms=False, created_by="test_user"),
    ]
    response = queue_notification_task(test_tasks)

    # test_tasks = [
    #     {"customer_id": 1111, "dummy": True, "email": True, "sms": False},
    #     {"customer_id": 2222, "dummy": True,  "email": False, "sms": True},
    #     {"customer_id": 3333, "dummy": True,  "email": True, "sms": True},
    #     {"customer_id": 4444, "dummy": True,  "email": False, "sms": False},
    # ]

    # test_customer = Customer(customer_id=1111, name="Test Name", created_by="test_user")
    # test_preference = NotificationPreference(notification_preference_id=11, customer_id=test_customer.customer_id, dummy=True, email=True, sms=False, created_by="test_user"),
    # print(f"          🛑🐛🔍DEBUG test_customer: {test_customer}")
    # print(f"          🛑🐛🔍DEBUG test_preference: {test_preference}")

    
    # Confirm tasks received
    assert response == {"message": f"All the {len(test_tasks)} tasks were queued."}

    # Confirm all tasks processed
    assert queue_completed()
