#%%
from aocd.models import Puzzle
from aocd import submit

import numpy as np
#%%
def parse(puzzle_input):
    return np.asarray([i for i in puzzle_input.split(',')]).astype(int)

def fuel_part1(diff):
    return np.sum(abs(diff))

def fuel_part2(diff):
    crab_fuels = []
    for crab_dist in abs(diff):
        crab_fuels.append(np.sum(np.arange(1, crab_dist + 1)))
        
    return np.sum(np.asarray(crab_fuels))

def find_best_position(start_pos, fuel_func = fuel_part1):
    
    min_position = np.min(start_pos)
    max_position = np.max(start_pos)
    fuels = []
    final_positions = np.arange(min_position, max_position+1)
    for final_pos in final_positions:
        diff = start_pos - final_pos
        fuels.append(fuel_func(diff))
    fuels = np.asarray(fuels)
    min_fuel_idx = np.argmin(fuels)
    
    return final_positions[min_fuel_idx], fuels[min_fuel_idx]

# %%
if __name__ == '__main__':
    puzzle = Puzzle(year = 2021, day = 7)
    start_pos = parse(puzzle.input_data)
    final_pos, soln_a = find_best_position(start_pos)
    
    # submit(soln_a, part = "a", year = 2021, day = 7)
    
    final_pos, soln_b = find_best_position(start_pos, fuel_part2)
    submit(soln_b, part = "b", year = 2021, day =7)
# %%
