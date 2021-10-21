num = int(input("100 이하의 양의 정수를 입력해 주세요 : "))
i = num
total = 0

if num <= 0 or num > 100:
    print("error!")
else:
    while i <= 100:
        total += i
        i += 1
    print(total)