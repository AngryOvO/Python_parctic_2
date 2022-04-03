## 모듈 삽입
import random

## 문자열에서 숫자만 추출하는 함수
def getNumber(strData):
    ## 임의의 문자열을 만들고
    numstr = ''
    ## 인자로 받은 문자열 크기만큼 반복
    for ch in strData:
        ## 문자열에 숫자가 있으면
        if ch.isdigit():
            ## 그 숫자를 새로 만든 문자열에 넣음
            numstr += ch

    ## 문자열에 저장된 숫자를 정수 형태로 리턴        
    return int(numstr)

## 선택정렬 알고리즘
def selectionsort(str1):

    i,j=0,0
    for i in range(0,len(str1)-1):
        for j in range(i+1,len(str1)):
            ## 여기서는 문자열에서 숫자를 추출한 새로운 문자열로 계산
            if getNumber(str1[i]) > getNumber(str1[j]):
                temp = str1[i]
                str1[i] = str1[j]
                str1[j] = temp


##2018038025 정하용
## 리스트와 변수 선언                
data = []
i = 0

## 10개의16진수의 랜덤값을 넣음
for i in range(0,10):
    tmp = hex(random.randrange(0,100000))
    ## 16진수의 앞 0x부분을 삭제
    tmp = tmp[2:]
    ## 리스트에 입력
    data.append(tmp)

## 출력
print('정렬 전 데이터 : ', end = '')
[print(num, end = ' ') for num in data]
## 정렬
selectionsort(data)
## 출력
print('\n정렬 후 데이터 : ', end='')
[print(num, end = ' ') for num in data]

