from threading import Thread
import time


def listen():
    i = 0
    while True:
        i += 1
        print(i)
        time.sleep(3)