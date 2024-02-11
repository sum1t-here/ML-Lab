class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

        @property
        def age(self):
            return self._age
        
        @age.setter
        def age(self, new_age):
            self._age = new_age

        @age.deleter
        def age(self):
            print("Deleting age ....")
            del self._age
        
person = Person("Hulk", 28)

print(person._age)
# 28
person._age = 30
print(person._age)
# 30
del person._age
print(person._age)