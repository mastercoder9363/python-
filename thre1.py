import threading
import time

def func1():
    for x in range(0, 10):
        time.sleep(0.2)
        print(x)

def func2():
    for x in range(0, 20):
        time.sleep(0.2)
        print(x)


t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)


t1.start()
t2.start()