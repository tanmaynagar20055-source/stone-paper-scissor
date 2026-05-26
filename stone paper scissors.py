import random
class StonePaperScissors:


    def __init__(self):
        self.choices = ["stone", "paper", "scissors"]

    def play_game(self):

        while True:

            print("===== STONE PAPER SCISSORS =====")

            user = input("Enter stone/paper/scissors: ").lower()

            if user not in self.choices:
                print("Invalid Choice!")
                continue

            computer = random.choice(self.choices)

            print("Computer Choice:", computer)

            if user == computer:
                print("Match Draw!")

            elif (
                (user == "stone" and computer == "scissors") or
                (user == "paper" and computer == "stone") or
                (user == "scissors" and computer == "paper")
            ):
                print("You Win!")

            else:
                print("Computer Wins!")

            again = input("Play Again? (yes/no): ").lower()

            if again != "yes":
                print("Thanks for Playing!")
                break


game = StonePaperScissors()

game.play_game()