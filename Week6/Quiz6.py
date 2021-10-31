# 정수를 입력 받아 정수 만큼 반복하면서, 키-자료 쌍을 공백을 사이에 두고 입력 받아 딕셔너리에 추가한다.
# 마지막으로 문자열을 하나 더 입력 받아, 그 문자열을 키 값으로 하는 자료를 출력하는 프로그램을 작성하시오.
# (동일한 키 값이 두 번 입력되는 경우는 없다고 가정한다.)

tempoDict = dict()

num = int(input("반복 횟수를 나타낼 정수를 입력해 주세요 : "))

for x in range(num):
    insertInfo = input("템포의 이름과 속도를 입력해 주세요 : ") # 자료형 str
    spl = insertInfo.split() # 띄어쓰기 기준으로 나눠줌. 자료형 list
    tempoName = spl[0]  # key 값이 될 템포의 이름을 담아줌
    tempoSpeed = spl[1]  # value 값이 될 템포의 속도를 담아줌
    tempoDict[tempoName] = tempoSpeed  # 딕셔너리에 저장

insertTempo = input("속도를 알고 싶은 템포의 이름을 입력해 주세요 : ")
print(tempoDict[insertTempo])