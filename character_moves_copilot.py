from pico2d import *
import math

open_canvas()

boy = load_image('character.png')


def move_top():
    print('Moving top')
    for x in range(0, 800, 5):
        draw_boy(x, 550)


def move_right():
    print('Moving right')
    for y in range(550, 50, -5):
        draw_boy(795, y)


def move_bottom():
    print('Moving bottom')
    for x in range(795, 0, -5):
        draw_boy(x, 50)


def move_left():
    print('Moving left')
    for y in range(50, 550, 5):
        draw_boy(5, y)


def move_rectangle():
    print("Moving rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()


def move_circle():
    print("Moving circle")
    r = 200
    for deg in range(0, 360, 2):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        draw_boy(x, y)


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


# 사각운동 후 원운동 실행
move_rectangle()
move_circle()

close_canvas()
