num = int(input("자연수를 입력해 주세요 : "))

for row in range (1, num+1):
    for col in range (0, row):
        print('*', end="")
    print(" ")