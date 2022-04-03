## 2018038025 정하용
## 함수 선언구간
## 입력 받을 숫자와 진법 인자로 받음
def change(num, div):
    ## 결과값을 저장할 리스트 생성
    result = []
    ## 각 변수에 인자값 저장
    q, r = num, div
    while q > 0:
        q, r = divmod(q, div)
        if r > 10:
            ## 10~ 16사이의 숫자에 해당하는 알파벳 입력
            _remain = 'ABCDEF'
            r = _remain[r-10]
            result.append(str(r))
    ## 출
    print("%d진수 : "%div,''.join(result[::-1]))

## input
n = int(input("10진수 입력 -->"))

## 함수 실행
change(n,2)
change(n,8)
change(n,16)

