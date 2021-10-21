num = int(input("자연수를 입력해 주세요 : "))

if num <= 0 :
    print("error!")
else :
    #중첩으로 안 할 때
    for row in range (num) :
        print(' ' * row, '*' * ((2 * (num - row)) - 1), sep='')

    #중첩으로 할 때
    for row in range (num) :
        for col in range (row) :
            print(" ", end='')
        for col in range ((num-row)*2-1) :
            print("*", end='')
        print('')