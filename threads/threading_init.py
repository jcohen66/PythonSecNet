import threading


def myTask():
    print(f"Hello world: {threading.current_thread().name}")


myFirstThread = threading.Thread(target=myTask)
myFirstThread.start()
