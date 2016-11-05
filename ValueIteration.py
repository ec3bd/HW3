import sys
import numpy

def main():
    MAX_ITERS = 10
    Uprime = [[0 for x in range(7)] for y in range(7)]
    discount = 1
    iter = 0;
    endCondition = False
    while(not endCondition):
        iter+=1
        U = Uprime
        delta = 0
        for i in range(0,7):
            for j in range(0,7):
                bestValue = -sys.maxsize
                bestMove = 0
                for l in range(-1,2):
                    for k in range(-1,2):
                        if i+l < 7 and i+l >=0 and j+k < 7 and j+k >=0:
                            if U[i+l][j+k] > bestValue:
                                bestMove = (l,k)
                                bestValue = U[i+l][j+k]
                Uprime[i][j] = reward((i,j)) + discount*bestValue
                if abs(Uprime[i][j] - U[i][j]) > delta:
                    delta = abs(Uprime[i][j] - U[i][j])
        endCondition = delta < .009 or iter == MAX_ITERS
    print(numpy.asarray(Uprime))
    print(iter)

def optimalPolicy(startpoint, U):
    i = startpoint[0]
    j = startpoint[1]
    while(True):
        bestMove = (0,0)
        bestValue = U[i][j]
        for l in range(-1,2):
            for k in range(-1,2):
                if i+l < 7 and i+l >=0 and j+k < 7 and j+k >=0:
                    if U[i+l][j+k] > bestValue:
                        bestValue = U[i+1][j+k]
                        bestMove = (l,k)
        #delta =
def reward(state):
    if state[0] is 3 and state[1] is 6:
        return 0
    else:
        return -1

if __name__ == "__main__":
    main()