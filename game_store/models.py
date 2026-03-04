from dataclasses import dataclass ,field
import json
import os

users = {
    
}

games = {
    
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
        games[212412] = {  # Username as key!
            "title": "bomba",
            "genre": "horror",
            "price": 200,
            "stock": 8,
            "publisher": "fromSoftware",
            "release_year": "2018"
        }
        with open('games.json', 'w', encoding='utf-8') as f:
            json.dump(games, f, indent=2)

    def load_library(games):
        """Load from JSON file."""
    if os.path.exists('games.json'):
        try:
            with open('games.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                games.clear()
                games.update(data)
            
        except:
            pass
    load_library(users)



class User:
    def __init__(self, username: str, email: str, password: str, b):
        self.username = username.lower()  # "Kg" → "kg" (case insensitive)
        self.email = email
        self.password = password
    
   
        
    def add_account(self):
        users[self.username] = {  # Username as key!
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
        print(f"✅ Account created! Login with: {self.username}")

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
                password=password
            )
        else:
            print("❌ Wrong password")
            return None
    
        

    
    
    def save_user(users):
        """Save to JSON file."""
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=2)

    def load_library(users):
        """Load from JSON file."""
    if os.path.exists('users.json'):
        try:
            with open('users.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                users.clear()
                users.update(data)
            
        except:
            pass
    load_library(users)


