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


def rock_paper_scissors():
    """Rock Paper Scissors vs computer!"""
    choices = ['rock', 'paper', 'scissors']
    print("✂️ ROCK PAPER SCISSORS (Type 'q' to quit)")
    wins = 0
    while True:
        player = input("\nYour choice: ").lower().strip()
        if player == 'q':
            print(f"Final: {wins} wins!")
            return
        if player not in choices:
            print("❌ Invalid! Choose rock, paper, or scissors.")
            continue
        computer = random.choice(choices)
        print(f"Computer: {computer}")
        if player == computer:
            print("🤝 Tie!")
        elif (player == 'rock' and computer == 'scissors') or \
             (player == 'paper' and computer == 'rock') or \
             (player == 'scissors' and computer == 'paper'):
            print("🎉 You win!")
            wins += 1
        else:
            print("💀 Computer wins!")
    print("Game over!")


def tic_tac_toe():
    """Tic Tac Toe (Player X vs Player O)."""
    board = [' ' for _ in range(9)]
    current = 'X'
    print("❌⭕ TIC TAC TOE")
    print("Positions:\n1|2|3\n4|5|6\n7|8|9")
    
    def print_board():
        print(f"\n{board[0]}|{board[1]}|{board[2]}\n-+-+-")
        print(f"{board[3]}|{board[4]}|{board[5]}\n-+-+-")
        print(f"{board[6]}|{board[7]}|{board[8]}\n")
    
    def check_winner(p):
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        return any(board[i] == board[j] == board[k] == p for i,j,k in wins)
    
    while True:
        print_board()
        try:
            pos = int(input(f"Player {current}, position (1-9): ")) - 1
            if pos < 0 or pos > 8 or board[pos] != ' ':
                print("❌ Invalid or taken! Try again.")
                continue
            board[pos] = current
            if check_winner(current):
                print_board()
                print(f"🎉 Player {current} wins!")
                return
            if ' ' not in board:
                print_board()
                print("🤝 Tie game!")
                return
            current = 'O' if current == 'X' else 'X'
        except ValueError:
            print("❌ Enter a number 1-9!")


def number_quiz():
    """Quick math quiz! Answer 10 questions."""
    score = 0
    print("🧮 NUMBER QUIZ (10 questions)")
    for i in range(10):
        a, b = random.randint(1, 20), random.randint(1, 20)
        try:
            ans = int(input(f"Q{i+1}: {a} + {b} = "))
            if ans == a + b:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! ({a + b})")
        except ValueError:
            print("❌ Skip!")
    print(f"🎯 Score: {score}/10")


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
    "pokete": play_pokete,
    "rps": rock_paper_scissors,
    "tictactoe": tic_tac_toe,
    "quiz": number_quiz
}
