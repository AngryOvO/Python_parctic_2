## 함수 선언구간
def upstring (op) :
    ## ups라는 변수에 인자로 받은 문자를 대문자화 시켜서 저장
    ups = op.upper()
    ## ups 리턴
    return ups
    
def downstring (op):
    ## downs라는 변수에 인자로 받은 문자를 소문자화 시켜서 저장
    downs = op.lower()
    ## downs 리턴
    return downs


## 2018038025 정하용

## 메인함수
a = input("문자열을 입력하세요 :") ## 문자열 입력 받음
c = '' 

## 받은 문자열의 크기만큼 반복
for i in range(0,len(a)):
    ## 만약 문자열의 i번째 문자가 대문자라면
    if a[i].isupper() == True:
        ## 그 문자를 소문자화 시키고 c에 저장
        c += downstring(a[i])
    ## 반대로 문자열의 i번째 문자가 소문자라면
    else:
        ## 그 문자를 대문자화 시키고 c에 저장
        c += upstring(a[i])

## 루프를 통과한 c 출력
print(c)    
