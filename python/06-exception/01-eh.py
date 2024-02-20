try:
    number = input('Enter a number')
    number * number
except Exception as e:
    print(f"Error: {e}")

def med(a,b):
    try:
        c = ((a+b)//(a-b))
    except ZeroDivisionError:
        print('(a-b) results 0')
    else:
        print(c)
    finally:
        print("This method will run always")
    
print(med(3,4))
# -7
# This method will run always
# None
print(med(2,2))
# (a-b) results 0
# This method will run always
# None