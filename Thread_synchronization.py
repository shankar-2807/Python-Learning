from threading import Thread, Lock
import time


def deposit(amt):
    Lock.acquire()
    global balance
    balance = balance + amt
    print("deposite: ", balance)
    Lock.release()

def withdraw(amt):
    Lock.acquire()
    global balance
    time.sleep(1)
    balance = balance - amt
    print("withdraw:", balance)
    Lock.release()


global balance
balance = 10000

global lock
lock = Lock()

t1 = Thread(name="t1", target=deposit, args=(5000,))
t2 = Thread(name="t2", target=withdraw, args=(3000,))

t1.start()
t2.start()


   
