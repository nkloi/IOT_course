import threading
import time

# Function for thread 1
def task1():
    for i in range(5):
        print(f"Task 1 - Count {i}")
        time.sleep(1)

# Function for thread 2
def task2():
    for i in range(5):
        print(f"Task 2 - Count {i}")
        time.sleep(1.5)

# Create threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("All tasks completed")