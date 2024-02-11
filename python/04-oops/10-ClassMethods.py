class Person:
    total_per = 0

    def __init__(self, name, age):
        self.name = name
        Person.total_per += 1

    # class variable cls
    @classmethod
    def create_person(cls, name, age):
        return cls(name,age)
    
    @staticmethod
    def inc_age(age):
        return age+5
        

person1 = Person.create_person("Natasha", 23)
person2 = Person.create_person("Wanda", 23)

print(Person.total_per) # 2
print(f"{person2.inc_age(32)}") # 37