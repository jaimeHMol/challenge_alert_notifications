import queue
import threading
import time


def process_task(task_number):
    """Function that simulates a task"""
    print(f"Processing task {task_number}")
    time.sleep(2)
    print(f"Task {task_number} completed")

def worker(q):
    while True:
        task_number = q.get()  # Obtains a task from the queue
        process_task(task_number)  # Process the task
        q.task_done()  # Marks the task as completed on the queue

# Creates a queue
task_queue = queue.Queue()

# Creates and instantiates several threads that simulates workers to process the tasks
for i in range(3):
    t = threading.Thread(target=worker, args=(task_queue,))
    t.daemon = True  # Threads will run in background
    t.start()

# Put tasks to the queue
for i in range(5):
    task_queue.put(i)

# Wait for all the tasks to finish
task_queue.join()

print("All the tasks were completed.")
