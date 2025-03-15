import random

def guess_game():
    print("Guess Number Game")
    number_to_guess = random.randint(1, 10)  
    attempts = 0

    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        attempts += 1
        
        if user_guess < number_to_guess:
            print("Too low! have another go.")
        elif user_guess > number_to_guess:
            print("Too high! have another go.")
        else:
            print(f"Congratulations! You guessed the number correctly {number_to_guess} in {attempts} attempts.")
            break

def rock_paper_scissors_game():
    print("Welcome to the Rock Paper Scissors Game! try your luck here")
    choices = ['rock', 'paper', 'scissors']

    while True:
        user_choice = input("Enter 'rock', 'paper', or 'scissors' (or 'exit' to quit): ").lower()
        
        if user_choice == 'exit':
            print("i am Exiting the game.")
            break
        elif user_choice not in choices:
            print("Invalid choice! Please choose ( rock, paper, or scissors ) .")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chooses {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win ")
        else:
            print("Sorry , you lost")

def main():
    while True:
        print("\nSelect a function (1-3):")
        print("1. Guess Number game")
        print("2. Rock Paper Scissors game")
        print("3. Exit program")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number (1-3).")
            continue
        
        if choice == 1:
            guess_game()
        elif choice == 2:
            rock_paper_scissors_game()
        elif choice == 3:
            print("Exiting the program. Goodbye! you are too good at this")
            break
        else:
            print("Invalid choice! Please enter (1-3).")

if __name__ == "__main__":
    main()