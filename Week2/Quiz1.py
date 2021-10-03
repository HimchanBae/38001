num1 = int(input("첫 번째 정수를 입력해주세요: "))
num2 = int(input("두 번째 정수를 입력해주세요: "))

bool1 = num1 > num2
bool2 = num1 < num2
bool3 = num1 >= num2
bool4 = num1 <= num2

print("%d > %d ---" % (num1, num2), bool1)
print("%d < %d ---" % (num1, num2), bool2)
print("%d >= %d ---" % (num1, num2), bool3)
print("%d <= %d ---" % (num1, num2), bool4)
