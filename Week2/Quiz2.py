num1 = int(input("첫 번째 정수를 입력해주세요: "))
num2 = int(input("두 번째 정수를 입력해주세요: "))
num3 = int(input("세 번째 정수를 입력해주세요: "))

boolean1 = ( num1 > num2 ) and ( num1 > num3 )
boolean2 = ( num1 == num2 ) and ( num2 == num3 )

print(boolean1, boolean2)
