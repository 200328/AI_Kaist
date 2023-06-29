from cs1robots import *
import time

create_world(avenues = 5, streets = 4)  #avenues = 가로, streets = 세로
hubo = Robot(beepers = 10)  #Robot 클래스의 인스턴스(카피) 만들기 (Robot이 beepers 10개를 가지고 있음)
sleep_time = 0.5

def dance():
    for i  in range(4):
        time.sleep(sleep_time)
        hubo.turn_left()

def move_or_turn():
    if hubo.front_is_clear():
        dance()
        time.sleep(sleep_time)
        hubo.move()
    else:
        time.sleep(sleep_time)
        hubo.turn_left()
        time.sleep(sleep_time)
        hubo.drop_beeper()  #노란공 내려놓기

for i in range(18): 
    move_or_turn()
