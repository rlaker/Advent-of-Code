#%%
from requests.api import head


# =============================================================================
# Decided not to use the test driven model for this one as it is simple enough
# =============================================================================

from aocd.models import Puzzle
from aocd import submit
puzzle = Puzzle(year=2021, day=2)
print(puzzle.input_data_fname)
print(puzzle.input_data)
# %%
import pandas as pd
import numpy as np

def parse(puzzle_input):
    """Want to read into a pandas dataframe then should be easy

    Parameters
    ----------
    puzzle_input : string
        puzzle input, should be like forward 9
    """
    #replace the spaces with \n so there is only one separator
    #then take every other value
    directions = np.asarray(puzzle_input.replace(' ', '\n').split('\n')[::2])
    values_str = puzzle_input.replace(' ', '\n').split('\n')[1::2]
    values = np.asarray([int(i) for i in values_str])
    
    
    print(directions.shape[0])
    print(values.shape[0])
    return directions, values

def part1(directions, values):
    idx_up = np.argwhere(directions == 'up').flatten()
    idx_down = np.argwhere(directions == 'down').flatten()
    idx_forward = np.argwhere(directions == 'forward').flatten()
    
    
    total_forward = np.sum(values[idx_forward])
    #says that down ADDs to depth
    total_depth = np.sum(values[idx_up])*-1 + np.sum(values[idx_down])

    return total_depth*total_forward

def part2(directions, values):
    """Now there is another aim value, which is affected by up and down.
    So the submarine is tilted by up and down, and is moved forward along this
    aim direction

    Parameters
    ----------
    directions : [type]
        [description]
    values : [type]
        [description]
    """
    
    #aim will be the cumulative sum of the up and down directions
    #I am going to make a new up_down array which has the sign applied by the up or down instruction. Then I can run np.cumsum on this array to get the aim at each time.
    
    directions_copy = directions.copy()
    directions_copy[directions_copy == 'up'] = -1 
    directions_copy[directions_copy == 'down'] = 1 
    directions_copy[directions_copy == 'forward'] = 0     
    
    signed_up_or_down = directions_copy.astype(int)
    
    aim = np.cumsum(signed_up_or_down * values)
    
    #this bit is the same as before
    idx_forward = np.argwhere(directions == 'forward').flatten()
    forward_vals = values[idx_forward]
    horizontal_pos = np.sum(forward_vals)
    
    #increases depth by aim * value forward
    depth = np.sum(aim[idx_forward]*forward_vals)
    
    return horizontal_pos*depth

if __name__ == '__main__':
        
    directions, values = parse(puzzle.input_data)
    
    soln_a = part1(directions, values)
    print(soln_a)
    #submit(soln_a, part = 'a', day = 2, year = 2021)
    
    soln_b = part2(directions, values)
    print(soln_b)
    
    #submit(soln_b, part = 'b', day = 2, year = 2021)
# %%
