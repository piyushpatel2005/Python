from dice import Dice, Die

def main():
    print("The Dice Roller")
    print()

    count = int(input("Enter the number of dice to roll: "))

    dice = Dice()
    for i in range(count):
        die = Die()
        dice.addDie(die)

    while True:
        dice.rollAll()
        print("YOUR ROLL: ", end="")
        for die in dice.list:
            print(die.value, end= " ")
        print("\n")

        choice = input("Roll again? (y/n): ")
        if choice != 'y':
            print("Bye!")
            break

if __name__ == "__main__":
    main()
