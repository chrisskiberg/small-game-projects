import random
import math

def generateWhiteNoise(width,height):
    random.seed()
    noise = [[r for r in range(width)] for i in range(height)]

    for i in range(height):
        for j in range(width):
            noise[i][j] = random.randint(0,1)

    return noise

def printNoise(noise):
    for i in noise:
        print()
        for o in i:
            if(o == 0):
                print('-',end='')
            else:
                print('#',end='')

    print("")