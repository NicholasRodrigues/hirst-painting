# import colorgram

# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 30)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors. append(new_color)
# print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64),
              (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58),
              (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216),
              (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]
jack = turtle_module.Turtle()

jack.hideturtle()
jack.speed(0)
jack.penup()
jack.setheading(225)
jack.forward(300)
jack.setheading(0)
num_of_dots = 100

for dot_count in range(1, (num_of_dots + 1)):
    jack.dot(20, random.choice(color_list))
    jack.forward(50)
    if dot_count % 10 == 0:
        jack.setheading(90)
        jack.forward(50)
        jack.setheading(180)
        jack.forward(500)
        jack.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
