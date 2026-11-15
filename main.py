from turtle import Turtle, Screen

import pandas

from scoreboard import Scoreboard

TOTAL_STATES = 50

screen = Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
map_turtle = Turtle()
map_turtle.shape(image)

data = pandas.read_csv("50_states.csv")
score = Scoreboard()

writer = Turtle()
writer.penup()
writer.hideturtle()

correct_guesses = []

while score.score != TOTAL_STATES:
    answer = screen.textinput(
        title=f"{score.score}/{TOTAL_STATES} states correct",
        prompt="What's another state's name? (type 'exit' to quit)",
    )

    # cancel gives None, so it ends the game the same way as typing exit
    if answer is None or answer.strip().lower() == "exit":
        missing_states = [state for state in data.state if state not in correct_guesses]
        pandas.DataFrame({"state": missing_states}).to_csv("states_to_learn.csv", index=False)
        break

    guess = answer.strip().title()
    row = data[data.state == guess]

    if row.empty:
        print("wrong guess")
        continue

    state_name = row.state.item()
    if state_name in correct_guesses:
        print("you already guessed that state")
        continue

    print("good guess")
    writer.goto(row.x.item(), row.y.item())
    writer.write(state_name)
    correct_guesses.append(state_name)
    score.got_point()

if score.score == TOTAL_STATES:
    score.YOU_WON()
    screen.exitonclick()
