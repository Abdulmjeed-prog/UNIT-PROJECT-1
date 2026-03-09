import models

models.load_users()
models.load_games()
models.load_giftcards()
current_user = None

def show_store_menu():
    
    """Store menu for logged-in users"""
    while True:
        models.load_users()
        models.load_games()
        print("\n" + "="*40)
        print(f"🛒 STORE MENU            {models.User.get_balance(current_user)}")
        print("="*40)
        print("1. View my library")
        print("2. Search Games")
        print("3. View Cart") 
        print("4. Add to Cart")
        print("5. Checkout")
        print("6. Redeem gift card")
        print("7. Logout")
        print("-"*40)
        
        try:
            choice = int(input(f"Welcome {current_user.username.title()}! Select (1-6): "))
        except ValueError:
            print("❌ Please enter a number!")
            continue
            
        if choice == 1:
            print("📋 Listing all games...")
            # models.list_games()
            #models.Game.display_games(models.games)
            models.Game.display_library(current_user)
            
        elif choice == 2:
            print("🔍 Search games...")
            pass
        elif choice == 3:
            print("🛒 Your cart...")
            models.User.display_user_cart(current_user)
        elif choice == 4:
            print("➕ Add to cart...")
            models.Game.display_games(models.games)
            game_id = input("Enter the Game ID:  ")
            models.User.add_to_cart(current_user, game_id)
            username = current_user.username
            models.User.save_user_cart(current_user.cart,username)
        elif choice == 5:
            print("💳 Checkout...")
            cart_total = models.User.display_user_cart(current_user)
            current_balance = current_user.get_balance()
           
            models.User.checkout(current_user, current_balance, cart_total)
            models.User.save_user(models.users)  # save updated balance/cart            
        elif choice == 6:
            gift_card  = input("Please Enter Your gift Card: ")
            models.User.redeem_gift_card(gift_card ,current_user)
            models.User.save_user(models.users)
        elif choice == 7:
            print("👋 Logging out...")
            break  # Returns to main menu
        else:
            print("❌ Invalid option (1-6 only)")

def show_admin_menu():
    """Admin panel for store management"""
    while True:
        print("\n" + "="*50)
        print("🔧 ADMIN PANEL")
        print("="*50)
        print("1. View All Users")
        print("2. Add Game") 
        print("3. Edit Game")
        print("4. Delete Game")
        print("5. View All Games")
        print("6. Add Gift Card")
        print("7. View All Gift Cards")
        print("8. Logout")
        print("-"*50)
        try:
            choice = int(input("Admin > "))
        except ValueError:
            print("❌ Enter a number!")
            continue
        
        if choice == 1:
            models.User.display_users()
        elif choice == 2:
            pass
        elif choice == 3:
            models.Game.display_games(models.games)
            game_id = input("Enter the ID of the Game: ")

            models.Game.update_game(game_id)

        elif choice == 4:
            models.Game.display_games(models.games)
            game_id = input("Enter the ID of the Game: ")
            models.Game.delete_game(game_id)
        elif choice == 5:
            pass
        elif choice == 6:
            giftcard = input("Enter Gift Card: ")
            models.User.add_gift_card(giftcard)
        elif choice == 7:
            models.User.display_gift_cards()
        elif choice == 8:
            pass
        elif choice == 9:
            pass
        elif choice == 10:
            print("👋 Admin logged out")
            break
        else:
            print("❌ Invalid option!")


while True:
    print("\n" + "="*50)
    print("      🎮 VIDEO GAME STORE 🎮")
    print("="*50)
    print("1. Register")
    print("2. Login") 
    print("3. Exit")
    print("-"*50)
    try:
        f_choice = int(input("Select an option (1-3): "))
    except ValueError:
        print("❌ Please enter a number!")
        continue
    
    if f_choice == 1:  # Register
        username = input("Username: ").strip()
        email = input("Email: ").strip()
        password = input("Password: ").strip()
        new_user = models.User(username, email, password)
        new_user.add_account()
        models.User.save_user(models.users)
    elif f_choice == 2:  # Login
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        logged_user = models.User.login(username, password)
        
        if logged_user.role == "user":
            current_user = logged_user
            print("🎮 Welcome to the store!")
            show_store_menu()  # ← GO TO STORE MENU!
            current_user = None  # Reset after logout
        
        elif logged_user.role == "admin":
            current_user = logged_user
            print(f"Welcom {current_user.username}")
            show_admin_menu()
            current_user = None
        else:
            print("❌ Login failed. Try again.")
            
    elif f_choice == 3:
        print("👋 Thanks for visiting!")
        break
        
    else:
        print("❌ Invalid option (1-3 only)")



# Fix your Game instantiation (class name case + constructor args)
#
