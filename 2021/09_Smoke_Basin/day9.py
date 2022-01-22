#%%
from aocd.models import Puzzle
from aocd import submit

import numpy as np
#%%

def parse(puzzle_input):
    str_rows = puzzle_input.split('\n')
    rows = []
    for str_row in str_rows:
        row_list = []
        for char in str_row:
            row_list.append(int(char))
        rows.append(row_list)
        
    return np.vstack(rows)



def part1(height_map):
    original = np.copy(height_map)
    
    
    shifted_up = np.roll(height_map, shift = -1, axis = 0)
    shifted_down = np.roll(height_map, shift = 1, axis = 0)
    shifted_left = np.roll(height_map, shift = -1, axis = 1)
    shifted_right = np.roll(height_map, shift = 1, axis = 1)
    
    #what is the difference between this element and one to the left
    #we have to shift the reference map to the right
    diff2left = original - shifted_right
    #do not allow the array to wrap around, so set the left most to -1
    # since I want the condition to be true later on
    diff2left[:, 0] = -1
    
    diff2right = original - shifted_left
    diff2right[:, -1] = -1
    
    diff2up = original - shifted_down
    diff2up[0, :] = -1
    
    diff2down = original - shifted_up
    diff2down[-1, :] = -1

    idc = np.argwhere((diff2down<0) & (diff2up<0) & (diff2left<0) & (diff2right<0))

    total_risk = 0
    for coordinate in idc:
        risk = original[coordinate[0], coordinate[1]] + 1
        total_risk += risk

    return total_risk
#%%
if __name__ == '__main__':
    puzzle = Puzzle(year = 2021, day = 9)
    height_map = parse(puzzle.input_data)
    
    soln_a = part1(height_map)
    
    submit(soln_a, part='a', year=2021, day = 9)
    
# %%
