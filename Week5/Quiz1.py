num = int(input("자연수를 입력해 주세요 : "))
i = 1
sum = 0
cnt = 0

if num <= 0:
    print("error!")
else:
    while True:
        sum += i
        i += 2
        cnt += 1
        if sum >= num:
            print(cnt, sum)
            break