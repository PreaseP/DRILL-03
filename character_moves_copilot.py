from pico2d import *
import math

# 화면 초기화
open_canvas(800, 600)
character = load_image('character.png')

def draw_character(x, y):
    """캐릭터를 그리는 함수"""
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.02)

def square_movement():
    """사각운동을 하는 함수"""
    print("사각운동 시작")

    # 하단 좌→우
    for x in range(100, 701, 5):
        draw_character(x, 100)

    # 우측 하→상
    for y in range(100, 501, 5):
        draw_character(700, y)

    # 상단 우→좌
    for x in range(700, 99, -5):
        draw_character(x, 500)

    # 좌측 상→하
    for y in range(500, 99, -5):
        draw_character(100, y)

def triangle_movement():
    """삼각운동을 하는 함수"""
    print("삼각운동 시작")

    # 밑변: 좌하→우하
    for x in range(150, 651, 5):
        draw_character(x, 150)

    # 우변: 우하→상점
    steps = 100
    for i in range(steps + 1):
        x = 650 - (i * 250 // steps)
        y = 150 + (i * 250 // steps)
        draw_character(x, y)

    # 좌변: 상점→좌하
    for i in range(steps + 1):
        x = 400 - (i * 250 // steps)
        y = 400 - (i * 250 // steps)
        draw_character(x, y)

def circle_movement():
    """원운동을 하는 함수"""
    print("원운동 시작")

    center_x, center_y = 400, 300
    radius = 150

    for angle in range(0, 360, 3):
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        draw_character(x, y)

# 메인 실행 부분
def main():
    """메인 함수 - 무한 반복"""
    try:
        while True:
            square_movement()
            triangle_movement()
            circle_movement()
    except KeyboardInterrupt:
        print("프로그램 종료")
    finally:
        close_canvas()

if __name__ == "__main__":
    main()

# insert for final commit
