from pico2d import *
import math

# 초기화
open_canvas()

# 이미지 로드
character = load_image('character.png')
grass = load_image('grass.png')

def draw_rectangle():
    global x, y
    print("Drawing rectangle")

    # 시작 위치 (왼쪽)
    x, y = 0, 90

    # 오른쪽으로 이동
    for x in range(0, 800+1, 10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

    # 위로 이동
    for y in range(90, 550+1, 10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

    # 왼쪽으로 이동
    for x in range(800, 0-1, -10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

    # 아래로 이동
    for y in range(550, 90-1, -10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

    # 다시 오른쪽으로 이동해서 중앙으로
    for x in range(0, 400+1, 10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

def draw_circle():
    print("Drawing circle")
    # 원의 중심과 반지름
    cx, cy = 400, 300
    r = 200

    for deg in range(0, 360+1, 5):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

    # 원운동 후 중앙으로 복귀
    for i in range(0, 10+1):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(cx, cy)
        delay(0.01)

# 메인 게임 루프
while True:
    draw_rectangle()
    draw_circle()
