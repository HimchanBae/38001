num = int(input("자연수를 입력해 주세요 : "))
a = 1

for row in range (num) :
    for col in range (num) :
        print(a, end=' ')
        a = (a + 2) % 10
    print('')