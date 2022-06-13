import random
import  functions as func



basicValues = ["paper", "scissor", "rock"]
stopGame = True
while stopGame:
    computerValue = random.choice(basicValues)
    userValue = input("Select value: ")
    if userValue in basicValues:
        print("Computer value: ",computerValue)
        if func.deadHeat(userValue, computerValue): 
            print("remis")
        elif func.paperWonWithRock(userValue, computerValue): 
            print("Paper won the game!")
            stopGame = False
        elif func.rockWonWithScissor(userValue, computerValue): 
            print("Rock won the game!")
            stopGame = False
        elif func.scissorWonWIthPaper(userValue, computerValue): 
            print("Scissor won the game!")
            stopGame = False
    else:
        print("User Value doesn't exists")
