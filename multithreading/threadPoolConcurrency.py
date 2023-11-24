from concurrent.futures import ThreadPoolExecutor
import threading

def task(n):
    print(f"Processing {n}")
    print(f"Accessing thread: {threading.get_ident()}")
    print(f"Thread Executed: {threading.current_thread().name}")

def main():
    print("Starting ThreadPoolExecutor")
    executor = ThreadPoolExecutor(max_workers=3)
    future = executor.submit(task, (2))
    future = executor.submit(task, (3))
    future = executor.submit(task, (4))
    print("All tasks complete")

if __name__ == "__main__":
    main()
