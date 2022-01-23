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

def find_lowest_points(height_map):
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
    
    return idc

def part1(height_map):
    
    idc = find_lowest_points(height_map)
    
    total_risk = 0
    for coordinate in idc:
        risk = height_map[coordinate[0], coordinate[1]] + 1
        total_risk += risk

    return total_risk

def is_edge(idx, N):
    if idx < 1:
        return True
    elif idx >= N-1:
        return True
    else:
        return False

def find_around_element(height_map, idx):
    
    row_N = height_map.shape[0]
    col_N = height_map.shape[1]
    
    surround_idc = []
    if idx[0] > 0:
        #look left
        surround_idc.append([idx[0]-1, idx[1]])
    if idx[0] <= row_N-2:
        #look right
        surround_idc.append([idx[0]+1, idx[1]])
    if idx[1] > 0:
        #look up
        surround_idc.append([idx[0], idx[1]-1])
    if idx[1] <= col_N-2:
        #look down
        surround_idc.append([idx[0], idx[1]+1])
        
    return surround_idc

def plot_basin(points, height_map):
    display_map = np.ones(height_map.shape)
    for point in points:
        display_map[point[0], point[1]] = height_map[point[0], point[1]] 
    print(display_map)
    print('')

def find_basin_size(height_map, low_idx):
    """Given an initial low point, this will find all the other 
    points in the basin. Which is bound by 9s or the edge.
    
    Returns the size of the basin.
    """
    
    row_N = height_map.shape[0]
    col_N = height_map.shape[1]
    
    size = 1
    
    #start at the lowest point, find surrounding ones.
    # NOT diagonals
    
    points_in_basin = [low_idx]
    new_points = [low_idx]
    search = True
    
    while search:
        length_before = len(points_in_basin)
        #look around the new points
        points_on_this_pass = []
        for idx in new_points:
            around_element = find_around_element(height_map, idx)
            
            for new_point in around_element:
                if height_map[new_point[0], new_point[1]] < 9:
                    if new_point not in points_in_basin:
                        points_in_basin.append(new_point)
                        points_on_this_pass.append(new_point)
                        
        new_points = points_on_this_pass

        #if no new points added then stop the search
        if length_before == len(points_in_basin):
            search = False
    
    # plot_basin(points_in_basin, height_map)
    
    return len(points_in_basin)        
        
def part2(height_map):
    
    lowest_points = find_lowest_points(height_map)
    
    basin_sizes = []
    #each lowest point has a basin
    for lowest_point in lowest_points:
        print(lowest_point[0], lowest_point[1])
        basin_sizes.append(find_basin_size(height_map, list(lowest_point)))
        
    sorted_basin_sizes = sorted(basin_sizes)
    
    return sorted_basin_sizes[-3] * sorted_basin_sizes[-2] * sorted_basin_sizes[-1]

#%%
if __name__ == '__main__':
    puzzle = Puzzle(year = 2021, day = 9)
    height_map = parse(puzzle.input_data)
    
    soln_a = part1(height_map)
    
    # submit(soln_a, part='a', year=2021, day = 9)
    
    soln_b = part2(height_map)
    submit(soln_b, part='b', year=2021, day = 9)
