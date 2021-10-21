while True:
    base = float(input("Base = "))
    height = float(input("Height = "))
    width = base * height / 2.0
    print("Triangle width =", round(width, 1))
    answer = input("Continue? ")
    if answer not in ('y' or 'Y'):
        break
