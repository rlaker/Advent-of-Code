#%%
from aocd.models import Puzzle
from aocd import submit

#%%
import numpy as np

def parse(puzzle_input):
    return puzzle_input.split('\n')


def common_colm(data, idx, mode = 'most'):
    count_0 = 0
    count_1 = 0
    for byte in data:
        if byte[idx] == '0':
            count_0 += 1
        elif byte[idx] == '1':
            count_1 += 1
        else:
            raise Exception("Not a 0 or 1")
    
    if count_0 > count_1:
        if mode == 'most':
            return '0'
        else:
            return '1'
    elif count_0 < count_1:
        if mode == 'most':
            return '1'
        else:
            return '0'
    elif count_0 == count_1:
        if mode == 'most':
            return '1'
        else:
            return '0'
    
    
def get_gamma(data):
    gamma_str = ''
    for i in np.arange(0,len(data[0])):
        gamma_str += common_colm(data, i, mode = 'most')

    return int(gamma_str, 2)

def get_epsilon(data):
    epsilon_str = ''
    for i in np.arange(0,len(data[0])):
        epsilon_str += common_colm(data, i, mode = 'least')

    return int(epsilon_str, 2)

def part1(data):
    
    gamma = get_gamma(data)
    epsilon = get_epsilon(data)
    
    return gamma*epsilon
    
def search_for_bit(data, bit, idx):
    matching = []
    for byte in data:
        if byte[idx] == bit:
            matching.append(byte)
    return matching

def get_generic_rating(data, mode = 'most'):
    remaining_bytes = data.copy()
    idx = 0
    # print(remaining_bytes)
    while len(remaining_bytes) > 1:
        #do the logic
        to_search = common_colm(remaining_bytes, idx, mode)
        
        #now search all the bytes with this as the first bit
        matching = search_for_bit(remaining_bytes, to_search, idx)
        
        remaining_bytes = matching.copy()
        # print(idx, to_search, remaining_bytes)
        idx += 1
    
    return int(remaining_bytes[0],2)
    

def get_oxygen_rating(data):
    return get_generic_rating(data, 'most')

def get_co2_rating(data):
    return get_generic_rating(data, 'least')

def get_life_support_rating(data):
    return get_oxygen_rating(data) * get_co2_rating(data)
    

#%%
    

if __name__ == '__main__':
    puzzle = Puzzle(year=2021, day=3)

    data  = parse(puzzle.input_data)
    soln = part1(data)
    # print(soln)
    part2_soln = get_life_support_rating(data)
    #submit(soln, part="a", day=3, year=2021)
    # submit(part2_soln, part = "b", day = 3, year = 2021)

# %%
