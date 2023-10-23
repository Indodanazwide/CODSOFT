import tkinter as tk
import random

def game_logic(player_choice):
    choices = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
         result = "a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissor") or (player_choice == "Paper" and computer_choice == "Rock") or (player_choice == "Scissor" and computer_choice == "Paper"):
        result = "you win!"
    else:
        result = "you loose!"

    display_screen.config(text=f"Player choice is {player_choice}, computer choice is {computer_choice}. The final result is {result}")

root = tk.Tk()

root.geometry("700x90")

display_screen = tk.Label(root, font="Arial")
display_screen.pack()

choice_frame = tk.Frame()
choice_frame.pack()

rock_button = tk.Button(choice_frame, text="Rock", command=lambda : game_logic("Rock"), font="Arial")
paper_button = tk.Button(choice_frame, text="Paper", command=lambda : game_logic("Paper"), font="Arial")
scissor_button = tk.Button(choice_frame, text="Scissor", command=lambda : game_logic("Scissor"), font="Arial")

rock_button.grid(row=0, column=0, padx=20)
paper_button.grid(row=0, column=1, padx=20)
scissor_button.grid(row=0, column=2, padx=20)


root.mainloop()
