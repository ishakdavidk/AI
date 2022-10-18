'Source: https://www.youtube.com/watch?v=G_UYXzGuqvM&ab_channel=Computerphile'

import numpy as np
import sys

grid = []
solution = None


def constrain(y,x,d):
    for i in range(0,9):
        if grid[y][i] == d:
            return False
    for i in range(0,9):
        if grid[i][x] == d:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == d:
                return False
    return True


def solve():
    global grid, solution
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for d in range(1,10):
                    if constrain(y,x,d):
                        grid[y][x] = d
                        solve()
                        grid[y][x] = 0
                return
    solution = np.copy(grid)


def get_input():
    global grid
    for _ in range(9):
        input_raw = input()
        int_list = list(map(int, input_raw.split(" ")))
        if len(int_list) != 9:
            sys.exit('Input per row must be 9 integers')
        grid.append(int_list)


'''
0 4 0 0 0 0 0 0 0
0 0 1 0 3 4 6 2 0
6 0 3 0 0 0 0 7 0
0 0 0 4 8 3 5 0 7
0 0 0 0 5 0 0 6 0
0 0 0 0 0 9 0 4 0
0 0 5 0 0 0 0 0 1
8 0 0 5 4 7 3 9 6
0 0 0 0 2 1 0 0 0
'''

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_input()
    solve()

    if solution is not None:
        for i in range(9):
            for j in range(9):
                print(solution[i][j], end=' ')
            print('')


