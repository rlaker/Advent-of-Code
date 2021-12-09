#%%
from aocd.models import Puzzle
from aocd import submit
puzzle = Puzzle(year=2021, day=1)
print(puzzle.input_data_fname)

import numpy as np

def parse(puzzle_input):
    return [int(line) for line in puzzle_input.split()]



def part1(data):
    """Solves day 1 puzzle

    Parameters
    ----------
    array : array
        Array of depths of the submarine
    """
    array = np.asarray(data)
    #gets the differences, finds where positive and returns the shape
    return np.where(np.diff(array) > 0)[0].shape[0]

def part2(data, window_size = 3):
    """Now I want a sliding window of size 3, then run part1 on it

    Parameters
    ----------
    array : array
        Same input data as before
    """
    array = np.asarray(data)
    N = array.shape[0]
    #get the indices for sliding window 
    # [[0,1,2]    [[0,1,2]     [[0,0,0]
    # [1,2,3]   =  [0,1,2]   +  [1,1,1]
    # [2,3,4]]     [0,1,2]]     [2,2,2]]
    index_arr = np.array([np.arange(0,window_size)]) + np.arange(0, N-window_size+1).reshape(N-window_size+1,1)
    
    
    sliced_arr = array[index_arr]
    summed_sliding = np.sum(sliced_arr, axis = 1)
    return part1(summed_sliding)
    

if __name__ == '__main__':
    data  = parse(puzzle.input_data)
    soln = part1(data)
    print(soln)
    part2_soln = part2(data)
    #submit(soln, part="a", day=1, year=2021)
    submit(part2_soln, part = "b", day = 1, year = 2021)
