import random
lst=['st','p','sc']
chance=3
no_of_chance=0
computer_score=0
your_score=0
print("\t\t\t\t STONE, PAPER AND SCISSOR\t\t\t\t\n")
print("type st for stone\n p for paper\n sc for scissor\n")

while no_of_chance < chance:
    _input=input("stone, paper or scissor:")
    _random=random.choice(lst)
    if _input==_random:
        print("Its a tie")
    elif _input=="st" and _random=="p":
        computer_score=computer_score+1
        print(f"you guessed {_input} and computer_guessed {_random}\n")
        print("computer wins 1 point\n")
        print(f"your score is {your_score} and computer's score is {computer_score}\n")
    elif _input=="st" and _random=="sc":
        your_score=your_score+1
        print(f"you guessed {_input} and computer_guessed {_random}\n")
        print("you win 1 point\n")
        print(f"your score is {your_score} and computer's score is {computer_score}\n")
    elif _input=="p" and _random=="st":
        your_score=your_score+1
        print(f"you guessed {_input} and computer_guessed {_random}\n")
        print("you win 1 point\n")
        print(f"your score is {your_score} and computer's score is {computer_score}\n")
    elif _input=="p" and _random=="sc":
        computer_score=computer_score+1
        print(f"you guessed {_input} and computer_guessed {_random}\n")
        print("computer wins 1 point\n")
        print(f"your score is {your_score} and computer's score is {computer_score}\n")
    elif _input=="sc" and _random=="p":
        your_score=your_score+1
        print(f"you guessed {_input} and computer_guessed {_random}\n")
        print("you win 1 point\n")
        print(f"your score is {your_score} and computer's score is {computer_score}\n")
    elif _input=="sc" and _random=="st":
        computer_score=computer_score+1
        print(f"you guessed {_input} and computer_guessed {_random}\n")
        print("computer wins 1 point\n")
        print(f"your score is {your_score} and computer's score is {computer_score}\n")
    else:
        print("you entered wrong input")

    no_of_chance=no_of_chance+1
    print(f"{chance-no_of_chance} is left out of {chance}")
    print("game over\n")

    if computer_score==your_score:
        print("tie\n")
    elif computer_score > your_score:
        print("computer win you lose\n")
    else:
        print("you win computer looses\n")
    
    print(f"your score is {your_score} and computer score is {computer_score}\n")