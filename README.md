# Project: Video Game Store CLI

## Overview
This is a command-line interface (CLI) application for a Digital Video Game Store. The system allows users to browse and purchase games using a wallet system fueled by gift cards. Once purchased, games are added to a user's library where they can actually be launched and played.

The project uses persistent JSON storage to manage users, games, and gift cards, ensuring data is saved between sessions.

---

## Features & User Stories

### As a Customer (User), I should be able to:
* **Register & Login:** Create a unique account and access it securely.
* **Browse Games:** View a list of all available games including their genre, price, and publisher.
* **Manage Cart:** Add games to a shopping cart by their ID and view the total price.
* **Wallet Management:** Redeem gift cards to increase my account balance (SAR).
* **Purchase:** Checkout my cart to move games from the store into my personal library.
* **Play Games:** Launch mini-games (like Tic-Tac-Toe, Hangman, etc.) directly from my library.

### As an Admin, I should be able to:
* **User Oversight:** View a full report of all registered users, their emails, and balances.
* **Inventory Management:** Edit existing game details or delete games from the store.
* **Gift Card Control:** Create new gift cards with specific SAR amounts and monitor which cards have been redeemed and by whom.

---

## Usage

Run the main script to start the application. Use the numeric keyboard to navigate the menus.

### 1. Account Setup
- **Register:** Follow the prompts to enter a username, email, and password.
- **Login:** Enter your credentials. The system will recognize if you are a standard **User** or an **Admin**.

### 2. User Commands (Store Menu)
- **View my library:** Type `1` to see your games. Enter the game number to **Play**.
- **Add to Cart:** Type `3`, then enter the **Game ID** (e.g., `100021`) to add it to your cart.
- **Checkout:** Type `4` to pay for your cart items using your balance.
- **Redeem Gift Card:** Type `5` and enter your code to add funds.

### 3. Admin Commands (Admin Panel)
- **Edit/Delete Game:** Type `2` or `3` and provide the **Game ID** to modify the store inventory.
- **Add Gift Card:** Type `5` to generate a new code and set its value.
- **View Reports:** Type `1` for a user report or `6` for a gift card status report.

---

## Data Management
The project automatically creates a `data/` directory to store the following:
- `users.json`: Stores user profiles and credentials.
- `games.json`: Stores the catalog of games.
- `giftcard.json`: Tracks all valid and used gift card codes.
- `{username}_cart.json`: Temporary storage for user shopping carts.