from threading import Thread
import time

class Mythread(Thread):
    def __init__(self, name, str):
        Thread.__init__(self)
        self.name = name
        self.str = str

    def run(self):
        for i in self.str:
            print(i)
            time.sleep()


t1 = Mythread("Thread1", "1111111111")
t2 = Mythread("Thread2", "2222222222")
t1.start()
t1.join(5)

t2.start()
t2.join()


