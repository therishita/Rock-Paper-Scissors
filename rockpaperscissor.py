import random

print("=" * 30)
print("      ROCK PAPER SCISSORS")
print("=" * 30)

while True:
    user_score = 0
    computer_score = 0

    while True:
        try:
            rounds = int(input("\nEnter the number of rounds you want to play: "))
            if rounds > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    choices = ["Rock", "Paper", "Scissors"]

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num} of {rounds}")

        print("\nChoose your move:")
        print("1: Rock")
        print("2: Paper")
        print("3: Scissors")

        while True:
            choice = input("\nEnter your choice (1-3): ")

            if choice in ["1", "2", "3"]:
                break

            print("Invalid choice! Please enter 1, 2, or 3.")

        user_choice = choices[int(choice) - 1]
        computer_choice = random.choice(choices)

        print("\n" + "-" * 30)
        print(f"You chose      : {user_choice}")
        print(f"Computer chose : {computer_choice}")
        print("-" * 30)

        # Game logic
        if user_choice == computer_choice:
            print("It's a Tie!")

        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            print("You Win!")
            user_score += 1

        else:
            print("Computer Wins!")
            computer_score += 1

    print("\n" + "=" * 30)
    print("         FINAL SCORE")
    print("=" * 30)
    print(f"You      : {user_score}")
    print(f"Computer : {computer_score}")

    if user_score > computer_score:
        print("\nCongratulations! You won the game!")
    elif computer_score > user_score:
        print("\nBetter luck next time!")
    else:
        print("\nThe game ended in a tie!")

    while True:
        play_again = input("\nDo you want to play again? (y/n): ").upper()

        if play_again in ["Y", "N"]:
            break

        print("Please enter y or n.")

    if play_again == "N":
        print("\nThank you for playing!")
        break
#RISHITA SARKAR 

