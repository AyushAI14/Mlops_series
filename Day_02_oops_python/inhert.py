print("Learning Inheritance")

class dog:
    def __init__(self,color,name,age):
        self.color = color 
        self.name = name
        self.age = age
    
    def get_color(self):
        return self.color

class breed(dog):
    def get_name(self):
        return self.name


dog1 = dog('black','kutta',4)
print(f"color of dog_1 is {dog1.get_color()}")

print('creating a derived class')
dog_breed_class = breed('white','chua',1)
print(f"this is deived from clas dog {dog_breed_class.get_name()}")


