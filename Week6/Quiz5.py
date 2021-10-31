# 주차장에 세워진 자동차의 차종을 모두 입력 받아, 중복되어 입력된 이름을 제거한 후,
# 알파벳 순서대로 출력하고, 그 개수를 출력하는 프로그램을 작성하시오.

car = input("주차장에 세워진 자동차의 차종을 입력하세요 : ") # 자료형 str
spl = car.split() # 띄어쓰기로 쪼개진 차 이름들이 담긴 list
carSet = set(spl) # set 로 만들어서 중복 제거
carSort = list(carSet) # 알파벳 순서로 sort 하기 위해서 list 로 다시 변환
carSort.sort() # 변환된 리스트를 sort

for carName in carSort: # 어차피 carSort 에는 중복된 이름이 없으므로 그냥 전체 반복, 순서도 정렬 되어 있음
    print(carName, end=' ') # 그대로 출력, 출력 예와 똑같이 나오게 하기 위해 개행 없이 띄어쓰기로 끝나게했는데 조금 더 깔끔한 방법이 있지 않을까...
print() # 출력 예와 똑같이 나오게 하기 위해... 반복문에서의 출력문이 개행되지 않으므로 별도로 다시 개행시켜 줌
print(len(carSort)) # carSrot 에는 중복된 이름이 없으므로 리스트의 크기가 곧 중복되지 않은 자동차 이름의 개수이다.

# Grandeur Avante Sonata Sonata Avante Genesis Sonata