from multiprocessing import Process
import time

# Function 1: Print numbers
def print_numbers():
    for i in range(5):
        print(f"[Numbers] {i}")
        time.sleep(1)

# Function 2: Print letters
def print_letters():
    for c in ['A', 'B', 'C', 'D', 'E']:
        print(f"[Letters] {c}")
        time.sleep(1)

if __name__ == "__main__":
    # Create two processes
    p1 = Process(target=print_numbers)
    p2 = Process(target=print_letters)

    # Start processes
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()

    print("Both processes finished!")