num1 = int(input("2부터 9까지의 수 중 한 개를 입력해 주세요 : "))
num2 = int(input("2부터 9까지의 수 중 다른 한 개를 입력해 주세요 : "))

if num1 < 2 or num2 < 2 or num1 > 9 or num2 > 9 or num1 == num2:
    print("error!")
elif num1 > num2:
    for row in range(1, 10):
        for col in range(0, num1 - num2 + 1):
            print(num1 - col, "*", row, "=", (num1 - col) * row, end="  ")
        print("")
else:
    for row in range(1, 10):
        for col in range(0, num2 - num1 + 1):
            print(num1 + col, "*", row, "=", (num1 + col) * row, end="  ")
        print("")
