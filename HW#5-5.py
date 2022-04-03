# 모듈 삽입
from time import*
from datetime import*

## 하루를 세는 기능을 가진 함수
def daycount(day1, day2):
    retDays = 0
    year, month, day = day1.split('/')
    sDay = date(int(year), int(month), int(day))
    year, month, day = day2.split('/')
    eDay = date(int(year), int(month), int(day))
    diffDays = eDay - sDay
    retDay = diffDays.days
    return retDay

## 2018038025 정하

##  요일을 세는 함수
def dayget(t):
    weeks = ['월', '화', '수', '목', '금', '토', '일']
    return weeks[t.tm_wday]

## 변수 선언구간
startday, curday, tm = '','',None
## 원하는 날짜 입력받음
startday = input('시작 날짜 (연/월/일)  : ')
## tm에는 현재의 날짜를 입력받음
tm = localtime()
curday = str(tm.tm_year) + '/' + str(tm.tm_mon) + '/' + str(tm.tm_mday)
## 출력
print(startday, '부터 오늘(', curday, ')까지는 ', daycount(startday,curday), '일이 지났습니다')
print('그리고 오늘은', dayget(tm), '요일입니다')
    
