menu = int(input("Question number?\n"))
while menu != 0:
    if menu == 1:
        for i in range(100, 500):
            j = i
            s = 0
            while j > 0:
                s += (j % 10) ** 3
                j //= 10
            if s == i:
                print(i)
    elif menu == 2:
        pass
    else:
        menu = int(input("Error. Try again:\n(0 to quit)\n"))
    menu = int(input("Question number?\n"))
