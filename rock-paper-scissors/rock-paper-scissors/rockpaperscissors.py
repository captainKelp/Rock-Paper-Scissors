import random
import tkinter

#NOTE: A function that determines whether the user wins or not
#      Passes the user's choice (based on what button they click)to the parameter
def get_winner(call):


    # Access variables declared after the function so that the variables can be changed inside of the function
    global wins, win, output

    # 1. Create random integer 1-3 to use as computer's play
    computerChoice.randrange(1, 2, 3)
    computer
    # 2. Using if-statements, assign the computer to a choice (rock, paper, scissors) using the random integer generated
    if computerChoice == 1:
        computerChoice = "rock"
    if computerChoice == 2:
        computerChoice = "paper"
    if computerChoice == 3:
        computerChoice = "scissors"
    return computerChoice
    # 3. Determine the winner based on what the user chose and what the computer chose
    root = tkinter()

    def callback(event):
        print("clicked at", event.x, event.y)
    frame = Frame(root, width = 100, height = 100)
    frame.bind("<rock>", callback)
    frame.pack()
     
    #   Rock beats Scissors
    #   Paper beats Rock
    #   Scissors beats Paper
    #   It's a tie if the computer and user chose the same object

    # If the user wins, increase win by 1
    # Use the output label to write what the computer did and what the result was (win, loss, tie)


# Use these functions as "command" for each button
def pass_s():
    get_winner("scissors")
def pass_r():
    get_winner("rock")
def pass_p():
    get_winner("paper")

window = tkinter.Tk()


#Variable to count the number of wins the user gets
win = 0

#START CODING HERE

# 1. Create 3 buttons for each option (rock, paper, scissors)
rock = tkinter.Button(
text = "Rock",
width = 15,
height = 5,
bg = "grey",
fg = "white",
)

paper = tkinter.Button(
text = "Paper",
width = 15,
height = 5,
bg = "grey",
fg = "white",
)

scissors = tkinter.Button(
text = "Scissors",
width = 15,
height = 5,
bg = "grey",
fg = "white",
)

rock.pack()
paper.pack()
scissors.pack()

# 2. Create 2 labels for the result and the number of wins
result = tkinter.Label(text = "result:")
userWins = tkinter.Label(text = "your wins: " + str(win))

result.pack()
userWins.pack()
# 3. Arrange the buttons and labels using grid

window.mainloop()
