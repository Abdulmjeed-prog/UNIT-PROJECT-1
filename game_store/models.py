from dataclasses import dataclass ,field
import json
import os
import random
users = {
    212121: {
        "username": "AhmedXd", "email": "Abdulmjeed@gmail.com"
    }
}

games = {
    212121: {
        "DarkSouls","PS5","Souls",2151,5,"FromSoftware",2018
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


class User:
    def __init__(self, username:str, email:str):
        self.id = random.randint(1, 10)
        self.username = username
        self.email = email
        
    def add_account(self):
        users[self.id] = {
            "username": self.username,
            "email": self.email
        }
    
    def save_library(users):
        """Save to JSON file."""
        with open('library.json', 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=2)

