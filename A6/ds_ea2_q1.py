import random

def montyHall(number):

    winCountStaying = 0
    winCountChanging = 0

    if(number is None or not isinstance(number, int) or number < 0):
        raise ValueError("Number of Experiments is invalid")
    
    for i in range(number):
        # random position of the car price behind one of the 3 doors
        positionOfCar = random.randint(0,2)
        # random guess where the car price could be behind one of the 3 doors
        choiceOfDoor = random.randint(0,2)

        

        # if first guess correct -> increase win count for staying, no win count increase for changing doors
        if(positionOfCar == choiceOfDoor):
            winCountStaying += 1
        # if first guess incorrect -> increase win count for changing, no win count increase for staying with first guess
        else:
            winCountChanging += 1

    return winCountStaying, winCountChanging
            



##### MAIN #####

n = 100
N = 10000
totalWinsWithChangingOpinion = 0

for i in range(N):
    count1, count2 = montyHall(n)
    totalWinsWithChangingOpinion  += count2

# average number of wins in N iterations a 100 trys per iteration
totalWinsWithChangingOpinion = totalWinsWithChangingOpinion/N

print("Monty Hall Problem with n = " + str(n) + " iterations, delivered following results: Wins with keeping the first guess = " + str(count1) + ", Wins with changing opinion = " + str(count2) + ".")

print("Average wins with changing opinion per " + str(N) + " iterations of experiments with " + str(n) + " trys per iteration --> " + str(totalWinsWithChangingOpinion) + ".")

print("Changing your opinion is always the better choice than staying with your first guess. After very many iterations you can see that the probability of success converges against" +
      " 2/3 (66.67%), doubling your win rate. The probability of a win while keeping the first guess converges against 1/3 (33.33%).")