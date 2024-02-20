import threading
import time

# only in i/o operation

def print_num():
        for i in range(5):
                time.sleep(5)
                print(f"print_numbers {i}")

def print_letters():
        for char in 'abcde':
                time.sleep(1)
                print(f"print_letters {char}")




thread1 = threading.Thread(target= print_num)
thread2 = threading.Thread(target= print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()