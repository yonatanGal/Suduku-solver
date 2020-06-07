import math


def find_empty_cells(board, i, j):
    """ this function check for an empty cell to fill"""
    for num1 in range(i, len(board[0])):
        for num2 in range(j, len(board[0])):
            if board[num1][num2] == 0:
                return num1, num2
    for num3 in range(len(board[0])):
        for num4 in range(len(board[0])):
            if board[num3][num4] == 0:
                return num3, num4
    return None, None


def is_value_valid(board, i, j, num):
    """ this function checks if we can input a value num in the cell[i][j]"""
    row_check = all([num != board[i][x] for x in range(len(board[0]))])
    if row_check:
        column_check = all([num != board[x][j] for x in range(len(board[0]))])
        if column_check:
            square_side = int(math.sqrt(len(board)))
            # here i'm finding the top left cells of the square that i,j are in
            top_x = square_side * (i // square_side)
            top_y = square_side * (j // square_side)
            for k in range(top_x, top_x + square_side):
                for l in range(top_y, top_y + square_side):
                    if board[k][l] == num:
                        return False
            return True
    return False


def solve_sudoku(board, i=0, j=0):
    """ this function solves the sudoku game using backtracking """
    i, j = find_empty_cells(board, i, j)
    if i is None:
        print(board)
        return True  # that means that there are no 0's on the board
    for num in range(1, len(board[0]) + 1):
        if is_value_valid(board, i, j, num):
            board[i][j] = num
            if solve_sudoku(board, i, j):
                return True
            board[i][j] = 0  # this is the backtracking
    return False


def print_k_subsets(n, k):
    """ this function prints all possible subsets from a size of k out of n
    integers, each subset in a different line """
    if k > n:
        return
    elif k == 0 or n == 0:
        print([])
        return
    elif k <= n:
        cur_set = [False] * n
        k_subset_helper(cur_set, k, 0, 0)


def print_subset(cur_set):
    """ this is an inner function which only prints one subset each time """
    subset = []
    for (index, in_cur_set) in enumerate(cur_set):
        if in_cur_set:
            subset.append(index)
    print(subset)


def k_subset_helper(cur_set, k, index, picked):
    """ this is the backtracking function """
    if k == picked:  # base case, we picked k items
        print_subset(cur_set)
        return
    if index == len(cur_set):  # backtracking, we've reach the end of the list
        return
    cur_set[index] = True
    # runs on all sets including this index
    k_subset_helper(cur_set, k, index+1, picked+1)

    cur_set[index] = False
    # Runs on all sets that do not include index.
    k_subset_helper(cur_set, k, index+1, picked)


def fill_k_subsets(n, k, lst):
    """ this function receives numbers n and k, and an empty list, and fil
    this list with all the subsets of n  of size n-1. """
    if k == 0 or n == 0 or k > n:
        lst.append([])
        return
    if k <= n:
        cur_set = [False] * n
        fill_k_subset_helper(cur_set, k, 0, 0, lst)


def append_subset(cur_set, lst):
    """ this function appends subsets into a given list based on the cur_set."""
    temporary_lst = []
    for (index, in_cur_set) in enumerate(cur_set):
        if in_cur_set:
            temporary_lst.append(index)
    lst.append(temporary_lst)


def fill_k_subset_helper(cur_set, k, index, picked, lst):
    """ this is the backtracking function which creates the subsets """
    if k == picked:  # base case, we picked k items
        append_subset(cur_set, lst)
        return
    if index == len(cur_set):  # backtracking, we've reach the end of the list
        return
    cur_set[index] = True
    # runs on all sets including this index
    fill_k_subset_helper(cur_set, k, index + 1, picked + 1, lst)

    cur_set[index] = False
    # Runs on all sets that do not include index.
    fill_k_subset_helper(cur_set, k, index + 1, picked, lst)


def return_k_subsets(n, k):
    """ this function returns every possible subset of k items from 0 to n-1,
     without """
    if n < k or k < 0:
        return list()
    if k == n:
        return [list(range(k))]
    return return_k_subsets(n-1, k) + [sub_list+[n-1] for
                                       sub_list in return_k_subsets(n-1, k-1)]