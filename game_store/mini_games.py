# games.py - ALL game functions here!
import random
import subprocess
import sys
import os
import shutil

def number_guessing():
    """Guess the number 1-100!"""
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("🔢 GUESS THE NUMBER (1-100)")
    print(f"You have {max_attempts} attempts!")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts+1}/{max_attempts} - Guess: "))
            attempts += 1
            
            if guess == secret:
                print(f"🎉 CORRECT! You won in {attempts} attempts!")
                return
            elif guess < secret:
                print("📈 Too low!")
            else:
                print("📉 Too high!")
        except ValueError:
            print("❌ Enter a number!")
            continue
    
    print(f"💀 Game over! Number was: {secret}")

def hangman():
    words = ["python", "pokete", "store", "eldenring"]
    word = random.choice(words).upper()
    guessed = ["_"] * len(word)
    wrong = 0
    
    print("🎯 HANGMAN")
    while wrong < 6 and "_" in guessed:
        print(f"Word: {' '.join(guessed)} | Wrong: {wrong}")
        guess = input("Letter: ").upper()
        if guess in word:
            for i, l in enumerate(word):
                if l == guess: guessed[i] = guess
        else:
            wrong += 1
    print(f"{'🎉 WIN!' if '_' not in guessed else '💀 LOSE:'} {word}")

def play_pokete():
    """Pokete launcher"""
    save_path = os.path.expanduser("~/.config/pokete")
    if os.name == 'nt':
        save_path = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "pokete")
    
    if os.path.exists(save_path):
        shutil.rmtree(save_path)
        print("🆕 Fresh Pokete!")
    
    subprocess.run([sys.executable, "-m", "pokete"])
    os.system("cls" if os.name == 'nt' else "reset")

# Dictionary for easy lookup
GAME_METHODS = {
    "guessing": number_guessing,
    "hangman": hangman,
    "pokete": play_pokete
}
