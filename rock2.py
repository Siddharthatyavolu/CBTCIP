import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a Tie!"
    elif ((user_choice == 'Rock' and comp_choice == 'Scissors') or 
         (user_choice == 'Paper' and comp_choice == 'Rock') or 
         (user_choice == 'Scissors' and comp_choice == 'Paper')):
        return "You Win!"
    else:
        return "Computer Wins!"

# Function to handle user choice
def on_choice_click(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(choices)
    result = determine_winner(user_choice, comp_choice)
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {comp_choice}\n{result}")

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")
window.geometry("400x250")

# Create labels
title_label = tk.Label(window, text="Rock, Paper, Scissors Game", font=("Arial", 16))
title_label.pack(pady=10)
choice_label = tk.Label(window, text="Choose your move:")
choice_label.pack()

# Create buttons for choices
choices = ["Rock", "Paper", "Scissors"]
for choice in choices:
    button = tk.Button(window, text=choice, command=lambda c=choice: on_choice_click(c))
    button.pack(pady=5)

# Create a label for displaying the result
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Start the GUI application
window.mainloop()
