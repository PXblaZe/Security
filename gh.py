from multiprocessing import Process
from time import sleep
def a():
    for i in range(10):
        print('hii')

def b():
    for i in range(10):
        print('hello')
if __name__ == '__main__':
    p1 = Process(target = a)
    p2 = Process(target = b)
    p1.start()
    p2.start()
    p1.join()
    sleep(1)
    p2.join()
