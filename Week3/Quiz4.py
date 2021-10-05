month = int(input("1~12월 중 하나를 정수로 입력해주세요 : "))

if ( month < 1 ) or ( month > 12 ) :
    print("error!")
elif month == ( 1 or 3 or 5 or 7 or 8 or 10 or 12 ) :
    print(31)
elif month == 2 :
    print(28)
else :
    print(30)