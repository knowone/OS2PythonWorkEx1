# --------------------------------------------------------------------------------------------------------------------
def quest1():
    """
    Question 1: prints all numbers that their sum of digits cubed are equal to themselves.
    """
    for i in range(100, 500):
        j = i
        s = 0
        while j > 0:
            s += (j % 10) ** 3
            j //= 10
        if s == i:
            print(i)


# --------------------------------------------------------------------------------------------------------------------
def quest2():
    """
    Question 2: Solves the question - if you buy 100 tickets for 400$, when each ticket costs either 3$,10$ or 15$
        How many tickets of each type did you buy?
    """

    def find(tickets, budget):
        """Finds, for a given tickets amount and budget how many tickets of each type you bought"""

        for x in range(tickets):
            for y in range(tickets):
                for z in range(tickets):
                    if ((3*x) + (10*y) + (15*z) == budget) & ((x + y + z) == tickets):
                        return[str(x) + " tickets for 3$", str(y) + " tickets for 10$", str(z) + " tickets for 15$"]

    print("To purchase 100 tickets with 400$ you need:")
    for found in find(100, 400):
        print(found)


# --------------------------------------------------------------------------------------------------------------------
def quest3():
    """
    Question 3: Plays with user 7 boom! where starting player is selected randomly for extra fun.
        Each player types the next number, but if the number is a multiple of 7 or has 7 in it then player must type
        "Boom" instead of the number. Also correct order of numbers must be kept. 
        Player is winner if was able to get to 30.
    """
    from random import randint
    turn = randint(1, 2)
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
                if usr_int == "invalid":
                    print("You loose!")
                    break
                elif usr_int != x:
                    print("You loose!")
                    break
            turn += 1
        if x == 30:
            print("You Win!")


# --------------------------------------------------------------------------------------------------------------------
def quest4():
    """
    Question 4: Implement a stack using list with operations:
        i - insert (push) to stack
        e - eject(pop) from stack
        p - print the stack
        
        When stack is empty, print will print "Empty"
        If stack is empty and e (pop) is called, the function will exit.
    """

    def insert(obj, stack: list):
        """Using list, appends to the end of the list.
        obj can be anything. Must be a printable object"""

        stack.append(obj)

    def eject(stack: list):
        """using list, pop the end of the list from the list.
        returns the ejected object"""

        if not stack:   # not stack will return true if list is [] (empty)
            return "Empty"
        else:
            obj = stack.pop()
            return obj

    def prt_stack(stack: list):
        """Print the list in 2 columns starting from 0 index.
        Prints the list backwards to simulate stack order (FIFO)
        Prints "Empty" if list is empty"""

        if not stack:
            print("Empty")
        else:
            for index, obj in enumerate(stack[::-1]):
                print(index, obj)

    my_stack = []
    user_choice = input("Enter a command (i, e, p):\n")
    while 1:
        if user_choice == 'i':
            obj_str = input("Enter string to insert to stack:\n")
            insert(obj_str, my_stack)
        elif user_choice == 'e':
            status = eject(my_stack)
            if status == "Empty":
                break   # stop only if stack is already empty
        elif user_choice == 'p':
            prt_stack(my_stack)
        else:
            print("Invalid choice. Try again..")
        user_choice = input("Enter a command (i, e, p):\n")


# --------------------------------------------------------------------------------------------------------------------
def getint(z):
    """
    Error preventing convert-to-int function.
        Catches ValueError exceptions if int() is being called with a string type argument.
    """

    try:
        return int(z)
    except ValueError:
        return "invalid"


# --------------------------------------------------------------------------------------------------------------------
def main():
    """
    Prompts a selection for user to choose between the 4 assignments.
    1,2,3,4 corresponds to the question numbers.
    0 will exit the program.
    For all other inputs, the program will display a retry message. 
    """
    quest = [quest1, quest2, quest3, quest4]
    menu = getint(input("Question number? (0 to quit)\n"))
    while menu != 0:
        if 0 < menu <= 4:
            quest[menu-1]()
        else:
            print("Invalid choice. Try again..\n")
        menu = getint(input("Question number? (0 to quit)\n"))

main()
