# child care centre program

current_roll = []


def main(roll):
    action = int(input("Please enter the number corresponding to the action you want to do:\n"
                       "1; drop off a child\n"
                       "2; pick up a child\n"
                       "3; calculate the charge for looking after the children currently in the roll\n"
                       "4; print the roll\n"
                       "5; exit program\n"
                       "Enter number here: "))

    if action in (1, 2, 3, 4, 5):
        if action == 1:
            drop_off()
        elif action == 2:
            pickup()
        elif action == 3:
            calc_cost()
        elif action == 4:
            print_roll()
        else:
            exit()
    else:
        print("Invalid input, please enter a number from 1 to 5.")
        main(roll)


def drop_off():
    child_name = str(input("What is the name of the child you are dropping off?: "))
    current_roll.append(child_name)
    print(f"{child_name} has been dropped off.")


def pickup():
    child_name = str(input("What is the name of the child you are picking up?: "))
    current_roll.remove(child_name)
    print(f"{child_name} Has been picked up")


def calc_cost():
    cost = len(current_roll) * 12
    print("The cost for looking after the children currently in the roll is $" + str(cost) + ".")


def print_roll():
    print("The current roll is:")
    for child in current_roll:
        print(child)


main(current_roll)
