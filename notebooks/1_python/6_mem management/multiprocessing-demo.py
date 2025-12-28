import multiprocessing
import time

def test_func1():
    print("do something")
    print("sleep for 1 sec")
    time.sleep(1)
    print("done with something")

if __name__ == '__main__':
    start = time.perf_counter()
    
    p1 = multiprocessing.Process(target=test_func1)
    p2 = multiprocessing.Process(target=test_func1)
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    end = time.perf_counter()
    print(f"The program is finished in {round(end-start, 2)} seconds.")