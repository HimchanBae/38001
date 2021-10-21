cnt = 0

while True:
    num = int(input("정수를 입력해 주세요(out=0) : "))
    if num%3 != 0 and num%5 != 0:
        cnt += 1
    elif num == 0:
        print(cnt)
        break