heightM = int(input("민수는 키를 입력하거라 : "))
weightM = int(input("민수는 몸무게를 입력하거라 : "))

heightG = int(input("기영이는 키를 입력하거라 : "))
weightG = int(input("민수는 몸무게를 입력하거라 : "))

bool = ( heightM > heightG ) and ( weightM > weightG )

print(bool)
