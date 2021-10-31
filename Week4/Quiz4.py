#1번이랑 중복 문제라서 for로 맹글어봄

num = int(input("100 이하의 양의 정수를 입력해 주세요 : "))
total = 0

if num <= 0 or num > 100:
    print("error!")
else:
    for i in range (1, num+1):
        total += i
    print(total)
