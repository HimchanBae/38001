num1 = int(input("행을 입력해 주세요 : "))
num2 = int(input("열을 입력해 주세요 : "))

for row in range (1, num1+1):
    for col in range (0, num2):
        print(row + col * row, end=" ")
    print("")