def quiz_game():
    while True:
        score = 0
        print("\n WELCOME TO THE QUIZ CHALLENGE ")
        print("Let's test your knowledge! ")
        print("----------------------------------")

        
        question = input("1. What is the capital of India? \n")
        if question== "delhi":
            print(" Correct! ")
            score += 1
            print(f"your score is {score}")
        else:
            print(" Wrong! The correct answer is Delhi.\n")


        question = input("2.  What is the largest planet in our Solar System? \n")
        if question== "jupiter":
            print(" Correct!")
            score += 1
            print(f"your score is {score}")

        else:
            print(" Wrong! The correct answer is Jupiter.\n")

        question = input("3  Which programming language is used for AI? \n")
        if question == "python":
            print(" Correct!")
            score += 1
            print(f"your score is {score}")

        else:
            print(" Wrong! The correct answer is Python.\n")

        
        question = input("4 How many days are there in a leap year? \n: ")
        if question == "366":
            print(" Correct! Leap year has one extra day.")
            score += 1
            print(f"your score is {score}")

        else:
            print("Wrong! The correct answer is 366.\n")

        question = input("5.  Who is known as the father of computer? \n ")
        if question == "charles babbage":
            print(" Correct!.")
            score += 1
            print(f"your score is {score}")

        else:
            print(" Wrong! The correct answer is Charles Babbage.\n")

        print("----------------------------------")
        print(f" Your Total Score: {score}")

        if score == 5:
            print(" Excellent!")
        elif score >= 3:
            print(" Good job! You know quite a lot.")
        else:
            print(" Keep learning, you’ll get better!")

        play_again = input(" Do you want to play again? (yes/no): ")
        if play_again != "yes":
            print(" Thanks for playing! See you next time. 👋")
            break

quiz_game()
