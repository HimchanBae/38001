sex = input("남자는 'M' 여자는 'F'를 입력해 주세요 : ")
age = int(input('나이를 입력해 주세요 : '))

if ( sex == 'M' ) and ( age >= 18 ) :
    print("MAN")
elif ( sex == 'M' ) and ( age < 18 ) :
    print("BOY")
elif ( sex == 'F' ) and ( age >= 18 ) :
    print("WOMAN")
elif ( sex == 'F' ) and ( age < 18 ) :
    print("GIRL")
else :
    print("error")