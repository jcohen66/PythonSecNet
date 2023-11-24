"""
Working with processes is very similar to working with threads. The difference is that you need
to use the multithreading module instead of the threading module
"""
import multiprocessing
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(processName)-10s) %(message)s')


def thread(name):
    logging.debug('Starting Process ' + name)
    time.sleep(5)
    print("%s: %s" % (name, time.ctime(time.time())))
    logging.debug('Stopping Process ' + name)


def check_state(process):
    if process.is_alive():
        print(f'Process {process.name} is alive.')
    else:
        print(f'Process {process.name} is not alive.')

if __name__ == '__main__':
    process = multiprocessing.Process(target=thread, args=('MyProcess',))
    process2 = multiprocessing.Process(target=thread, args=('MyProcess2',))
    check_state(process)
    check_state(process2)
    process.start()
    process2.start()
    check_state(process)
    check_state(process2)

