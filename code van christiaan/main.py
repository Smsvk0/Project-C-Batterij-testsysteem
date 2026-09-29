import threading
import time
from test_1 import model
from test_2 import operator

print('Main was started')

i = 0

class workers:
    def model():
        b=2
        print('Value a =', b)
        time.sleep(1)
    
    def operator():
        print('This operator works')
        time.sleep(1)

class start:
    def loop():
        i = 0
        t1.start()
        t2.start()
        while i < 414:
    
            i += 1
            a = i
            print(i)
               
            print('In the loop')
            
            
            t1.join()
            #t1.interrupt()
            #t1.join()
            #t1.interrupt()
            t2.join()
            #t2.interrupt()
    
            print('t1 was started')
#t2 = Thread(target=operator)
t1 = threading.Thread(target=model)
t2 = threading.Thread(target=operator)
starter = start.loop()
start()

