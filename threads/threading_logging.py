import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)-10s) %(message)s')

def thread(name):
    logging.debug(f"Thread {name} starting")
    time.sleep(2)
    print(f"{name} {time.ctime(time.time())}")
    logging.debug(f"Thread {name} finishing")

def check_state(thread):
    if thread.is_alive():
        print(f"Thread {thread.name} is Alive")
    else:
        print(f"Thread {thread.name} is NOT Alive")

th1 = threading.Thread(name="Thread 1", target=thread, args=("Thread 1",))
th2 = threading.Thread(name="Thread 2", target=thread, args=("Thread 2",))
th1.setDaemon(True)
th1.start()
th2.start()
check_state(th1)
check_state(th2)
while(th1.is_alive()):
    logging.debug("Thread is executing...")
    time.sleep(1)
th1.join()
th2.join()
