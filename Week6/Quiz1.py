# 인터넷 게임 계정의 수를 입력 받은 후,
# 각 계정의 아이디, 승률, 계급을 입력 받아,
# 계급이 'Bronze' 가 아니면서 승률이 60.0 이상이거나,
# 계급이 'Platinum' 인 아이디를 입력 받은 순서대로
# 출력 예와 같은 형식으로 "[Gosu]" 를 붙여 출력하는 프로그램을 작성하시오.

idNum = int(input("인터넷 게임 계정의 수를 입력해 주세요 : "))
idAry = []

for x in range(idNum):  # 게임 계정의 수만큼 어레이 만들기 위해
    idInfo = input("각 계정의 아이디, 승률, 계급을 입력해 주세요 : ")
    splInfo = idInfo.split()  # 각 항목을 서로 비교하기 위해
    idAry.append(splInfo)  # 어레이에 정보를 담아줌
    if ((idAry[x][2] != 'Bronze') and (float(idAry[x][1]) >= 60.0)) or (idAry[x][2] == 'Platinum'):  # 조건에 맞으면 고수로 인정해 줌
        print("[Gosu]", idAry[x][0])
