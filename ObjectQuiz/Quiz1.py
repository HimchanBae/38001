class Account:
    def __init__(self, account="441-0290-1203", balance=500000, interestRate=7.3):
        self.__account = account
        self.__balance = balance
        self.__interestRate = interestRate

    def setAccount(self, account):
        self.__account = account

    def getAccount(self):
        return self.__account

    def getBalance(self):
        return self.__balance

    def calculateInterest(self):
        return self.__balance * self.__interestRate / 100

    def deposit(self, money):
        if money < 0:
            print("입금할 금액을 정확하게 입력해 주세요.")
        else:
            self.__balance += money

    def withdraw(self, money):
        if self.__balance < money:
            print("잔액이 인출할 금액보다 적습니다.")
        else:
            self.__balance -= money

userA = Account()
#print(f"계좌정보: {userA.getAccount()} 현재잔액: {userA.getBalance()}")
#userA.deposit(20000)
#print(f"계좌정보: {userA.getAccount()} 현재잔액: {userA.getBalance()}")
#print(f"이자: {userA.calculateInterest()}")

selectNum = 0

while(selectNum != 4):
    try:
        selectNum = int(input("원하는 행동을 선택해 주세요 1=계좌 정보 확인, 2=입금, 3=출금, 4=종료 : "))
    except ValueError:
        print("숫자를 입력해 주세요")

    if selectNum == 1:
        print(f"계좌정보: {userA.getAccount()} 현재잔액: {userA.getBalance()}")
    if selectNum == 2:
        while True:
            try:
                money = int(input("입금하실 금액을 입력해 주세요:"))
            except ValueError:
                print("정확한 숫자를 입력해 주세요")
            userA.deposit(money)
            print(f"계좌정보: {userA.getAccount()} 현재잔액: {userA.getBalance()}")
            break
    if selectNum == 3:
        while True:
            try:
                money = int(input("출금하실 금액을 입력해 주세요:"))
            except ValueError:
                print("정확한 숫자를 입력해 주세요")
            userA.withdraw(money)
            print(f"계좌정보: {userA.getAccount()} 현재잔액: {userA.getBalance()}")
            break
    else:
        print("1에서 4사이의 숫자를 입력해 주세요.")
