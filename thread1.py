# write a program in python to print 1 to 10 no and ten letters concurrently
import threading
import time

def print_number(name):
    for i in range(1, 11):
        print(name, i)
        time.sleep(1)
        
def print_letters(name):
    ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for l in ls:
        print(name, l)
        time.sleep(1)    
        
thread1 = threading.Thread(target=print_number, args=("Numbers",))
thread2 = threading.Thread(target=print_letters, args=("Letters",))
thread1.start()
thread1.join()
thread2.start()
thread2.join()
print("All tasks are executed")
