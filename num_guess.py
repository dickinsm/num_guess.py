# Author: Makaliah Dickinson
# Date: 7/5/2020
# Description: Write a program that prompts the user for an integer that the player (maybe the user, maybe someone else)
#              will try to guess. If the player's guess is higher than the target number, the program should display
#              "too high" If the user's guess is lower than the target number, the program should display "too low"
#              The program should use a loop that repeats until the user correctly guesses the number. Then the program
#              should print how many guesses it took.
print("Enter the number for the player to guess.")
n = int(input())
guess = int(input("Enter your guess.\n"))
count = 0
while guess != n:
    if guess > n:
        print("Too high - try again:")
    else:
        print("Too low - try again:")
    count += 1
    guess = int(input())
print("You guessed it in", count, "tries.")
