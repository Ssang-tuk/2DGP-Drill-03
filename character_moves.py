from pico2d import *

open_canvas()

boy = load_image('character.png')


def move_top():
    print('Moving top')
    for x in range(0, 780, 5):
        draw_boy(x, 550)
    pass


def move_right():
    print('Moving right')
    for y in range(550, 50, -5):
        draw_boy(780, y)
    pass

def move_bottom():
    print('Moving bottom')
    for x in range(780, 0, -5):
        draw_boy(x, 50)
    pass


def move_left():
    print('Moving left')
    for y in range(50, 550, 5):
        draw_boy(20, y)
    pass

def move_rectangle():
    print("Moving rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass


def move_circle():
    print("Moving circle")
    r = 200
    for deg in range(0, 360, 3):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        draw_boy(x, y)
    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


def move_top_triangle():
    print("Moving top triangle")
    for x in range(0, 780, 5):
        draw_boy(x, 550)
    pass


def move_down_triangle():
    print("Moving down triangle")
    x, y = 780, 550
    while x > 400 and y > 50:
        draw_boy(x, y)
        x -= 4
        y -= 5
    pass


def move_up_triangle():
    print("Moving up triangle")
    x, y = 400, 50
    while x > 0 and y < 550:
        draw_boy(x, y)
        x -= 4
        y += 5
    pass


def move_triangle():
    print("Moving triangle")
    move_top_triangle()
    move_down_triangle()
    move_up_triangle()
    pass


while True:
    move_rectangle()
    move_triangle()
    move_circle()



close_canvas()
