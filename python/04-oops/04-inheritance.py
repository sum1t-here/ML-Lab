class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"Sound by {self.name} is {self.sound}")

class Dog(Animal):
    def __init__(self,name,sound,breed):
        super().__init__(name,sound) # initial method of Animal class
        # super -> initialise the parent class
        self.breed = breed

    def wag_tail(self):
        print(f"{self.name} is wagging its tail")

    
lion = Animal("Simba","roar")
german_shepherd = Dog("buddy", "woof", "german shepherd")

lion.make_sound()
# Sound by Simba is roar
german_shepherd.wag_tail()
# buddy is wagging its tail