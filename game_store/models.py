from dataclasses import dataclass ,field
import json
import os

users = {
    
}

games = {
    
}

gift_cards = {
    "ABCD-EFGH-IJKL-MNOP": {  # 20 chars + dashes (exact PSN format)
        "amount": 100.0,
        "currency": "SAR",
        "is_used": False,
        "assigned_to": None,
        "code": "ABCD-EFGH-IJKL-MNOP"
    },
    "WXYZ-1234-5678-9ABC": {
        "amount": 50.0, 
        "currency": "SAR",
        "is_used": False,
        "assigned_to": None,
        "code": "WXYZ-1234-5678-9ABC"
    },
    "PSN4-QRST-UVWX-YZ12": {
        "amount": 200.0,
        "currency": "SAR", 
        "is_used": False,
        "assigned_to": None,
        "code": "PSN4-QRST-UVWX-YZ12"
    }
}


class Game: 
    def __init__(self, id: int, title: str, genre: str, price: float, stock: int, 
                 publisher: str, release_year: int):
        self.id = id           
        self.title = title
        self.genre = genre
        self.price = price
        self.stock = stock
        self.publisher = publisher
        self.release_year = release_year
    
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
            print(f"   {game['genre']} | ${game['price']:,.2f} | Stock: {game['stock']}")
            print(f"   {game['publisher']} - {game['release_year']}")
            print("-" * 70)

    

    def save_game(games):
        """Save to JSON file."""
        with open('data/games.json', 'w', encoding='utf-8') as f:
            json.dump(games, f, indent=2)

    



class User:
    def __init__(self, username: str, email: str, password: str, balance:int = 0):
        self.username = username.lower()  # "Kg" → "kg" (case insensitive)
        self.email = email
        self.password = password
        self.__balance = balance
        self.cart = {}
    
    def set_balance(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
        
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
            "balance": 0
        }
        
        print(f"✅ Account created successfully!")
        print(f"   Login with: {self.username}")
        print(f"   Save your details safely!")


    @staticmethod
    def login(username: str, password: str) -> 'User|None':
        username = username.lower().strip()  # Normalize input
        
        if username not in users:
            print("❌ User not found. Register first.")
            return None
        
        user_data = users[username]
        
        if password == user_data["password"]:
            print(f"✅ Welcome back, {username.title()}!")
            return User(
                username=username,
                email=user_data["email"],
                password=password,
                balance=user_data["balance"]
            )
        else:
            print("❌ Wrong password")
            return None
    
    def redeem_gift_card(gift_card, current_user):
        if gift_card in gift_cards:
            users[current_user.username]["balance"] += gift_cards[gift_card]["amount"]  # Fixed!
            print(f"✅ Added {gift_cards[gift_card]['amount']} SAR to balance!")
            gift_cards[gift_card]["is_used"] = True  # Mark as used
            gift_cards[gift_card]["assigned_to"] = current_user.username
        else:
            print("❌ Invalid gift card")

    def add_to_cart(current_user, game_id ):
        if game_id not in games:
            return "invalid ID"

        game = games[game_id]

        if game_id not in current_user.cart:
            current_user.cart[game_id] = 1
        else:
            current_user.cart[game_id] += 1
        
        
        print(current_user.cart)
        print(f"✅ Added '{game['title']}' to your cart.")
        print(f"   🛒 Cart now has {len(current_user.cart)} items")

    def display_user_cart(current_user):
        current_user.cart = load_user_cart(current_user.username)
        print("\n🛒 YOUR CART")
    
        if not current_user.cart:
            print("Cart is empty!")
            return
    
        for game_id, quantity in current_user.cart.items():  # ← .items() FIX!
            game = games[game_id]
            print(f"{quantity}x {game['title']} (ID: {game_id})")
            print(f"  Price: ${game['price']}")
            print()

            
    
    
    def save_user(users):
        os.makedirs("data", exist_ok=True)  # Creates folder if missing!
        with open('data/users.json', 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=2)
    
    def save_user_cart(cart,username):
        """Save to JSON file."""
        with open(f'data/{username}_cart.json', 'w', encoding='utf-8') as f:
            json.dump(cart, f, indent=2)



@staticmethod
def load_games():
    global games
    if os.path.exists('games.json'):
        try:
            with open('data/games.json', 'r') as f:
                games.clear()
                games.update(json.load(f))
                print(f"✅ Loaded {len(games)} games")
        except Exception as e:
            print(f"❌ Load error: {e}")

@staticmethod
def load_users():
    global users
    if os.path.exists('data/users.json'):
        try:
            with open('data/users.json', 'r') as f:
                users.clear()
                users.update(json.load(f))
                print(f"✅ Loaded {len(users)} users")
        except Exception as e:
            print(f"❌ Load error: {e}")

@staticmethod
def load_user_cart(username: str) -> dict:
    """Load user's cart from JSON"""
    cart_file = f'{username}_cart.json'
    if os.path.exists(cart_file):
        try:
            with open(cart_file, 'r', encoding='utf-8') as f:
                cart = json.load(f)
                print(f"✅ Loaded {len(cart)} cart items for {username}")
                return cart
        except Exception as e:
            print(f"❌ Cart load error: {e}")
    return {}  # Empty cart if no file




