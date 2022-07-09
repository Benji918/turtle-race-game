from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=1000, height=400)
user_bet = screen.textinput(title='Input your bet please', prompt='Which turtle will win the race? Enter a color.')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_coordinates = [-70, -30, 0, 30, 70, 100]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-480, y=-y_coordinates[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    import random
    for turtle in all_turtles:
        if turtle.xcor() > 480:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f'You chose {user_bet}, the winning turtle was {winning_color} you won!')
            else:
                print(f'You lose bitch, {winning_color} won!')
        if turtle.xcor() == 480:
            is_race_on = False
            print(f'{turtle.color()} tied with {turtle.color}!')

        random_pacing = random.randint(0, 10)
        turtle.forward(random_pacing)










screen.exitonclick()
