## 모듈 삽입 구간
import turtle
import random
import math
from tkinter.simpledialog import *

## 변수 선언구간
inStr = ''
## 조건에서 제시한 크기 500 500
swidth, sheight = 500, 500
## 글자크기 20
tX, tY, txtSize = 0,0,20
## 반지름 200
radius, angle, radian = 200, 0, 0

turtle.title('거북이로 나선형 모양으로 글자쓰기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)	 
turtle.penup()

## 2018038025 정하
inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')

## 각도는 360 나누기 문자열의 길이
angle = 360  / len(inStr)

## 입력받은 문자열만큼 반복
for ch in inStr :

    ## 라디안 값 지정
    radian = 3.14 * angle / 180

    ## x좌표와 y좌표 힌트에 나온 만큼 지정
    tX = radius * math.cos(radian)
    tY = radius * math.sin(radian)
    ## 색깔은 랜덤
    r = random.random(); g = random.random(); b = random.random()

    ## 거북이 좌표따라
    turtle.goto(tX, tY)
	
    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은고딕', txtSize, 'bold'))
    ## 두바퀴를 돌것이므로 각도를 두배로 설정
    angle += 360 * 2 / len(inStr)
    ## 나선형이기 때문에 반지름을 초기값 200에 입력받은 문자열의 길이만큼 나눠서 빼줌
    radius -= 200 /len(inStr)

turtle.done()
