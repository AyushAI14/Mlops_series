# intialize a class 
class employee:
    # its is a special/magic/dunder method --> constructer
    def __init__(self):
        print("Attributes execution start")
        self.name = 'Ayush'
        self.age = 19
        self.salary = 50000
        self.designation =  'ML engineer'
        print("Attributes executed")

    
    def travel(self,place):
        return f"i am going to {place}"
# object and instance of class
ayush = employee()

# print an attribute 
print(ayush.age)

# calling a method
print(ayush.travel('dubai'))
print(type(ayush))



