import random

number = random.randint(0,3)

words = ["meg","peter","lois","stewie"]
hint1 = ["no family","fat","ginger","evil"]
hint2 = ["abombination","the clam","bad food","time machine"]

secretword = words[number]
guess = ""
counter =  1


while True:
    print("Guess my secret word!")
    print("Type 'hint1', 'hint2', 'first letter', or 'give up', for answer.")
    guess = input()

    if guess == secretword:
        print("Finally")
        print("It took you " + str(counter) + " guesses.")
        break

    elif guess == "hint1":
        print(hint1[number])
        print (hint2[number])

    elif guess == "hint2":
        print(hint2[number])

    elif guess == "first letter":
        print(secretword[0])

    elif guess == "give up":
        print("Wow. You are a disgrace.")
        print("You failed " + str(counter) + " times.")
        break

    else:
        print("Try again.")
        counter += 1
        
         
