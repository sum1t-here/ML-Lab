import multiprocessing
import time

# cpu bound operation

def print_num():
        for i in range(5):
                time.sleep(5)
                print(f"print_numbers {i}")

def print_letters():
        for char in 'abcde':
                time.sleep(1)
                print(f"print_letters {char}")

if __name__ == '__main__':
            process1 = multiprocessing.Process(target=print_num)
            process2 = multiprocessing.Process(target=print_letters)

            process1.start()
            process2.start()

            process1.join()
            process2.join()