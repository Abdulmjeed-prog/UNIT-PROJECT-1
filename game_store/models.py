from dataclasses import dataclass ,field
import json
import os
import mini_games
users = {
    
}

games = {
    
}

gift_cards = {

}


class Game: 
    def __init__(self, id: int, title: str, genre: str, price: float, 
                 publisher: str, release_year: int):
        self.id = id           
        self.title = title
        self.genre = genre
        self.price = price
        self.publisher = publisher
        self.release_year = release_year

    @staticmethod
    def display_games(games):
        """Display all games from dict"""
        if not games:
            print("No games available.")
            return
    
        print("\n📋 AVAILABLE GAMES:")
        print("=" * 70)
        for num, game_id in enumerate(games, start=1):
            game = games[game_id]
            print(f"{num}. {game['title']} (ID: {game_id})")
            print(f"   {game['genre']} | {game['price']:,.2f} SAR")
            print(f"   {game['publisher']} - {game['release_year']}")
            print("-" * 70)

    @staticmethod 
    def display_library(current_user):
        """Display all games from dict"""
        if not current_user.library:
            print("No games available.")
            return
    
        print("\n📋 AVAILABLE GAMES:")
        print("=" * 70)
        for num, owned in enumerate(current_user.library, start=1):
            print(f"{num}. {owned['title']} (ID: {owned['game_id']})")  
            print(f"   {owned['genre']}")
            print("-" * 70)
        
        # Game selection
        try:
            choice = int(input("\nEnter game number to PLAY (or 0 to cancel): "))
            if 1 <= choice <= len(current_user.library):
                selected_game = current_user.library[choice-1]
                game_id = selected_game['game_id']
                print(f"\n🎮 Launching: {selected_game['title']}...")
                play_game_from_library(game_id,selected_game)
            else:
                print("Cancelled.")
        except ValueError:
            print("❌ Enter a number!")
    @staticmethod
    def update_game(game_id: str):
        """Admin: update a game's info with validation."""
        if game_id not in games:
            print("❌ Invalid game ID.")
            return
        
        game = games[game_id]
        print(f"\n✏️ Editing game: {game['title']} (ID: {game_id})")
        
        # --- Title (non-empty string) ---
        new_title = input(f"New title [{game['title']}]: ").strip()
        if new_title == "":
            new_title = game["title"]  # keep old
        elif len(new_title) < 2:
            print("❌ Title must be at least 2 characters. Keeping old title.")
            new_title = game["title"]
        
        # --- Genre (optional, non-empty if changed) ---
        new_genre = input(f"New genre [{game['genre']}]: ").strip()
        if new_genre == "":
            new_genre = game["genre"]
        
        # --- Price (float >= 0) ---
        while True:
            new_price_str = input(f"New price [{game['price']}]: ").strip()
            if new_price_str == "":
                new_price = game["price"]
                break
            try:
                new_price = float(new_price_str)
                if new_price < 0:
                    print("❌ Price cannot be negative.")
                    continue
                break
            except ValueError:
                print("❌ Enter a valid number for price (e.g. 199 or 199.99).")
        
        # --- Publisher (optional) ---
        new_publisher = input(f"New publisher [{game['publisher']}]: ").strip()
        if new_publisher == "":
            new_publisher = game["publisher"]
        
        # --- Release year (int, reasonable range) ---
        while True:
            new_year_str = input(f"New release year [{game['release_year']}]: ").strip()
            if new_year_str == "":
                new_year = game["release_year"]
                break
            try:
                new_year = int(new_year_str)
                if new_year < 1980 or new_year > 2030:
                    print("❌ Year must be between 1980 and 2030.")
                    continue
                break
            except ValueError:
                print("❌ Enter a valid year (e.g. 2018).")
        
        # --- Apply changes ---
        game["title"] = new_title
        game["genre"] = new_genre
        game["price"] = new_price
        game["publisher"] = new_publisher
        game["release_year"] = new_year
        
        Game.save_game(games)
        print("✅ Game updated successfully!")

    @staticmethod
    def delete_game(game_id):
        """Delete game from store with confirmation."""
        if game_id not in games:
            print("❌ Invalid game ID.")
            return
        
        game = games[game_id]
        print(f"\n🗑️ Delete '{game['title']}'?")
        print(f"  ID: {game_id} | Price: {game['price']} SAR")
        
        confirm = input("Type 'DELETE' to confirm (or Enter to cancel): ").strip().upper()
        
        if confirm == "DELETE":
            removed_game = games.pop(game_id)
            Game.save_game(games)
            print(f"✅ '{removed_game['title']}' deleted successfully!")
        else:
            print("❌ Deletion cancelled.")

    @staticmethod
    def save_game(games):
        """Save to JSON file."""
        with open('data/games.json', 'w', encoding='utf-8') as f:
            json.dump(games, f, indent=2)

    



class User:
    def __init__(self, username: str, email: str, password: str, balance:int = 0, cart=None, library=None, role="user"):
        self.username = username.lower()
        self.email = email
        self.password = password
        self.__balance = balance
        self.cart = cart or {}
        self.library = library or []
        self.role = role
    
    def set_balance(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    

    @staticmethod
    def display_users():
        """Display all users for admin"""
        if not users:
            print("👥 No users registered yet!")
            return
        
        print("\n👥 ALL USERS REPORT")
        print("=" * 80)
        print(f"{'ID':<4} {'USERNAME':<12} {'EMAIL':<25} {'BALANCE':<10} {'GAMES':<6}")
        print("-" * 80)
        
        user_count = 0
        total_balance = 0
        
        for username, data in users.items():
            user_count += 1
            balance = data.get('balance', 0)
            library_count = len(data.get('library', []))
            total_balance += balance
            
            print(f"{user_count:<4} {username.title():<12} {data['email']:<25} "
                f"{balance:<10} {library_count:<6}")
        
        print("-" * 80)
        print(f"TOTAL: {user_count} users | Total Balance: {total_balance} SAR")
        print(f"Average Balance: {total_balance/user_count:.0f} SAR/user")
    
    def add_to_cart(current_user, game_id: str):
        """Add a game to the current user's cart by game_id."""
        game_id = str(game_id).strip()

        # 1) Validate game exists
        if game_id not in games:
            print("❌ Invalid game ID.")
            return

        game = games[game_id]

        # 2) Make sure user has a cart dict
        if current_user.cart is None:
            current_user.cart = {}

        # 3) Prevent duplicates
        if game_id in current_user.cart:
            print(f"⚠️ '{game['title']}' is already in your cart.")
            return

        # 4) Add with default quantity = 1
        current_user.cart[game_id] = 1

        # 5) Feedback
        print(f"✅ Added '{game['title']}' to your cart.")
        print(f"   🛒 Cart now has {len(current_user.cart)} items.")


        
    def add_account(self):
    # 1. Check if user already exists
        if self.username in users:
            print(f"❌ Username '{self.username}' already exists!")
            return
    
    # 2. Username validation
        if len(self.username) < 3:
            print("❌ Username must be at least 3 characters!")
            return
        if not self.username.replace("_", "").replace("-", "").isalnum():
            print("❌ Username can only contain letters, numbers, _, -")
            return
    
    # 3. Email validation (basic)
        if "@" not in self.email or "." not in self.email:
            print("❌ Invalid email format!")
            return
    
    # 4. Password validation
        if len(self.password) < 6:
            print("❌ Password must be at least 6 characters!")
            return
    
    # 5. All good - create account
        users[self.username] = {
            "username": self.username,
            "email": self.email,
            "password": self.password,  # In production: hash this!
            "balance": 0,
            "cart": {},
            "library": [],
            "role": "user"
        }
        
        print(f"✅ Account created successfully!")
        print(f"   Login with: {self.username}")
        print(f"   Save your details safely!")


    @staticmethod
    def login(username: str, password: str) -> 'User|None':
        username = username.lower().strip()  # Normalize input
        
        if username not in users:
            print("❌ User not found. Register first.")
            return User(username=username,
                        email="",
                        password=password,
                        balance=0,
                        cart={},
                        library=[],
                        role = "")
        
        user_data = users[username]
        
        if password == user_data["password"]:
            print(f"✅ Welcome back, {username.title()}!")
            return User(
                username=username,
                email=user_data["email"],
                password=password,
                balance=user_data["balance"],
                cart=user_data.get("cart", {}),      
                library=user_data.get("library", []),
                role = user_data["role"]

            )
        else:
            print("❌ Wrong password")
            return User(username=username,
                        email="",
                        password=password,
                        balance=0,
                        cart={},
                        library=[],
                        role = "")
    
    def redeem_gift_card(gift_card, current_user):
        if gift_card in gift_cards and not gift_cards[gift_card]["is_used"]:
            users[current_user.username]["balance"] += gift_cards[gift_card]["amount"]  # Fixed!
            current_user.set_balance(current_user.get_balance() + gift_cards[gift_card]["amount"])
            print(f"✅ Added {gift_cards[gift_card]['amount']} SAR to balance!")
            gift_cards[gift_card]["is_used"] = True  # Mark as used
            gift_cards[gift_card]["assigned_to"] = current_user.username
            save_giftcard(gift_cards)
        else:
            print("❌ Invalid gift card")

    def add_gift_card(giftcard_code: str = None):
        """Admin: Add new gift card with flexible validation."""
        if giftcard_code is None:
            giftcard_code = input("Enter gift card code: ").strip().upper()
        
        # Validation 1: Length (10-25 chars, like your examples)
        if len(giftcard_code) < 10 or len(giftcard_code) > 25:
            print("❌ Code must be 10-25 characters (e.g. WXYZ-1234-5678-9ABC)")
            return
        
        # Validation 2: Format (alphanumeric + dashes/underscores)
        if not giftcard_code.replace("-", "").replace("_", "").replace(".", "").isalnum():
            print("❌ Only letters, numbers, -, _, . allowed")
            return
        
        # Validation 3: Unique
        if giftcard_code in gift_cards:
            print(f"❌ '{giftcard_code}' already exists!")
            return
        
        # Validation 4: Amount (> 0)
        while True:
            try:
                amount = float(input("Amount (SAR): "))
                if amount <= 0:
                    print("❌ Amount must be positive!")
                else:
                    break
            except ValueError:
                print("❌ Enter valid number!")
        
        # Save
        gift_cards[giftcard_code] = {
            "amount": amount,
            "currency": "SAR",
            "is_used": False,
            "assigned_to": None,
            "code": giftcard_code
        }
        
        save_giftcard(gift_cards)
        print(f"✅ '{giftcard_code}' added ({amount} SAR)!")
    

    def display_gift_cards():
        """Admin: Display all gift cards status."""
        if not gift_cards:
            print("💳 No gift cards created yet!")
            return
        
        print("\n💳 ALL GIFT CARDS")
        print("=" * 80)
        print(f"{'CODE':<20} {'AMOUNT':<10} {'STATUS':<10} {'ASSIGNED TO'}")
        print("-" * 80)
        
        used_count = 0
        total_value = 0
        
        for code, data in gift_cards.items():
            status = "✅ USED" if data["is_used"] else "🆓 AVAILABLE"
            assigned = data["assigned_to"] or "None"
            
            if data["is_used"]:
                used_count += 1
            
            total_value += data["amount"]
            
            print(f"{code:<20} {data['amount']:<10} SAR {status:<10} {assigned}")
        
        print("-" * 80)
        print(f"Total: {len(gift_cards)} cards | Used: {used_count}/{len(gift_cards)}")
        print(f"Total Value: {total_value} SAR")


    def display_user_cart(current_user):
        current_user.cart = load_user_cart(current_user.username)
    
        if not current_user.cart:
            print("Cart is empty!")
            return
        total = 0

        for game_id in current_user.cart.keys():  # Simple keys only
            game = games[game_id]
            print(f"{game['title']} (ID: {game_id})")  # Clean "Game Title (ID: 1001)"
            print(f"  Price: {game['price']} SAR")
            total += float(game['price'])  # Use float, not int
        print(f"\n💰 Total: {total:.2f} SAR")

        return total

    def checkout(current_user, balance, total):
        try:
            if balance >= total:
                users[current_user.username]["balance"] -= total
                current_user.set_balance(current_user.get_balance() - total)
                print("✅ Checkout complete!")
                
                # ADD GAMES TO LIBRARY (snapshots!)
                users[current_user.username].setdefault("library", [])
                current_user.library = current_user.library or []
                
                for game_id in current_user.cart:  # cart still has items
                    game = games.get(game_id)
                    if game:
                        snapshot = {
                            "game_id": game_id,
                            "title": game["title"],
                            "price": game["price"],
                            "genre": game.get("genre", "Unknown")
                        }
                        
                        # Avoid duplicates
                        if not any(g["game_id"] == game_id for g in current_user.library):
                            current_user.library.append(snapshot)
                            users[current_user.username]["library"].append(snapshot)
                            print(f"📚 Added: {game['title']}")
                
                # Clear cart AFTER adding to library
                current_user.cart = {}
                users[current_user.username]["cart"] = {}
                delete_cart_file(current_user.username)
                
                # Save everything
                User.save_user(users)
                print("🎮 Games added to your library!")
                
            else:
                print("❌ Insufficient balance")
        except Exception as e:
            print(f"❌ Checkout error: {e}")


        
    def save_user(users):
        os.makedirs("data", exist_ok=True)  # Creates folder if missing!
        with open('data/users.json', 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=2)
    
    def save_user_cart(cart,username):
        """Save to JSON file."""
        with open(f'data/{username}_cart.json', 'w', encoding='utf-8') as f:
            json.dump(cart, f, indent=2)




def load_games():
    global games
    if os.path.exists('data/games.json'):
        try:
            with open('data/games.json', 'r') as f:
                games.clear()
                games.update(json.load(f))
        except Exception as e:
            print(f"❌ Load error: {e}")


def load_users():
    global users
    if os.path.exists('data/users.json'):
        try:
            with open('data/users.json', 'r') as f:
                users.clear()
                users.update(json.load(f))
        except Exception as e:
            print(f"❌ Load error: {e}")

def load_giftcards():
    global gift_cards
    if os.path.exists('data/giftcard.json'):
        try:
            with open('data/giftcard.json', 'r') as f:
                gift_cards.clear()
                gift_cards.update(json.load(f))
        except Exception as e:
            print(f"❌ Load error: {e}")


def load_user_cart(username: str) -> dict:
    """Load user's cart from JSON"""
    cart_file = f'data/{username}_cart.json'
    if os.path.exists(cart_file):
        try:
            with open(cart_file, 'r', encoding='utf-8') as f:
                cart = json.load(f)
                print(f"✅ Loaded {len(cart)} cart items for {username}")
                return cart
        except Exception as e:
            print(f"❌ Cart load error: {e}")
    return {}  # Empty cart if no file

def delete_cart_file(username):
    """Delete cart JSON file"""
    cart_file = f'data/{username}_cart.json'
    if os.path.exists(cart_file):
        os.remove(cart_file)
        print(f"🗑️ Deleted {cart_file}")
    else:
        print("📁 No cart file found")



def play_game_from_library(game_id, game_snapshot):
    """Launch minigame or specific game logic based on game_id"""
    game_id = str(game_id)  # Normalize
    

    if game_id == "100021":
        mini_games.play_pokete()
    elif game_id == "100022":
        mini_games.rock_paper_scissors()
    elif game_id == "100023":
        mini_games.tic_tac_toe()
    elif game_id == "100024":
        mini_games.number_quiz()
    elif game_id == "100025":
        mini_games.hangman()
    elif game_id == "100026":
        mini_games.number_guessing()
    else:
        pass
    
    input("\nPress Enter to return to store...")


def save_giftcard(gift_cards):
    os.makedirs("data", exist_ok=True)  # Creates folder if missing!
    with open('data/giftcard.json', 'w', encoding='utf-8') as f:
        json.dump(gift_cards, f, indent=2)




