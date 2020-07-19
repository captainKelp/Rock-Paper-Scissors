import random
import tkinter

#NOTE: A function that determines whether the user wins or not
#      Passes the user's choice (based on what button they click)to the parameter
window = tkinter.Tk()

def get_winner(call):
    buttons = rock, paper, scissors
    for button in buttons:
        if button is clicked(button):
            print(button)
            userChoice = str(button)


    # Access variables declared after the function so that the variables can be changed inside of the function
    global wins, win, output

    # 1. Create random integer 1-3 to use as computer's play
    computerChoice.randrange(1, 2, 3)

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

    #   Rock beats Scissors
    if (userChoice == "rock") & (computerChoice == "scissors"):
        win += 1
        outcome = "you win"
    #   Paper beats Rock
    if (userChoice == "paper") & (computerChoice == "rock"):
        win += 1
        outcome = "you win"
    #   Scissors beats Paper
    if (userChoice == "scissors") & (computerChoice == "paper"):
        win += 1
        outcome = "you win"
    #   It's a tie if the computer and user chose the same object
    if (userChoice == computerChoice):
        outcome = "you tied"
    else:
        outcome = "you lose"
    return outcome

    # If the user wins, increase win by 1
    # Use the output label to write what the computer did and what the result was (win, loss, tie)
    #this onyl has computer's choice
    #must include if you won, lost, or tied the current match
    #shouldn't there be a limit to matches before we get the final result and total wins label (located at the end of the program)
    output = tkinter.Label(row = 0, column = 1, text = computerChoice)

# Use these functions as "command" for each button
def pass_s():
    get_winner("scissors")
def pass_r():
    get_winner("rock")
def pass_p():
    get_winner("paper")

#Variable to count the number of wins the user gets
win = 0

#START CODING HERE


# 1. Create 3 buttons for each option (rock, paper, scissors)
def clicked(event):
    print("clicked at", event.x, event.y)

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

#binds Button CLicking Event to Buttons
rock.bind("<Button-1>", clicked)
paper.bind("<Button-1>", clicked)
scissors.bind("<Button-1>", clicked)

# 2. Create 2 labels for the result and the number of wins
stats = tkinter.Label(text = "result: " + outcome)
score = tkinter.Label(text = "score: " + str(win))


# 3. Arrange the buttons and labels using grid

#columns
window.columnconfigure(1, weight = 1, minsize = 25)
window.columnconfigure(2, weight = 1, minsize = 25)
window.columnconfigure(3, weight = 1, minsize = 25)

#rows
window.rowconfigure(0, weight = 1, minsize = 25)
window.rowconfigure(1, weight = 1, minsize = 25)

#buttons
rock.grid(row = 1, column = 1)
paper.grid(row = 1, column = 2)
scissors.grid(row = 1, column = 3)

#labels
stats.grid(row = 0, column = 2)
score.grid(row = 0, column = 3)

#for button in buttons:
#    frame = tkinter.Frame(
#        master = window,
#        relief = tkinter.RAISED,
#        borderwidth = 1
#    )
#    frame.grid(row = buttons, padx = 5, pady = 5)


window.mainloop()
