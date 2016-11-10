import sys
import numpy
from copy import deepcopy


MAX_ITERS = 50
lightWind = False
strongWind = True


def main():
    Uprime = [[0 for x in range(7)] for y in range(7)]
    discount = 1
    iter = 0;
    endCondition = False
    while(not endCondition):
        iter+=1
        U = deepcopy(Uprime)
        delta = 0
        for i in range(0,7):
            for j in range(0,7):
                bestValue = -sys.maxsize
                bestMove = (0,0)
                wind = 0
                if(j >= 3 and j <= 5):
                    if lightWind:
                        wind = -1
                    elif strongWind:
                        wind = -2
                for l in range(-1+wind,2+wind):
                    for k in range(-1,2):
                        if i+l < 7 and i+l >=0 and j+k < 7 and j+k >=0:
                            if U[i+l][j+k] > bestValue:
                                bestMove = (l,k)
                                bestValue = U[i+l][j+k]
                        else:
                            ind1 = i+l
                            ind2 = j+k
                            if i+l >= 7:
                                ind1 = 6
                            if i+l < 0:
                                ind1 = 0
                            if j+k >= 7:
                                ind2 = 6
                            if j+k < 0:
                                ind2 = 0
                            if U[ind1][ind2] > bestValue:
                                bestMove = (l,k)
                                bestValue = U[ind1][ind2]
                Uprime[i][j] = reward((i,j)) + discount*bestValue
                if abs(Uprime[i][j] - U[i][j]) > delta:
                    delta = abs(Uprime[i][j] - U[i][j])
        endCondition = delta == 0 or iter == MAX_ITERS

    numpy.set_printoptions(linewidth=85)
    print(numpy.asarray(Uprime))
    policy1 = optimalPolicy((3,0), U)
    policy2 = optimalPolicy((3,0), U, True)
    print(policy1)
    if len(policy1) == len(policy2):
        nonequal = False
        for i in range(0,len(policy1)):
            if policy1[i] != policy2[i]:
                nonequal = True
        if nonequal:
            print(policy2)

def optimalPolicy(startpoint, U, alternatePath=False):
    i = startpoint[0]
    j = startpoint[1]
    path = []
    iter = 0
    while(True):
        iter+=1
        lastState = (i,j)
        if iter == MAX_ITERS:
            break
        bestMove = (0,0)
        bestValue = U[i][j]
        outofbound = False
        wind = 0
        if(j >= 3 and j<=5):
            if lightWind:
                wind = -1
            elif strongWind:
                wind = -2
        for l in range(-1+wind,2+wind):
            for k in range(-1,2):
                if i+l < 7 and i+l >=0 and j+k < 7 and j+k >=0:
                    if not alternatePath:
                        if U[i+l][j+k] > bestValue:
                            bestValue = U[i+l][j+k]
                            bestMove = (l,k)
                    else:
                        if U[i+l][j+k] >= bestValue:
                            bestValue = U[i+l][j+k]
                            bestMove = (l,k)
        i = i + bestMove[0]
        j = j + bestMove[1]
        if outofbound:
            i = ind1
            j = ind2
        if bestMove == (0,0):
            break
        stringMove = ""
        printMove = (bestMove[0]-wind, bestMove[1])

        if printMove[0] == -1:
            stringMove = "N"
        elif printMove[0] == 0:
            stringMove = ""
        elif printMove[0] == 1:
            stringMove = "S"
        if printMove[1] == -1:
            stringMove += "W"
        elif printMove[1] == 0:
            stringMove += ""
        elif printMove[1] == 1:
            stringMove += "E"
        path.append(repr(lastState)+ " : "+repr(stringMove) + " -> ("+repr(i)+","+repr(j)+")")

    return path

def reward(state):
    if state[0] is 3 and state[1] is 6:
        return 0
    else:
        return -1

if __name__ == "__main__":
    main()