import numpy as np
import sys
from itertools import combinations
from functools import reduce
import time


tops, sides = [], []
tops_opts, sides_opts = [], []
h, w = 0, 0
grid = []
solution = None


def update_opts(opts_matrix, place_proc):
    filtered_opts = []
    for opt_vec in opts_matrix:
        opt_pass = True
        for i in range(len(place_proc)):
            if place_proc[i] == '*' and opt_vec[i] == -1:
                opt_pass = False
                break
            elif place_proc[i] == '-' and opt_vec[i] == 1:
                opt_pass = False
                break
        if opt_pass:
            filtered_opts.append(opt_vec)
    filtered_opts = np.array(filtered_opts)

    return filtered_opts


def overlap(opts_matrix, place_proc):
    filtered_opts = update_opts(opts_matrix, place_proc)

    if len(filtered_opts) > 0:
        sum_filt_opts = np.sum(filtered_opts, axis=0)
        pos_overlap_idxs = np.where(sum_filt_opts == len(filtered_opts))
        neg_overlap_idxs = np.where(sum_filt_opts == -len(filtered_opts))

        return pos_overlap_idxs, neg_overlap_idxs, filtered_opts
    else:
        sys.exit('There is no solution')


def generate_all_opts(places, groups):
    n_empty = places - (sum(groups) + (len(groups) - 1))
    opts = combinations(range(len(groups) + n_empty), len(groups))

    opts_matrix = []
    for opt in opts:
        opt_vec = [-1] * places
        start = 0
        for i in range(len(opt)):
            for j in range(groups[i]):
                opt_vec[start + opt[i] + j] = 1
            start = start + groups[i]
        opts_matrix.append(opt_vec)
    opts_matrix = np.array(opts_matrix)

    return opts_matrix


def get_input():
    global grid, tops, sides, h, w
    h, w = map(int, input().split(' '))
    for _ in range(h):
        input_raw = input()
        int_list = list(map(int, input_raw.split(" ")))
        sides.append(int_list)
    for _ in range(w):
        input_raw = input()
        int_list = list(map(int, input_raw.split(" ")))
        tops.append(int_list)

    for _ in range(h):
        grid_row = []
        for _ in range(w):
            grid_row.append(' ')
        grid.append(grid_row)

    grid = np.array(grid)


'''
10 10
1 1
2 2
5
1 1 1
7
5 2
3 1
3 1
4 2
7
1
6
2 6
8
2 6
6 2
1 1
1
1 2
4
'''

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_input()

    for i in range(len(sides)):
        sides_opts.append(generate_all_opts(w, sides[i]))
    for j in range(len(tops)):
        tops_opts.append(generate_all_opts(h, tops[j]))

    proc_iter = 0
    while True:
        for i in range(len(sides)):
            if sides[i][0] != -1:
                pos_overlap_idxs, neg_overlap_idxs, filtered_opts = overlap(sides_opts[i], grid[i, :])
                sides_opts[i] = filtered_opts
                for pos_overlap_idx in pos_overlap_idxs[0]:
                    grid[i, pos_overlap_idx] = '*'
                for neg_overlap_idx in neg_overlap_idxs[0]:
                    grid[i, neg_overlap_idx] = '-'
                if len(filtered_opts) == 1:
                    sides[i] = [-1]

        for j in range(len(tops)):
            if tops[j][0] != -1:
                pos_overlap_idxs, neg_overlap_idxs, filtered_opts = overlap(tops_opts[j], grid[:, j])
                tops_opts[j] = filtered_opts
                for pos_overlap_idx in pos_overlap_idxs[0]:
                    grid[pos_overlap_idx, j] = '*'
                for neg_overlap_idx in neg_overlap_idxs[0]:
                    grid[neg_overlap_idx, j] = '-'
                if len(filtered_opts) == 1:
                    tops[j] = [-1]

        proc_iter += 1
        if proc_iter == 1000:
            print(f'Cannot find the solution after {proc_iter} row and column iterations.')
            break

        if np.sum(np.sum(sides)) == -len(sides) and np.sum(np.sum(tops)) == -len(tops):
            print(f'Find the solution after {proc_iter} row and column iterations.')
            break

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '*':
                print(grid[i][j], end='')
            else:
                print(' ', end='')
        print()


