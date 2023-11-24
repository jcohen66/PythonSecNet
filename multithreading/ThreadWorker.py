import threading

class ThreadWorker(threading.Thread):
    def __init__(self):
        # Call the parent constructor
        super(ThreadWorker,self).__init__()


    def run(self):
        # Override the run() method of the parent class
        self.target(*self.args)
        for i in range(10):
            print(f"{self.name}: {i}")
