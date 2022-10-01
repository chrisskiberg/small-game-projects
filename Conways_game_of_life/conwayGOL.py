import random
import math
import classes 
import noise_fun as fun

# random.seed()

# def generateWhiteNoise(width,height):
#     noise = [[r for r in range(width)] for i in range(height)]

#     for i in range(0,height):
#         for j in range(0,width):
#             noise[i][j] = random.randint(0,1)

#     return noise

# noise = generateWhiteNoise(10,10)

# for i in noise:
#     print()
#     for o in i:
#         if(o == 0):
#             print('-',end='')
#         else:
#             print('#',end='')

def seperatePrints():
    for i in range(200):
        print("-", end="")

grid=classes.Grid(110, 30)
# print("length:", grid.length)
# print("width:", grid.width)
# print(grid.grid)
# grid.print()


noise = fun.generateWhiteNoise(110,30)
# fun.printNoise(noise)

grid.grid_setter_grid(noise)
grid.print()
for i in range(50):
    # seperatePrints()
    grid.update()
    grid.print()






# for y in range(1,MAX_LENGTH):
#     # Kan bruke en tellefunksjon for å optimalisere, teller antallet mellom dem som skal være spaces, bruke en for lokke
#     # if cell here, print black square
#     # else, print a space
#     for x in range(1, MAX_WIDTH):
#         print(chr(9608), end='')
#     print("")
# print("")
# print("")
# for i in range(1,MAX_LENGTH):
#     # if cell here, print black square
#     # else, print a space
#     print(chr(9608), end=' ')



# print(chr(9608)+chr(9608)+chr(9608))

# # Object cell
#     # position
#     # dead or alive

# # Object grid
#     # param length and width
#     # positions taken

# def create_newcell(pos):

# def commit_alive():
#     # check around all the cells position and see if there are 3 neighbors
#     if (more than 3 cells nearby)

# def update_print():
#     return -1

# def create_seed(): # specifies the starting position of the cells
#     return -1

# def create_grid(): # Function to create grid, under, initialize
#    return -1 


# def check_neighbors(): # Checks the amount of nearby neighbors

#     if alive
#     if (less than 2 neighbors):
#         cell.set_death()
#     elif (more than 3 neighbors):

#         if (dead):
#             cell.set_alive()
#         else:
#             cell.set_death()

#     else ():
#         # keep alive
#         print("hei")

# def death(): # From if fewer than 2 cells nearby
#    return -1 

