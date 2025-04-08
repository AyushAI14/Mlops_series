print("Oops mini project : ChatBook")


class ChatBook:
    def __init__(self):
       self.name = ''
       self.password = ''
       self.login = False
       self.menu()

    def menu(self):
        user_input=input("""
                        Hello to the welcome page of ChatBook
                        Press 1 to signin
                        Press 2 to signup
                        Press 3 to login
                        Hit any key to exit
                         """)
        if user_input == '1':
            print("you pressed 1")
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        else:
            exit()

obj=ChatBook()
