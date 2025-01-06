class Student:
    def __init__(self, name, age):
        self.__name = name
        self.age = age
    
s = Student ("Rohan", 60)
print(s.__name)