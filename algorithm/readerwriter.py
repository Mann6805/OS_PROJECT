import threading
import time
import random

mutex = threading.Semaphore(1)  
db = threading.Semaphore(1)  
reader_count = 0
iterations = 0 
def Reader():
    global reader_count, iterations
    while iterations < 10: 
        mutex.acquire()  
        reader_count += 1  
        if reader_count == 1: 
            db.acquire()  
        mutex.release() 
        print("Reading...")
        time.sleep(random.uniform(0.5, 1.5))
        
        mutex.acquire()  
        reader_count -= 1  
        if reader_count == 0: 
            db.release() 
        mutex.release()  
        
        time.sleep(random.uniform(0.5, 1.5))
        iterations += 1 

def Writer():
    global iterations
    while iterations < 10:  
        time.sleep(random.uniform(0.5, 3.5))
        db.acquire() 
        print("Writing...")
        time.sleep(random.uniform(0.5, 1.5))
        db.release()
        iterations += 1  

reader_thread = threading.Thread(target=Reader)
writer_thread = threading.Thread(target=Writer)

reader_thread.start()
writer_thread.start()

reader_thread.join()
writer_thread.join()