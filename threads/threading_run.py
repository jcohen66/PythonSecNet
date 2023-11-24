import threading

class MyThread(threading.Thread):
    def __init__(self, message):
        threading.Thread.__init__(self)
        self.message = message
    def run(self):
        print(self.message)


threads = []

def test():
    for num in range(10):
        thread = MyThread(f"I am the {num} thread")
        thread.name = f"Thread {num}"
        thread.start()
        threads.append(thread)
    # Wait for all threads to complete
    for thread in threads:
        # Block until the thread terminates
        thread.join(timeout=1)

if __name__ == "__main__":
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=5))