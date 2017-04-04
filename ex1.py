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
        def find(tickets, budget):
            for x in range(tickets):
                for y in range(tickets):
                    for z in range(tickets):
                        if ((3*x) + (10*y) + (15*z) == budget) & ((x + y + z) == tickets):
                            return[str(x) + " tickets for 3$", str(y) + " tickets for 10$", str(z) + " tickets for 15$"]
        print("To purchase 100 tickets with 400$ you need:")
        for x in find(100, 400):
            print(x)
    elif menu == 3:
        from random import randint
        turn = randint(1, 2)
        def getint(x):
            try:
                return int(x)
            except ValueError:
                return False
        print("7 Boom!")
        if turn == 1:
            print("you start:")
        else:
            print("I start:")
        for x in range(1, 31):
            if turn == 2:
                if ((x % 7) == 0) | ((x % 10) == 7):
                    print("Computer: Boom!")
                else:
                    print("Computer: " + str(x))
                turn -= 1
            elif turn == 1:
                user = input("You: ")
                if ((x % 7) == 0) | ((x % 10) == 7):
                    if (user != "Boom") & (user != "boom") & (user != "Boom!") & (user != "boom!"):
                        print("You loose!")
                        break
                else:
                    usr_int = getint(user)
                    if not usr_int:
                        print("You loose!")
                        break
                    elif usr_int != x:
                        print("You loose!")
                        break
                turn += 1
            if x == 30:
                print("You Win!")
    else:
        menu = int(input("Error. Try again:\n(0 to quit)\n"))
    menu = int(input("Question number?\n"))
