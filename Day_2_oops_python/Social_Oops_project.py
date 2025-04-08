print("Oops mini project : ChatBook")

class ChatBook:
    def __init__(self):
       self.email = ''
       self.password = ''
       self.login = False
       self.post = ''
       self.menu()

    def menu(self):
        user_input=input("""
                        Hello to the welcome page of ChatBook
                        Press 1 to signup
                        Press 2 to signin
                        Press 3 to write a posplit 
                        Press 4 to View your post
                        Hit any key to exit
                         """)
        if user_input == '1':
            print("you pressed 1")
            self.signup()

        elif user_input == '2':
            print("You pressed 2")
            self.signin()
        elif user_input == '3':
            print("You pressed 3")
            self.Createpost()
        elif user_input == '4':
            print("You pressed 4")
            self.viewPost()
        else:
            exit()
        
    def signup(self):
        inputEmail = input("Enter your email : ")
        inputPass = input("Enter Password : ")
        self.email = inputEmail
        self.password = inputPass
        print("You have SIGNED UP successfully")
        print("\n")
        self.menu()
        
    def signin(self):
        if self.email=='' and self.password=='':
            print("First Sign Up by pressing 1")
        else:
            takeemail = input("Enter your email : ")
            takepass = input("Enter the password : ")
            if takeemail==self.email and takepass==self.password:
                print("You have SIGNED IN successfully")
                print("write a post by pressing 3")
                self.login = True
            else:
                print("Please enter valid email or password")
        self.menu()
    def Createpost(self):
        if self.login == True:
            inputPost = input("Write a post : \n ")
            self.post = inputPost 
        else:
            print("Please SIGN IN first by pressing  2")
        self.menu()
    def viewPost(self):
        if self.login == True:
            print(self.post)
        else:
            print("please SIGN IN  first by pressing 2")

            




User_1=ChatBook()
