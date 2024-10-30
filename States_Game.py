from turtle import Turtle , Screen
from Pandas_States import States
from TurtleHandling import Marker

# setting up the screen
IMAGE = "./blank_states_img.gif"
screen = Screen()
screen.title("U.S States Game")
screen.setup(725,491)
screen.addshape(IMAGE)
turtle = Turtle()
turtle.shape(IMAGE)

#setting up the classes
marker = Marker()
states = States()

#setting up the game loop
known_states = []
correct_guesses = 0

while correct_guesses < 50:
    guess_state = screen.textinput(f"{correct_guesses}/50 Names Guessed Correct" , "Enter Another State's Name").title()
    if guess_state not in known_states:
        if states.is_in_states(guess_state):
            coordinates = states.get_coordinates(guess_state)
            marker.mark(guess_state , coordinates)
            known_states.append(guess_state)
            correct_guesses += 1

    if guess_state == "Exit":
        missing_states = states.get_missing_file(known_states)
        print(missing_states)
        break
screen.mainloop()