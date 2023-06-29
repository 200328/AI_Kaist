from cs1robots import *
import time

load_world("./worlds/amazing2.wld")
hubo = Robot(beepers = 10)
# 객체의 카피 하나 만들기 (이름 hubo)
# 버퍼 10개를 가지고 "태어남"

hubo.set_trace("blue")
#지나가는 길에 파란 발자취 남기기

sleep_time = 0.5

def turn_right():
  for i in range(3):
    hubo.turn_left()

#---------------------------------------------------
# print(hubo.__dir__())
# print("right_is_clear" in hubo.__dir__())
time.sleep(sleep_time)
hubo.drop_beeper()
time.sleep(sleep_time)
#hubo.move()
timeout = 4  # 4번의 기회가 있다

while not hubo.front_is_clear() and timeout > 0: #앞이 막혀있을 때
    hubo.turn_left()
    timeout -= 1

if timeout == 0:
    print("all sides are blocked!")
else:
    hubo.move()

while not hubo.on_beeper():
    # 만약 오른쪽 clear
    # 오른쪽으로 회전
    # 전진
    # elif 앞이 clear라면
    # 전진
    # else
    # 왼쪽으로 회전
  if hubo.front_is_clear():
    time.sleep(sleep_time)
    hubo.move()
  else:
    time.sleep(sleep_time)
    hubo.turn_left()
