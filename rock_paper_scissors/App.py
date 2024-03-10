import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock, Paper, Scissors Game")

        # Adding a label for instructions
        self.label = tk.Label(master, text="Enter your choice (rock/paper/scissors):", font=("Arial", 12))
        self.label.pack()

        # Adding an entry widget for user input
        self.entry = tk.Entry(master, font=("Arial", 12))
        self.entry.pack()

        # Adding a button with a callback function
        self.play_button = tk.Button(master, text="Play", command=self.play_game, font=("Arial", 12))
        self.play_button.pack()
    
    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def play_game(self):
        user_choice = self.entry.get().lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            messagebox.showerror("Invalid Choice", "Please enter rock, paper, or scissors.")
            return

        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)

        #Display the result in a hemed message box
        messagebox.showinfo("Result", f"You chose {user_choice}. Computer chose {computer_choice}. {result}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
        ):
            return "You win!"
        else:
            return "Computer wins!"

if __name__ == "__main__":
    root = tk.Tk()

    # setting the windows size
    root.geometry("400x200")

    # Adding a background color
    root.configure(bg="#f0f0f0")
    
    app = RockPaperScissorsApp(root)
    root.mainloop()
