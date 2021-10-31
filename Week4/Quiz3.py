num = int(input("한 개의 자연수를 입력해 주세요 : "))

if num <= 0:
    print("error!")
else:
    for i in range(1, 11):
        print(num * i, end=" ")
