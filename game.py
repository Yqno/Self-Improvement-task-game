import random

def self_improvement_task_game():
    print("Welcome to the self improvement task game!")
    print("The goal of this game is to work on personal growth and self-improvement.")
    print("Each round, you will be given a prompt to work on. Good luck!")

    rounds = [
        "Write down three things you are grateful for.",
        "Spend 10 minutes meditating.",
        "Write down your goals for the next week.",
        "Do something kind for someone else.",
        "Write down three things you accomplished today.",
        "Spend 10 minutes exercising.",
        "Write down three things you want to learn this week.",
        "Write down three positive affirmations about yourself.",
        "Read 10 Pages on a Self help Book.",
        "Approach someone.",
        "give someone a Compliment",
        "learn 20 minutes about a new Topic."


    ]

    while True:
        print("\n")
        print("It's time for a new round!")
        task = random.choice(rounds)
        print(f"Your task for this round is: {task}")

        answer = input("Did you complete the task? (yes/no) ")
        if answer.lower() == "yes":
            print("Great job! Keep up the good work.")
        elif answer.lower() == "no":
            print("Don't worry, there's always next round to work on personal growth.")
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    self_improvement_task_game()
