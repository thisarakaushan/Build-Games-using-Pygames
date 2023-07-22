# Build the Pygames

[Pygame](https://www.pygame.org/news) is a python wrapper for SDL– a cross-platform C library for controlling multimedia, written by Pete Shinners.It is a wrapper around the SDL (Simple DirectMedia Layer) library. What this means is that, using pygame, you can write games or other multimedia applications in Python that will run unaltered on any of SDL's supported platforms (Windows, Unix, Mac, BeOS and others).

In this section we indroduce the basics of pygamefunctions without defining classes and objects.

## Requiremts

python3 -m pip install -U pygame

## Pygame

Python module developed for writing gamews in python. It is a cross platform. Python is written on top of the simple DirectMedia Layer, wrappers around OS fuctions.
That will run unaltered on any of SDL's supported platforms (Windows, Unix, Mac, BeOS and others). It can be used for Multimedia Development. Pygame is distributes with python.

### Key takeaways 

The Pygame import statement is always placed at the beginning of the program. It imports the pygame classes,methods and attributes into the current name space. 
Now this new methods can be called via pygame.method().

For exemple we can now initialize or quit pygame with the following command:
pygame.init()
pygame.quit()

The function display.set_mode() sets the screen size. It returns a Surface object wich we assign to the variable screen. This variable will be one of the most used variables. It represents the window we see:

screen = pygame.display.set_mode((640, 240))

You can now run this program and test it. At this moment it does very little. It opens a window and closes it immediately

Pygame will register all events from the user into an event queue which can be received with the code pygame.event.get(). Every element in this queue is an Event object and they'll all have the attribute type, which is an integer representing what kind of event it is. In the pygame module there are predefined integer constants representing the type. Except for this attribute, events have different attributes.

Mainly we work with the events in the pygame.

### Event Types

1. Quit - none
2. Activeevent - gain, state
3. Keydown - unicode, key, mod
4. Keyup - key, mod
5. Mousemotion - pos, rel, buttons
6. Mousebuttonup - pos, button
7. Mousebuttondown - pos, button
8. Joyaxismotion - joy, axis, value
9. Joyballmotion - joy, ball, rel
10. Joyhatmotion - joy, hat, value
11. Joybuttonup - joy, button
12. Joybuttondown - joy, button
13. Videoresize - size, w, h
14. VideoExpose - none
15. Userevent - code

* Pygame handles all its events messaging through an event queue.

To handle our events we simply loop through the queue, check what type it is (with the help of the predefined constants in the pygame module) and then perform some action. This code will check if the user has pressed the close button on the top corner of the display, and if so terminate the program.

for event in pygame.event.get():

    if event.type == pygame.QUIT:
        # Close the program any way you want, or troll users who want to close your program.
        raise SystemExit

Example : 
for event in pygame.event.get():

    if event.type == pygame.QUIT:  # Close your program if the user wants to quit.
        raise SystemExit
    elif event.type == pygame.MOUSEMOTION:
        if event.rel[0] > 0:  # 'rel' is a tuple (x, y). 'rel[0]' is the x-value.
            print("You're moving the mouse to the right")
        elif event.rel[1] > 0:  # pygame start y=0 at the top of the display, so higher y-values are further down.
            print("You're moving the mouse down")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            print("You pressed the left mouse button")
        elif event.button == 3:
            print("You pressed the right mouse button")
    elif event.type == pygame.MOUSEBUTTONUP:
        print("You released the mouse button")

To use the module you first need to import and initialize pygame correctly and set a mode for the display. It's convenient to define color constants in advance, making your code more readable and more beautiful. All functions takes a Surface to draw on, a color and a position argument that's either a pygame Rect or a 2-element integer/float sequence (the pygame.draw.circle will only take integers because of undefined reasons

The code below will showcase all the different functions, how they are used and how they look. We'll initialize pygame and define some constants before the examples.

import pygame
from math import pi
pygame.init()

screen = pygame.display.set_mode((100, 100))
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0) 

The black color is the Surface default color and represents the part of the Surface that hasn't been drawn onto. The parameters of each function is explained down below at Parameters .

* Rect

size = (50, 50)

rect_border = pygame.Surface(size)  # Create a Surface to draw on.
pygame.draw.rect(rect_border, RED, rect_border.get_rect(), 10)  # Draw on it.

rect_filled = pygame.Surface(size)
pygame.draw.rect(rect_filled, RED, rect_filled.get_rect()) 



