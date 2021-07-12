import random
print("hi")
def randomNumGen() :
    RandomNum = random.randint(1,10)
    return RandomNum

def UserGuess(result = "Hi, I am thinking of a number between 1 and 10. Make a Guess: "):
    UserAnswer = int(input(result))
    return UserAnswer

def CheckUserGuess(UserAnswer,RandomNum):
    if UserAnswer > RandomNum:
        return "Too High!"
    elif UserAnswer < RandomNum:
        return "Too Low!"
    else:
        return "Congrats Buddy!"

def mainFunction():

    playagain = "Yes"
    while playagain == "Yes":

        Numofguesses = 0
        RandomNumber = randomNumGen()
        # print("For testing purposes",RandomNumber)
        UsersAnswer = UserGuess()
        Numofguesses = Numofguesses + 1
        result = CheckUserGuess(UsersAnswer,RandomNumber)

        while result != "Congrats Buddy!":
            print(result)
            UsersAnswer = UserGuess("Try again: ")
            Numofguesses = Numofguesses + 1
            result = CheckUserGuess(UsersAnswer,RandomNumber)



        if Numofguesses == 1 :
            print(result)
            print("You took only " + str(Numofguesses) + " try to get the answer! I am proud of you :)")

        else:
            print(result)
            print("You took " + str(Numofguesses) + " tries to get the answer! It could've been better :(")
        playagain = input("So do you want to play again?(type Yes)")


mainFunction()




