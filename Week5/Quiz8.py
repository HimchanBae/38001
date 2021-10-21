num = int(input("자연수를 입력해 주세요 : "))
a = 1

for row in range (num) :
    for col in range (row) :
        print(' ', end=' ')
    for col in range (num-row) :
        print(a, end=' ')
        a += 1
    print('')