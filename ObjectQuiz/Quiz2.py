class Book:
    def __init__(self, bookName=None, bookPrice=0, bookDiscountRate=0):
        self.__bookName = bookName
        self.__bookPrice = bookPrice
        self.__bookDiscountRate = bookDiscountRate

    def setBookName(self, bookName):
        self.__bookName = bookName

    def getBookName(self):
        return self.__bookName

    def setBookDiscountRate(self, bookDiscountRate):
        self.__bookDiscountRate = bookDiscountRate

    def getBookDiscountRate(self):
        return self.__bookDiscountRate

    def setBookPrice(self, bookPrice):
        self.__bookPrice = bookPrice

    def getBookPrice(self):
        return self.__bookPrice

    def getDiscountBookPrice(self):
        return self.__bookPrice * ((100 - self.__bookDiscountRate) / 100)


bookA = Book()
bookB = Book()
bookC = Book()

bookA.setBookName("SQL Plus")
bookA.setBookPrice(50000)
bookA.setBookDiscountRate(5)

bookB.setBookName("Java 2.0")
bookB.setBookPrice(40000)
bookB.setBookDiscountRate(3)

bookC.setBookName("JSP Servlet")
bookC.setBookPrice(60000)
bookC.setBookDiscountRate(6)

for i in range(3):
    if i == 0:
        print(f"{bookA.getBookName()} {bookA.getBookPrice()}원 {bookA.getBookDiscountRate()}%")
    elif i == 1:
        print(f"{bookB.getBookName()} {bookB.getBookPrice()}원 {bookB.getBookDiscountRate()}%")
    else:
        print(f"{bookC.getBookName()} {bookC.getBookPrice()}원 {bookC.getBookDiscountRate()}%")
        print()

sumOfBookPrice = bookA.getBookPrice() + bookB.getBookPrice() + bookC.getBookPrice()
sumOfDiscBookPrice = bookA.getDiscountBookPrice() + bookB.getDiscountBookPrice() + bookC.getDiscountBookPrice()

print(f"책 가격의 합:{sumOfBookPrice}원")
print(f"할인 된 책 가격의 합:{sumOfDiscBookPrice}원")
