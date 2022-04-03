import operator

## 문자열 입력 받음
string1 = input("문자열을 입력하세요 :")


##2018038025 정하용

##딕셔너리와 리스트 선언
countstrdic = {}
countstr = []



## ch라는 변수를 string1의 크기만큼 반복
for ch in string1:

    ## 만약 ch가 한글이면
    if 'ㄱ' <= ch  and ch <= '힣':
        ## ch가 countstrdic 안에 있으면
        if ch in countstrdic :
            ##countstrdic의 ch인덱스의 값을 1 더함
            countstrdic[ch] += 1
            ## 없으면 키값을 다시 1로 만듬
        else:
            countstrdic[ch] = 1

## countstr 리스트에 내림차순으로 정렬한 countstrdic을 저장
countstr = sorted(countstrdic.items(), key = operator.itemgetter(1), reverse = True)

## 출력구간
print('원문\n', string1)
print('---------------------')
print('문자\t빈도수')
print('---------------------')
for i in range(0, len(countstr)):
    print(countstr[i][0], '\t', countstr[i][1])
