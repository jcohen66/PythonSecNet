from concurrent.futures import ProcessPoolExecutor, as_completed
import os

def task():
    print(f"Executing our task on process {os.getpid()}")

def main():
    executor = ProcessPoolExecutor(max_workers=3)
    task1 = executor.submit(task)
    task2 = executor.submit(task)

if __name__ == "__main__":
    main()