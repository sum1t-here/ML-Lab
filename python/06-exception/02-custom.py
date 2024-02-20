class coldDrinkException(Exception):
    def __init__ (self, message="Sorry, we only serve hot beverages"):
        self.message = message
        super().__init__(self.message)

def serve_hot_drinks(drink_temp):
    if drink_temp == 'cold':
        raise coldDrinkException()
    else:
        print("Enjoy Your coffee")


try:
    serve_hot_drinks('cold')
except coldDrinkException as e:
        print(e)

# Sorry, we only serve hot beverage
        
try:
    serve_hot_drinks(1)
except coldDrinkException as e:
        print(e)

# Enjoy Your coffee