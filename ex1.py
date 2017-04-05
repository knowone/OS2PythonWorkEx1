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

        def getint(z):
            try:
                return int(z)
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
    elif menu == 4:

        def insert(obj, stack: list):
            stack.append(obj)

        def eject(stack: list):
            if not stack:
                return "Empty"
            else:
                obj = stack.pop()
                return obj

        def prt_stack(stack: list):
            if not stack:
                print("Empty")
            else:
                for index, obj in enumerate(stack[::-1]):
                    print(index, obj)

        my_stack = []
        status = ""
        user_choice = input("Enter a command (i, e, p):\n")
        while 1:
            if user_choice == 'i':
                obj_str = input("Enter string to insert to stack:\n")
                insert(obj_str, my_stack)
            elif user_choice == 'e':
                status = eject(my_stack)
                if status == "Empty":
                    break
            elif user_choice == 'p':
                prt_stack(my_stack)
            else:
                print("Invalid choice. Try again..")
            user_choice = input("Enter a command (i, e, p):\n")
    else:
        menu = int(input("Error. Try again:\n(0 to quit)\n"))
    menu = int(input("Question number?\n"))
