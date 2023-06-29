/*
주어진 코드는 임의의 이미지를 흑백으로 변환하는 작업을 수행합니다.

이 코드가 NumPy를 활용하도록 수정하여, 임의의 이미지를 3색 포스터로 변환하는 작업을 수행하도록 만드세요:

밝은 픽셀은 노랑,
어두운 픽셀은 파랑,
중간쯤의 픽셀은 초록.
밝기를 위한 기준치는 자유롭게 설정해도 됩니다. 아래 예시는 255의 1/3값과 2/3값을 쓰고 있습니다.
*/

  # 예시답안

  from cs1media import *
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
# This code converts an image into a black & white poster.
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# 별도의 이미지를 업로드하여 사용하세요
pix = Image.open("kfp.png")
pix.show()
pix = np.array(pix)

# 한 픽셀을 3색 중 하나로 변환
def per_pixel_process(px):
    #print(px);return
    #avg = int(np.mean(px))
    if px >= 255.0*2/3:
        return yellow
    elif px >= 255.0*1/3:
        return green
    else:
        return blue

# 이미지->array로 변환
# array를 per_pixel_process의 인자로 주면
# 반환되는 array가 per_pixel_process 연산이
# 모든 픽셀에 적용된 결과물임
vec_per_pixel_process = np.vectorize(per_pixel_process)
means = np.mean(pix, axis=-1)

three_colorized = np.array(vec_per_pixel_process(means))
# 중간중간 .shape 변수를 출력하여 transpose가 왜 필요한지 생각해봅시다
# tranpose는 참고로 튜플을 인자로 받는데
# 아래처럼 (1, 2, 0)이라 쓰이면
# 0번째 축을 1번째로 대체하고,
# 1번째 축을 2번째로 대체하고,
# 2번째 축을 0번째로 대체합니다
# shape로 꼭 의미를 확인해보세요
# 해설이 필요할 경우 꼭 질문 주세요
reshaped = three_colorized.transpose((1, 2, 0))

pltimg = plt.imshow(reshaped)
plt.show()
