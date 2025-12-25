# import colorgram  #this is really cool, extracting colors from images.
#
# colors_rgb = []
# colors = colorgram.extract("image.jpg", 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors_rgb.append((r, g, b))
#
# print(colors_rgb)

import random # import random module used to randomly change turtle's color
import turtle as t # initializing the default settings for the turtle
t.speed("fastest") # this function allows me to set the turtle's speed
t.teleport(-250, -250) # moving turtle to optimal starting position
t.colormode(255) # making sure that the turtle module recognizes colors from 0 to 255, not 0 to 1 which is its default
t.hideturtle() # hides turtle to make presentation cleaner

color_list = [(236, 35, 108), (145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95), (220, 171, 45),
              (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91),
              (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35)]
# the above is the extracted list of colors from one of Hirst's dot paintings
# the code that extracted these colors is at the top of the file (hidden state)

for _ in range(10): # nested for-loop to make all 100 dots
    for num in range(10):
        t.dot(20, random.choice(color_list)) # dot function - makes dots. (size, color) are the inputs
        t.teleport(t.xcor()+50) # moves turtle to next dot placement without any trailing lines
    t.teleport(t.xcor()-500, t.ycor()+50) # moves turtle up to next row of dots to be drawn


screen = t.Screen()
screen.exitonclick()