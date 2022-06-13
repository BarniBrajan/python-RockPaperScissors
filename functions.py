def deadHeat(userValue, computerValue):
    if (userValue == "paper" and computerValue == "paper") or (userValue == "rock" and computerValue == "rock") or (userValue == "scissor" and computerValue == "scissor"):
        return True

def paperWonWithRock(userValue, computerValue):
        if (userValue == "paper" and computerValue == "rock") or (userValue == "rock" and computerValue == "paper"):
            return True

def rockWonWithScissor(userValue, computerValue):
        if (userValue == "scissor" and computerValue == "rock") or (userValue == "rock" and computerValue == "scissor"):
            return True

def scissorWonWIthPaper(userValue, computerValue):
        if (userValue == "scissor" and computerValue == "paper") or (userValue == "paper" and computerValue == "scissor"):
            return True