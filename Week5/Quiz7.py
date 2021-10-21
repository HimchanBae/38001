num = int(input("자연수를 입력해 주세요 : "))

for row in range (num) :
    for col in range (num - row - 1) :
        print(' ', end=' ')
    for col in range (row+1) :
        print(col+1, end=' ')
    print('')
