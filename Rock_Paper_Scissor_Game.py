import random
from tkinter import *

class RockPaperScissorsGame:

    def __init__(self, root):

        self.root = root
        self.root.geometry("620x500")
        self.root.title("ROCK PAPER SCISSOR GAME")
        self.root.configure(bg="deepskyblue3")
        self.root.minsize(300, 300)
        self.root.maxsize(650, 650)

        # Initialize variables for computer choice label and result label
        self.computer_label = None
        self.result_label = None
        self.labelll = None
        self.labellll = None
        self.final_label = None
        self.play_again_button = None
        self.exit_button = None
        self.player_score = 0
        self.computer_score = 0
        self.turn = 0
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(text="WELCOME TO THE\n\n ROCK PAPER SCISSOR\n\n GAME", bg="deepskyblue3",
                           font="comicsansms 20 bold")
        self.label.grid(ipadx=100, padx=70, pady=40)

        self.start_button = Button(fg="black", bg="aquamarine1",
                                   text="START", relief=SUNKEN, command=self.start_game)
        self.start_button.grid(row=2, column=0, ipadx=100, ipady=50, pady=5)
        self.exit_button = Button(fg="black", bg="aquamarine1", relief=SUNKEN, text="EXIT", command=quit)
        self.exit_button.grid(row=3, column=0, ipadx=105, ipady=50)

    def computer_turn(self):
        choice = random.choice(["ROCK", "PAPER", "SCISSOR"])
        # Update existing label instead of creating a new one each time
        if self.computer_label:
            self.computer_label.config(text=f"Computer: {choice}")
        else:
            self.computer_label = Label(text=f"Computer: {choice}", bg="deepskyblue3", font="Comfortaa 25 bold")
            self.computer_label.grid(row=3, column=0, pady=10)
        return choice

    def update(self, player_choice):
        self.turn += 1
        computer_choice = self.computer_turn()
        result = self.compare_choices(player_choice, computer_choice)
        # Update existing label instead of creating a new one each time
        if self.result_label:
            self.result_label.config(text=result)
        else:
            self.result_label = Label(text=result, bg="deepskyblue3", font="comicsansms 20 bold")
            self.result_label.grid(row=2, column=0, pady=10)

        if self.turn == 10:
            self.clear()
            self.show_final_scores()
            self.player_score = 0
            self.computer_score = 0
            self.turn = 0

    def compare_choices(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == "ROCK" and computer_choice == "SCISSOR") or \
                (player_choice == "PAPER" and computer_choice == "ROCK") or \
                (player_choice == "SCISSOR" and computer_choice == "PAPER"):
            self.player_score += 1
            self.score_track()
            return "You win!"
        else:
            self.computer_score += 1
            self.score_track()
            return "Computer wins!"

    def score_track(self):
        if self.labelll:
            self.labelll.grid_forget()
        if self.labellll:
            self.labellll.grid_forget()
        self.labelll = Label(self.root, text=f"Player Score: {self.player_score}", bg="deepskyblue3",
                             font="Georgia 20")
        self.labelll.grid(row=6, column=0, pady=10)
        self.labellll = Label(self.root, text=f"Computer Score: {self.computer_score}", bg="deepskyblue3",
                              font="Georgia 20")
        self.labellll.grid(row=7, column=0, pady=10)

    def show_final_scores(self):
        # Forget the player frame
        self.player_frame.grid_forget()
        if self.labelll:
            self.labelll.grid_forget()
        if self.labellll:
            self.labellll.grid_forget()

        # Display final scores
        self.final_result = f"Final Score:\nPlayer: {self.player_score}\nComputer: {self.computer_score}"
        self.final_label = Label(self.root, text=self.final_result, bg="deepskyblue3", font="comicsansms 20 bold")
        self.final_label.grid(row=0, column=2, padx=190, ipadx=20, pady=15)

        # Provide options for the player
        self.play_again_button = Button(self.root, text="Play Again", command=self.start_game)
        self.play_again_button.grid(row=1, column=2, padx=190, ipadx=30, ipady=30, pady=10)
        self.exit_button = Button(self.root, text="Exit", command=quit)
        self.exit_button.grid(row=2, column=2, padx=190, ipadx=50, ipady=30, pady=10)

    def clear(self):
        # Remove computer choice label and result label
        if self.computer_label:
            self.computer_label.grid_forget()
            self.computer_label = None
        if self.result_label:
            self.result_label.grid_forget()
            self.result_label = None

    def start_game(self):
        # Forget the welcome message and the frame containing buttons
        self.label.grid_forget()
        self.start_button.grid_forget()
        self.exit_button.grid_forget()
        if self.final_label:
            self.final_label.grid_forget()
            self.play_again_button.grid_forget()
            self.exit_button.grid_forget()

        # Create and display new frame for the game
        self.player_frame = Frame(root, borderwidth=40, bg="deepskyblue3", height=30, width=20)
        self.labell = Label(self.player_frame, text="Player", bg="deepskyblue3",
                            font="Comfortaa 25 bold")
        self.labell.grid(row=4, column=3, ipadx=70, pady=10)
        self.rock_button = Button(self.player_frame, fg="black", text="ROCK", command=lambda: self.update("ROCK"))
        self.rock_button.grid(row=5, column=2, ipadx=30, ipady=29, pady=10)
        self.paper_button = Button(self.player_frame, fg="black", text="PAPER", command=lambda: self.update("PAPER"))
        self.paper_button.grid(row=5, column=3, ipadx=30, ipady=30, pady=10)
        self.scissor_button = Button(self.player_frame, fg="black", text="SCISSOR",
                                     command=lambda: self.update("SCISSOR"))
        self.scissor_button.grid(row=5, column=4, ipadx=30, ipady=30, pady=10)
        self.player_frame.grid()


if __name__ == "__main__":
    root = Tk()
    game_instance = RockPaperScissorsGame(root)
    root.mainloop()
