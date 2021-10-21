num = int(input("1부터 100까지의 정수 중 한 개를 입력해 주세요 : "))
i = 1
#중첩 반복문으로 어떻게??
if num < 1 or num > 100 :
    print("error!")
else :
    while True :
        if ( num * i ) >= 100 :
            print("\n100보다 작은 배수 중 10의 배수가 없습니다.")
            break
        print(num * i, end=' ')
        i += 1
        if ( num * i ) % 10 == 0 :
            print(num * i)
            break
