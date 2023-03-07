import copy
import time
import random

# Grids 1-5 are 2x2
grid1 = [
    [1, 0, 4, 2],
    [4, 2, 1, 3],
    [2, 1, 3, 4],
    [3, 4, 2, 1]]

grid2 = [
    [1, 0, 4, 2],
    [4, 2, 1, 3],
    [2, 1, 0, 4],
    [3, 4, 2, 1]]

grid3 = [
    [1, 0, 4, 2],
    [4, 2, 1, 0],
    [2, 1, 0, 4],
    [0, 4, 2, 1]]

grid4 = [
    [1, 0, 4, 2],
    [0, 2, 1, 0],
    [2, 1, 0, 4],
    [0, 4, 2, 1]]

grid5 = [
    [1, 0, 0, 2],
    [0, 0, 1, 0],
    [0, 1, 0, 4],
    [0, 0, 0, 1]]

grid6 = [
    [0, 0, 6, 0, 0, 3],
    [5, 0, 0, 0, 0, 0],
    [0, 1, 3, 4, 0, 0],
    [0, 0, 0, 0, 0, 6],
    [0, 0, 1, 0, 0, 0],
    [0, 5, 0, 0, 6, 4]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2)]
'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''


def check_section(section, n):
    if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n + 1)]):
        return True
    return False


def get_squares(grid, n_rows, n_cols):
    squares = []
    for i in range(n_cols):
        rows = (i * n_rows, (i + 1) * n_rows)
        for j in range(n_rows):
            cols = (j * n_cols, (j + 1) * n_cols)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][cols[0]:cols[1]]
                square += line
            squares.append(square)

    return (squares)


def check_solution(grid, n_rows, n_cols):
    '''
    This function is used to check whether a sudoku board has been correctly solved
    args: grid - representation of a suduko board as a nested list.
    returns: True (correct solution) or False (incorrect solution)
    '''
    n = n_rows * n_cols

    for row in grid:
        if check_section(row, n) == False:
            return False

    for i in range(n_rows):
        column = []
        for row in grid:
            column.append(row[i])
        if check_section(column, n) == False:
            return False

    squares = get_squares(grid, n_rows, n_cols)
    for square in squares:
        if check_section(square, n) == False:
            return False

    return True


def recursive_solve(grid, n_rows, n_cols):
    n = n_rows * n_cols

    # create a copy of the original grid
    solution = copy.deepcopy(grid)

    # find all empty cells in the grid
    empty_cells = [(i, j) for i in range(n)
                   for j in range(n) if solution[i][j] == 0]

    # loop through each empty cell and try to fill it with a valid value
    valid = True

    for cell in empty_cells:

        i, j = cell
        # find all possible values that can be placed in the empty cell

        possible_values = set(range(1, n + 1))
        for k in range(n):
            # check same row and column
            possible_values.discard(solution[k][j])
            possible_values.discard(solution[i][k])

            # check same square
            x = (i // n_rows) * n_rows + k // n_cols
            y = (j // n_cols) * n_cols + k % n_cols
            possible_values.discard(solution[x][y])

        # if there are no possible values, backtrack to previous cell
        if not possible_values:
            valid = False
            break

        # randomly choose a value from the possible values
        value = random.choice(list(possible_values))
        solution[i][j] = value

    # check if the completed grid is valid
    if valid and check_solution(solution, n_rows, n_cols):
        return solution

    # if maximum number of tries is reached and no valid solution is found,
    # return the original grid
    return grid


def random_solve(grid, n_rows, n_cols, max_tries=500):
    while not check_solution(grid, n_rows, n_cols):
        for i in range(4):
            for j in range(4):
                if grid[i][j] == 0:
                    grid[i][j] = random.randint(1, 4)
        if check_solution(grid, n_rows, n_cols):
            return grid
        else:
            grid = [[0 for x in range(4)] for y in range(4)]
    return grid


def solve(grid, n_rows, n_cols):
    '''
    Solve function for Sudoku coursework.
    Comment out one of the lines below to either use the random or recursive solver
    '''

    return random_solve(grid, n_rows, n_cols)
    return recursive_solve(grid, n_rows, n_cols)


'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''


def main():
    points = 0

    print("Running test script for coursework 1")
    print("====================================")

    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        print("Solving grid: %d" % (i + 1))
        start_time = time.time()
        solution = solve(grid, n_rows, n_cols)
        elapsed_time = time.time() - start_time
        print("Solved in: %f seconds" % elapsed_time)
        print(solution)
        if check_solution(solution, n_rows, n_cols):
            print("grid %d correct" % (i + 1))
            points = points + 10
        else:
            print("grid %d incorrect" % (i + 1))

    print("====================================")
    print("Test script complete, Total points: %d" % points)


if __name__ == "__main__":
    main()