from pico2d import *
import math

open_canvas()

# 이미지 로드
grass = load_image('grass.png')
boy = load_image('character.png')

def draw_background():
    """배경(잔디) 그리기"""
    grass.draw(400, 30)

def draw_boy(x, y):
    """캐릭터를 지정된 위치에 그리기"""
    clear_canvas_now()
    draw_background()
    boy.draw_now(x, y)
    delay(0.01)

def move_rectangle():
    """사각형 운동 - 화면 가장자리를 따라 시계방향으로 이동"""
    print("사각형 운동 시작")

    # 상단 이동 (왼쪽에서 오른쪽으로)
    for x in range(50, 750, 5):
        draw_boy(x, 550)

    # 우측 이동 (위에서 아래로)
    for y in range(550, 100, -5):
        draw_boy(750, y)

    # 하단 이동 (오른쪽에서 왼쪽으로)
    for x in range(750, 50, -5):
        draw_boy(x, 100)

    # 좌측 이동 (아래에서 위로)
    for y in range(100, 550, 5):
        draw_boy(50, y)

def move_circle():
    """원 운동 - 화면 중앙을 중심으로 원형 이동"""
    print("원 운동 시작")

    center_x = 400
    center_y = 300
    radius = 200

    # 360도 회전하며 원 운동
    for degree in range(0, 360, 3):
        radian = math.radians(degree)
        x = center_x + radius * math.cos(radian)
        y = center_y + radius * math.sin(radian)
        draw_boy(x, y)

def main():
    """메인 함수 - 사각형 운동과 원 운동을 무한 반복"""
    try:
        while True:
            # 사각형 운동 실행
            move_rectangle()

            # 원 운동 실행
            move_circle()

    except KeyboardInterrupt:
        print("프로그램이 중단되었습니다.")

    close_canvas()

if __name__ == "__main__":
    main()
