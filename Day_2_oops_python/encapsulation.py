print("learning encapsulation")

# intialize a class 
class employee:
    __user_id = 0
    # its is a special/magic/dunder method --> constructer
    def __init__(self):
        self.__name = 'Ayush'
        employee.__user_id +=1
        self.age = 19
        self.salary = 50000
        self.designation =  'ML engineer'

    def get_name(self):
        return self.__name

    def set_name(self,value):
        self.__name = value
    
    @staticmethod
    def get_user_id():
        return employee.__user_id
    
    def travel(self,place):
        return f"i am going to {place}"
# object and instance of class
user1 = employee()

# print an attribute 
#print(user1.__name)
print(f"we can access private attributes {user1._employee__name}")

print(user1.get_name())
user1.set_name('agu')
print(user1.get_name())


print(user1.get_user_id())




