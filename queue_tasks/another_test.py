import queue
import threading
import time


def worker(q):
    while True:
        item = q.get()
        print(f'Working on {item}')
        time.sleep(2)
        print(f'Finished {item}')
        q.task_done()



def main():
    # q = queue.Queue()

    # # Turn-on the worker thread.
    # # threading.Thread(target=worker, daemon=True).start()
    # for i in range(3):
    #     t = threading.Thread(target=worker, args=(q,))
    #     t.daemon = True
    #     t.start()


    # # Send thirty task requests to the worker.
    # for item in range(30):
    #     q.put(item)

    # # Block until all tasks are done.
    # q.join()
    # print('All work completed')


    from alert_notifications_api.models.notification_preference import \
        NotificationPreference
    from queue_tasks.main import queue_completed, queue_task

    test_tasks = [
        NotificationPreference(notification_preference_id=1, customer_id=1111, dummy=True, email=True, sms=False, created_by="test_user"),
        NotificationPreference(notification_preference_id=2, customer_id=2222, dummy=True, email=True, sms=False, created_by="test_user"),
    ]
    response = queue_task(test_tasks)
    print(response)


if __name__ == "__main__":
    main()


    