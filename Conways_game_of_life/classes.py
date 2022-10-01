from copy import deepcopy
import os
import time


class Grid: 
    MAX_WIDTH=201
    MAX_LENGTH=54

    def __init__(self, width, length, grid=[]): 
        self.width=width
        self.length=length
        if (len(grid)==0):
            for i in range(length):
                grid.append([0 for i in range(width)])
        self.grid=grid


    def update(self): # klasse funksjon

        grid_new=deepcopy(self.grid)
        dead_cell_neighbors={}
        key_arr=[] # kan gjøres om til et set()
        
        # Finds location of cells
        cell_locs=[]
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if (self.grid[y][x]==1):
                    cell_locs.append([y,x])
        print("")
        # print(self.grid[1][1])


        for cell_loc in cell_locs: # check alive/death
            neighbors=0

            if (cell_loc[0]+1!=self.length):
                if (self.grid[cell_loc[0]+1][cell_loc[1]]==1):
                    neighbors+=1
                else:
                    key=str(cell_loc[0]+1)+str(cell_loc[1])
                    if (key in key_arr):
                        dead_cell_neighbors[key]+=1
                    else:
                        key_arr.append(key)
                        dead_cell_neighbors[key]=1


            if (cell_loc[1]+1!=self.width):
                if (self.grid[cell_loc[0]][cell_loc[1]+1]==1):
                    neighbors+=1
                else:
                    key=str(cell_loc[0])+str(cell_loc[1]+1)
                    if (key in key_arr):
                        dead_cell_neighbors[key]+=1
                    else:
                        key_arr.append(key)
                        dead_cell_neighbors[key]=1


            if (cell_loc[0]-1!=-1):                
                if (self.grid[cell_loc[0]-1][cell_loc[1]]==1):
                    neighbors+=1
                else:
                    key=str(cell_loc[0]-1)+str(cell_loc[1])
                    if (key in key_arr):
                        dead_cell_neighbors[key]+=1
                    else:
                        key_arr.append(key)
                        dead_cell_neighbors[key]=1

            
            if (cell_loc[1]-1!=-1):
                if (self.grid[cell_loc[0]][cell_loc[1]-1]==1):
                    neighbors+=1
                else:
                    key=str(cell_loc[0])+str(cell_loc[1]-1)
                    if (key in key_arr):
                        dead_cell_neighbors[key]+=1
                    else:
                        key_arr.append(key)
                        dead_cell_neighbors[key]=1


            if (cell_loc[0]-1!=-1 and cell_loc[1]+1!=self.width):                
                if (self.grid[cell_loc[0]-1][cell_loc[1]+1]==1):
                    neighbors+=1
                else:
                    key=str(cell_loc[0]-1)+str(cell_loc[1]+1)
                    if (key in key_arr):
                        dead_cell_neighbors[key]+=1
                    else:
                        key_arr.append(key)
                        dead_cell_neighbors[key]=1


            if (cell_loc[0]+1!=self.length and cell_loc[1]+1!=self.width):                
                if (self.grid[cell_loc[0]+1][cell_loc[1]+1]==1):
                    neighbors+=1
                else:
                    key=str(cell_loc[0]+1)+str(cell_loc[1]+1)
                    if (key in key_arr):
                        dead_cell_neighbors[key]+=1
                    else:
                        key_arr.append(key)
                        dead_cell_neighbors[key]=1


            if (cell_loc[0]+1!=self.length and cell_loc[1]-1!=-1):                
                if (self.grid[cell_loc[0]+1][cell_loc[1]-1]==1):
                    neighbors+=1
                else:
                    key=str(cell_loc[0]+1)+str(cell_loc[1]-1)
                    if (key in key_arr):
                        dead_cell_neighbors[key]+=1
                    else:
                        key_arr.append(key)
                        dead_cell_neighbors[key]=1


            if (cell_loc[0]-1!=-1 and cell_loc[1]-1!=-1):
                if (self.grid[cell_loc[0]-1][cell_loc[1]-1]==1):
                    neighbors+=1
                else:
                    key=str(cell_loc[0]-1)+str(cell_loc[1]-1)
                    if (key in key_arr):
                        dead_cell_neighbors[key]+=1
                    else:
                        key_arr.append(key)
                        dead_cell_neighbors[key]=1
                
            # print("y:", cell_loc[0], "x:", cell_loc[1], "neighbors:", neighbors, end=" ")
            if ((neighbors<2 or neighbors>3) and self.grid[cell_loc[0]][cell_loc[1]]==1):
                # print("dead")
                grid_new[cell_loc[0]][cell_loc[1]]=0
            # else:
                # print("alive")
            
            # if (neighbors!=8):

                # print('!8')
        
        # for cell_loc in self.cell_locs: # set alive
        #         # if not out of grid
        #         key=str(cell_loc[0])+str(cell_loc[1])
        #         if (key in key_arr):
        #             dead_cell_neighbors[key]+=1
        #         else:
        #             key_arr.append(key)
        #             dead_cell_neighbors[key]=1


        # Sets dead cells alive
        for key in dead_cell_neighbors:
            if (dead_cell_neighbors[key]==3):
                # print("y", key[0], "x", key[1], "neigbors:", dead_cell_neighbors[key])
                grid_new[int(key[0])][int(key[1])]=1


        self.grid=grid_new

    def print(self): # klasse funksjon
        # print("")
        os.system('cls' if os.name=='nt' else "printf '\033c'")
        for i in range(self.width+2):
            print("-", end="")
        print("")

        for y in range(self.length):
            print("|", end="")
            for x in range(self.width):
                if (self.grid[y][x]==1):
                    print(chr(9608), end='')
                else:
                    print(" ", end='')
            print("|", end="")
            print("")

        for i in range(self.width+2):
            print("-", end="")
        print("")
        time.sleep(0.4)



    def grid_setter_locs(self, cell_locs):
        # Resetter til null
        for y in range(1,self.length):
            for x in range(1,self.width):
                self.grid[y][x]=0

        # Setter cellene til de oppgitte lokasjoene til 1
        if (len(cell_locs)>0):
            for cell_loc in cell_locs:
                self.grid[cell_loc[0]][cell_loc[1]]=1

    def grid_setter_grid(self, grid):
        # print(len(self.grid))
        # print(len(self.grid[0]))
        self.grid=grid
        # print(len(grid))
        # print(len(grid[0]))
        # print(self.length)
        # print(self.width)


    # Funksjon som kan sjekke antall neighbors til en loc cell