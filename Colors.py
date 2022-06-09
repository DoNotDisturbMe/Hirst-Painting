import random
import colorgram
import turtle
from turtle import Turtle

rgb_color = []
color = colorgram.extract('colouring.jpg', 38)
for colors in color:
    r = colors.rgb.r
    g = colors.rgb.g
    b = colors.rgb.b
    list = (r,g,b)
    rgb_color.append(list)
print("RGB",rgb_color)


turtle.colormode(255)
timm = Turtle()
timm.penup()
timm.hideturtle()
# color_name = [(246, 242, 235), (247, 240, 244), (239, 242, 247), (237, 245, 240), (212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220), (97, 127, 168), (34, 81, 49), (180, 188, 210), (84, 65, 30), (16, 77, 106)]

turtle.setheading(0)
turtle.forward(300)
turtle.setheading(0)


number_of_dots = 100

for dot_count in range(1, number_of_dots):
    timm.dot(28, random.choice(rgb_color))
    timm.forward(50)
    if dot_count % 10 == 0:
        timm.setheading(50)
        timm.forward(90)
        timm.setheading(180)
        timm.forward(500)
        timm.setheading(0)



