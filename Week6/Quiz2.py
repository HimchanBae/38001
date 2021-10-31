# 세 리스트를 입력받은 후, 모두 셋으로 형변환한 후,
# 세 집합의 교집합과 합집합을 구하여 출력하는 프로그램을 작성하시오.

intAry = [] # 정수로 이루어진 리스트
interAry = set() # 합집합을 구하기 위한 세트
unionAry = set() # 교집합을 구하기 위한 세트

for x in range(3):
    intList = input("정수로 이루어진 리스트를 입력해 주세요 : ")
    splInt = intList.split() # 띄어쓰기 기준으로 쪼개줌
    setInt = set(splInt) # 자료형은 문자열이지만 사실은 숫자인 어레이 리스트를 세트로 형변환 {'3', '6', '9'}
    intAry.append(setInt) # 세트인 원소로 이루어진 세트 리스트가 만들어짐 [{}, {}, {}]
    # 교집합은 반복문 안에서 어떻게 바로 비교해줄지 모르겠음 ㅜㅜ
    unionAry = setInt | unionAry # 합집합을 담아줌

interAry = intAry[0] & intAry[1] & intAry[2] # 교집합을 담아줌

interAry = {int(i) for i in interAry} # 자료형이 문자열이라 정수형으로 형변환 시켜서 다시 담아줌
unionAry = {int(i) for i in unionAry} # 자료형이 문자열이라 정수형으로 형변환 시켜서 다시 담아줌

print("Intersection:", interAry)
print("Union:", unionAry)

