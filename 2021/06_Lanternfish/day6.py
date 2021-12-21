#%%
from aocd.models import Puzzle
from aocd import submit

import numpy as np
#%%
def parse(puzzle_input):
    return np.asarray(puzzle_input.split(",")).astype(int)

def part1(start_fish, n_days = 80):
    fish = start_fish
    
    for day_no in np.arange(0, n_days):
        # print(day_no)
        #find all the fish at zero
        zero_idc = np.argwhere(fish < 1).flatten()
        not_zero = np.argwhere(fish >= 1).flatten()
        #change these to a 6
        fish[zero_idc] = 6
        #now add all the new fish to the end
        fish = np.append(fish, np.ones(zero_idc.shape[0])*8)

        fish[not_zero] -= 1
        # print(fish)
        # print('')
        
    return fish.shape[0]


def how_many_resets(n_days):
    "This is how many times a newly created fish will reset in n_days"

    if n_days < 8:
        return 0
    else:
        return 1+ (n_days - 8) // 6 

def get_days_left(n_days):
    if n_days < 8:
        return np.array([])
    else:
        no_resets = 1+ (n_days - 8) // 6
        days_left = n_days - (np.ones(no_resets)*8 + np.arange(0, no_resets)*6)
        return days_left
    
def get_reset_days(n_days):
    if n_days < 8:
        return np.array([])
    else:
        no_resets = 1+ (n_days - 8) // 6
        return np.ones(no_resets)*8 + np.arange(0, no_resets)*6

def just_one_fish(n_days = 80, new = True):
    no_fish = 1
    
    if new:
        days_left = get_days_left(n_days).astype(int)
    else:
        no_resets = n_days // 6
        days_left = n_days - np.arange(1, no_resets+1)*6
        days_left = days_left.astype(int)
    # print(f'Original days left: {n_days}, days list {days_left}')
    for left in days_left:
        # print(f'Original days left: {n_days}, left {left}')
        #for each set of resets this fish will create a new one
        no_fish += just_one_fish(left)
        
    # print('')
    return no_fish

def part2(start_fish, n_days):
    
    current_states = {
        0: start_fish[start_fish==0].shape[0],
        1: start_fish[start_fish==1].shape[0],
        2: start_fish[start_fish==2].shape[0],
        3: start_fish[start_fish==3].shape[0],
        4: start_fish[start_fish==4].shape[0],
        5: start_fish[start_fish==5].shape[0],
        6: start_fish[start_fish==6].shape[0],
        7: 0,
        8: 0,
    }
    
    for day in np.arange(0, n_days):
        #this is genius from the reddit guy
        #so you just shift it down one, now all those that where at
        #0 have become baby fish that take 8 to reproduce
        next_states = {
            0: current_states[1],
            1: current_states[2],
            2: current_states[3],
            3: current_states[4],
            4: current_states[5],
            5: current_states[6],
            6: current_states[7],
            7: current_states[8],
            8: current_states[0],
        }
    
    
        #but the ones that were already 0 have to be reset to 6
        if current_states[0] > 0:
            next_states[6] += current_states[0]
            
        current_states = next_states
        next_states = {}
        
    no_fish = 0
    #now sum, up all fish
    for fish_state in current_states:
        no_fish += current_states[fish_state]
    return no_fish

def part2_arr(start_fish, n_days):
    
    current_state = np.array([
        start_fish[start_fish==0].shape[0],
        start_fish[start_fish==1].shape[0],
        start_fish[start_fish==2].shape[0],
        start_fish[start_fish==3].shape[0],
        start_fish[start_fish==4].shape[0],
        start_fish[start_fish==5].shape[0],
        start_fish[start_fish==6].shape[0],
        0,
        0,
    ], dtype = np.float64)
    
    for day in np.arange(0, n_days):
        
        next_state = current_state[1:]
        #make NEW fish
        next_state = np.append(next_state, current_state[0])
        #return all the fish at zero to state6
        if current_state[0] > 0:
            next_state[6] += current_state[0]
        
        current_state = next_state
        next_state = np.zeros(9)
        
        
    return np.sum(current_state)
        
# %%
if __name__ == '__main__':
    puzzle = Puzzle(year = 2021, day = 6)
    start_fish = parse(puzzle.input_data)
    
    soln_a = part1(start_fish)
    #submit(soln_a, part = "a", year = 2021, day = 6)
    
    soln_b = part2(start_fish, 256)
    #submit(soln_b, part = 'b', year = 2021, day = 6)