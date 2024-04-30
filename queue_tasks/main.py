import queue
import threading
import time
from typing import Dict, List

from alert_notifications_api.models.notification_dto import NotificationDTO

task_queue = queue.Queue()
counter = 0

def process_dummy_task(customer):
    """Function that simulates a task"""
    print(f"Processing dummy task for customer {customer}")
    time.sleep(1)
    print(f"Dummy task for customer {customer} completed")


def worker(q):
    """ Worker that has the logic to process tasks, especially for notifications. """

    global counter
    while True:
        notification: NotificationDTO = q.get() # Obtains a task from the queue
        if notification.dummy:
            process_dummy_task(notification.customer_email) # Process the task
            counter += 1
        else:
            if notification.email:
                counter += 1
            if notification.sms:
                counter += 1
        q.task_done() # Marks the task as completed on the queue


def queue_notification_task(tasks: List[NotificationDTO]) -> Dict[str, str]:
    """ Custom method queue a notification to be delivered. """
 
    # Creates and instantiates several threads that simulates workers to process the tasks
    for _ in range(len(tasks)):
        t = threading.Thread(target=worker, args=(task_queue,))
        t.daemon = True # Threads will run in background
        t.start()

    # Put tasks to the queue
    for task in tasks:
        task_queue.put(task)

    # Wait for all the tasks to finish
    task_queue.join()

    global counter
    local_count = counter
    counter = 0
    return {"message": f"All the {local_count} tasks were queued."}


def queue_completed() -> bool:
    """ Returns if all the items in the queue were completed, otherwise the queue will
    still be processing tasks. """
    print(f"Actual size of the queue: {task_queue.qsize()}")
    return task_queue.empty()
