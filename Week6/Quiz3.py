# 정수를 입력받아 입력받은 정수만큼 반복하면서, 각 줄에 나라의 이름과 그 나라의 수도를 공백을 사이에 두고 입력받는다.
# 그 후에, 나라의 이름을 입력받아 그 나라의 수도를 출력하는 프로그램을 작성하라.
# 만약 나라가 입력된 적이 없으면, Unknown Country 를 출력한다.

num = int(input("반복 횟수를 나타낼 정수를 입력해 주세요 : ")) # 입력받은 정수만큼 반복
capOfCntry = dict() # 나라와 수도를 담아 줄 딕셔너리

for x in range(num):
    insert = input("나라의 이름과 그 나라의 수도를 입력해 주세요 : ")
    spl = insert.split() # 나라와 수도를 나눠줌
    country = spl[0] # 나라와 수도 각각 담아줌, 이 경우에는 나라의 이름이 key
    capital = spl[1] # 수도의 이름이 해당 key 의 값이 된다.

    capOfCntry[country] = capital # 딕셔너리에 저장

insertCntry = input("수도를 알고 싶은 나라를 입력해 주세요 : ")
if insertCntry in capOfCntry: # 만약 알고 싶은 나라가 딕셔너리에 있다면
    print(capOfCntry.get(insertCntry, "Unknown Country")) # 그 나라(key)에 대응되는 수도의 이름(값)을 알려준다.


