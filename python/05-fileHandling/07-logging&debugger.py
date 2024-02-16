# Logging is a technique used in software development that allows developers to see into their application’s runtime process
# Error Reporting / Debugging -> Exceptions logged detailing where it occurred, timestamped, input/output data if possible, user information etc

import logging

# Level of logging
# debug
# info
# warning
# error
# critical

logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')

logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")

# 2024-02-16 19:37:23,657 - DEBUG - This is a debug message
# 2024-02-16 19:37:23,657 - INFO - This is a info message
# 2024-02-16 19:37:23,657 - WARNING - This is a warning message
# 2024-02-16 19:37:23,657 - ERROR - This is a error message
# 2024-02-16 19:37:23,657 - CRITICAL - This is a critical message

# def sqr_num(num):
#     try:
#         result = num**2
#         logging.info(f"square of {num} is {result}")
#         return result
#     except Exception as e:
#         logging.error("Square cannot be found")

# if __name__ == "__main__":
#     numbs = [1,2,3,4,5,'s']

#     for num in numbs:
#         try:
#             sq_result = sqr_num(num)
#             logging.debug("Succesfully Implemented")
#         except Exception as e:
#             logging.warning(f"Couldnot process {num}")

# 2024-02-16 22:42:44,474 - INFO - square of 1 is 1
# 2024-02-16 22:42:44,474 - DEBUG - Succesfully Implemented
# 2024-02-16 22:42:44,474 - INFO - square of 2 is 4
# 2024-02-16 22:42:44,474 - DEBUG - Succesfully Implemented
# 2024-02-16 22:42:44,474 - INFO - square of 3 is 9
# 2024-02-16 22:42:44,474 - DEBUG - Succesfully Implemented
# 2024-02-16 22:42:44,474 - INFO - square of 4 is 16
# 2024-02-16 22:42:44,474 - DEBUG - Succesfully Implemented
# 2024-02-16 22:42:44,474 - INFO - square of 5 is 25
# 2024-02-16 22:42:44,474 - DEBUG - Succesfully Implemented
# 2024-02-16 22:46:57,444 - ERROR - Square cannot be found
# 2024-02-16 22:46:57,444 - DEBUG - Succesfully Implemented
            
# debugging
            
import pdb
# n -> next, s -> step, c -> count, q -> quit n

def sqr_num(num):
    try:
        result = num**2
        pdb.set_trace()
        return result
    except Exception as e:
        print("Square cannot be found")

if __name__ == "__main__":
    numbs = [1,2,3,4,5,'s']

    for num in numbs:
        try:
            sq_result = sqr_num(num)
            print("Succesfully Implemented")
        except Exception as e:
            print(f"Couldnot process {num}")
