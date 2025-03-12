import turtle
import random
import time


screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Random Walk Simulation with Turtle")
screen.bgcolor("white")


axis = turtle.Turtle()
axis.speed(0)
axis.color("black")
axis.penup()
axis.hideturtle()
axis.goto(-350, 0)
axis.pendown()
axis.goto(350, 0)
axis.penup()
axis.goto(360, -10)
axis.write("X-axis", font=("Arial", 12, "bold"))
axis.goto(0, -250)
axis.pendown()
axis.goto(0, 250)
axis.penup()
axis.goto(10, 260)
axis.write("Y-axis", font=("Arial", 12, "bold"))


car = turtle.Turtle()
car.shape("arrow")
car.color("red")
car.speed(1)


F_L_R = [0.5, 0.3, 0.2]
F_L_R = [int(10 * i) for i in F_L_R]
step_limit = 20
step_size = 20

car.penup()
car.goto(0, 0)
car.pendown()


for step in range(step_limit):
    rn = random.randint(0, 9)
    if rn in range(F_L_R[0]):
        car.setheading(90)
    elif rn in range(F_L_R[0], F_L_R[0] + F_L_R[1]):
        car.setheading(180)
    else:
        car.setheading(0)

    car.forward(step_size)
    time.sleep(0.2)

screen.mainloop()
