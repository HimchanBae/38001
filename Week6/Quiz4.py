# 매 년 피아노 콩쿠르 최우수상을 받은 학생들의 이름과 정수 하나를 입력 받아,
# 입력받은 정수 만큼 최우수상을 받은 학생들을 모두 출력하는 프로그램을 작성하시오.
# (먼저 입력된 이름을 우선하여 출력한다.)

# < for item in list> 와 <for i in range(len(list))> 의 차이는?
from collections import Counter # collections 모듈의 Counter 클래스를 사용

name = input("최우수상을 받은 학생들의 이름을 입력해 주세요 : ") # 자료형 str
nameAry = name.split() # 띄어쓰기로 쪼개진 학생들의 이름이 담긴 list

countTable = Counter(nameAry) # Counter 클래스는 자동으로 중복된 원소들을 묶고 개수를 알려주는 딕셔너리형으로 저장된다.

n = int(input("최우수상을 n번 받은 학생들의 이름을 알고싶다면 정수 n을 입력해 주세요 : "))

for studentName, time in countTable.items():
    if time == n:
        print(studentName) # 반복문이 돌아가면서 값(value)이 n인 이름을 차례대로 찾아내므로 입력된 순서대로 출력된다.
