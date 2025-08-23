import turtle
import random

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Catch the Turtle")
FONT = ("Arial", 25, "normal")
score = 0
game_over = False
time_left = 10

#turtle list
turtle_list = []

turtle.hideturtle()

#score turtle
score_turtle = turtle.Turtle()

#coutdown turtle
countdown_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.8

    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score 0", move=False, align="center", font=FONT)


def make_turtle(x, y):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.goto(x * 10, y * 10)

    kind = random.choice(["normal", "bonus", "penalty"])
    if kind == "bonus":
        t.color("gold")
    elif kind == "penalty":
        t.color("red")
    else:
        t.color("dark green")

    def handle_click(x, y):
        global score, time_left
        if kind == "normal":
            score += 1
            time_left += 0.5
        elif kind == "bonus":
            score += 5
            time_left += 2
        elif kind == "penalty":
            score -= 3
            time_left -= 2

        if time_left <= 0:
            time_left = 0
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)

    t.onclick(handle_click)
    turtle_list.append(t)

x_coordinates = [-30, -15, 0, 15, 30]
y_coordinates = [-20, -10, 0, 10, 20]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        chosen = random.choice(turtle_list)

        kind = random.choices(
            ["normal", "bonus", "penalty"],
            weights=[70, 20, 10],
            k=1
        )[0]
        if kind == "bonus":
            chosen.color("gold")
        elif kind == "penalty":
            chosen.color("red")
        elif kind == "normal":
            chosen.color("dark green")

        chosen.showturtle()

        speed = max(200, 800 - (score * 30))
        screen.ontimer(show_turtles_randomly, speed)

def countdown():
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.8
    countdown_turtle.setpos(0, y - 30)
    countdown_turtle.clear()

    if time_left > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time_left), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over", move=False, align="center", font=FONT)

def start_game():
    turtle.tracer(0)

    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown()

    turtle.tracer(1)

start_game()
turtle.mainloop()