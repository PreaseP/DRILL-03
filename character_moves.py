from pico2d import *

open_canvas()

boy = load_image('character.png')


def move_top():
    print('Moving top')
    for x in range(0, 800):
        draw_boy(x, 550)
    pass


def move_right():
    print('Moving right')
    for y in range(550, 40, -1):
        draw_boy(770, y)
    pass


def move_bottom():
    print('Moving bottom')
    for x in range(800, 0, -1):
        draw_boy(x, 40)
    pass


def move_left():
    print('Moving left')
    for y in range(40, 550):
        draw_boy(30, y)
    pass


def move_rectangle():
    print("Moving rectangle")
    # move_top()
    # move_right()
    # move_bottom()
    move_left()
    pass


def move_circle():
    print("Moving circle")
    r = 200
    for deg in range(0, 360):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        draw_boy(x, y)
    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


def move_triangle():
    print("Moving triangle")
    pass


while True :
    # move_circle()
    move_triangle()
    # move_rectangle()
    break
    pass


close_canvas()
