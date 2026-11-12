from turtle import Turtle, Screen
import pandas
from scoreboard import Scoreboard

t = Turtle()
screen = Screen()
score = Scoreboard()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

data =  pandas.read_csv("50_states.csv")
# states = data["state"]
# print(states)

score = Scoreboard()


correct_list= []



while score.score !=50:
    score.update_score_display()
    timmy = Turtle()
    timmy.penup()
    timmy.hideturtle()


    answer_state = screen.textinput(title=f"{score.score}/50 correct gueesses", prompt="What's another state's name?")
    if answer_state == "exit":

        # missing_states = []
        # for state in data.state:
        #     if state not in correct_list:
        #         missing_states.append(state)



        missing_states = [state  for state in data.state if state not in correct_list]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # print(answer_state)
    captilized_answer= answer_state.title()
    # print(captilized_answer)
    # monday =data[data.day == "Monday"]

    correct_or_not =data[data.state == captilized_answer]
    if correct_or_not.empty:
        print("wrong guess")
        continue

    else:
        for j in correct_list:
            if j == correct_or_not.state.item():
                print("you already guessed that state")
                break
        else:

            print("good guess")

            x=correct_or_not.x.item()
            y=correct_or_not.y.item()
            timmy.goto(x,y)
            timmy.write(correct_or_not.state.item())
            correct_list.append(correct_or_not.state.item())
            score.got_point()
    # print(correct_or_not)




# screen.mainloop()