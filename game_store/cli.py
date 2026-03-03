import models

while True:
    choice = int(input("Select Your Option: "))
    if choice == 1:
        username = input("Enter Your username: ")
        email = input("Enter Your Email: ")
        user1 = models.User(username,email)
        models.User.add_account(user1)
        print(models.users)
        models.User.save_library(models.users)
    elif choice == 2:
        pass
    elif choice == 3:
        print("Hello World")
        game1 = models.game(232124,"Bloodborne","PS5","Souls",2151,5,"fromSoftware",2018)
        print(game1)
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        print("Thank You")
        break
    else:
        print("Invalid select")