import random

def dice_roller():
    while True:
        num_dice = int(input("Enter the number of dice: "))
        num_sides = int(input("Enter the number of sides on each die: "))

        print("\nRolling the dice...\n")
        for _ in range(num_dice):
            roll = random.randint(1, num_sides)
            print(f"You rolled: {roll}")

        print()
        play_again = input("Do you want to roll the dice again? (yes/no): ")
        if play_again.lower() != "yes":
            break
        print()

dice_roller()
