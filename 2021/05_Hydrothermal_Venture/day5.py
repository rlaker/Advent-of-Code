#%%
from aocd.models import Puzzle
from aocd import submit

#%%
import numpy as np

def parse(puzzle_input):
    raw_coords = [i for i in puzzle_input.split("\n")]
    
    coords_start = []
    coords_end = []
    for line in raw_coords:
        split_coords = line.split(' -> ')
        coord_start = np.asarray(split_coords[0].split(',')).astype(int)
        coord_end = np.asarray(split_coords[1].split(',')).astype(int)
        
        coords_start.append(coord_start)
        coords_end.append(coord_end)
    
    return np.vstack(coords_start), np.vstack(coords_end)

def part1(coords_start, coords_end):
    
    #find just horizontal lines
    horiz_idc  = np.argwhere(coords_start[:, 0] == coords_end[:,0]).flatten()
    vertical_idc  = np.argwhere(coords_start[:, 1] == coords_end[:,1]).flatten()
    
    lines_to_select = np.concatenate((horiz_idc, vertical_idc))
    
    print(lines_to_select)
    dimension = np.max([coords_start.max(), coords_end.max()]) + 1
    line_map = np.zeros((dimension, dimension))
    
    lines_start = coords_start[lines_to_select]
    lines_end = coords_end[lines_to_select]
    
    for line_start, line_end in zip(lines_start, lines_end):
        #get the map and add 1 everywhere the line exists
        #so for horizontal lines keep y the same and get every index between start and end x
        if line_start[1] == line_end[1]:
            #arange only ever increases, so make
            if line_start[0] > line_end[0]:
                x_idx = np.arange(line_end[0], line_start[0]+1)
            else:
                x_idx = np.arange(line_start[0], line_end[0]+1)
            y_idx = line_start[1]
        #vertical line
        elif line_start[0] == line_end[0]:
            if line_start[1] > line_end[1]:
                y_idx = np.arange(line_end[1], line_start[1]+1)
            else:
                y_idx = np.arange(line_start[1], line_end[1]+1)
            x_idx = line_start[0]
        print(line_start)
        print(x_idx, y_idx)
        print('')
        line_map[y_idx, x_idx] += 1
        
    #how many where at least two lines overlap
    return np.argwhere(line_map >= 2).shape[0]
        
def part2(coords_start, coords_end):
    
    
    dimension = np.max([coords_start.max(), coords_end.max()]) + 1
    line_map = np.zeros((dimension, dimension))
    
    
    for line_start, line_end in zip(coords_start, coords_end):
        #get the map and add 1 everywhere the line exists
        #so for horizontal lines keep y the same and get every index between start and end x
        if line_start[1] == line_end[1]:
            #arange only ever increases, so make
            if line_start[0] > line_end[0]:
                x_idx = np.arange(line_end[0], line_start[0]+1)
            else:
                x_idx = np.arange(line_start[0], line_end[0]+1)
            y_idx = line_start[1]
        #vertical line
        elif line_start[0] == line_end[0]:
            #arange only works when number increases
            if line_start[1] > line_end[1]:
                y_idx = np.arange(line_end[1], line_start[1]+1)
            else:
                y_idx = np.arange(line_start[1], line_end[1]+1)
            x_idx = line_start[0]
            
        else:
            #I know they are diagonal
            
            #both increasing (downward right diagonal)
            if line_start[0] < line_end[0] and line_start[1] < line_end[1]:
                x_idx = np.arange(line_start[0], line_end[0]+1)
                y_idx = np.arange(line_start[1], line_end[1]+1)
            
            #downward left 
            elif line_start[0] > line_end[0] and line_start[1] < line_end[1]:

                x_idx = np.arange(line_start[0], line_end[0]-1, -1)
                y_idx= np.arange(line_start[1], line_end[1]+1)
                
            # upward_right
            elif line_start[0] < line_end[0] and line_start[1] > line_end[1]:

                x_idx = np.arange(line_start[0], line_end[0]+1)
                y_idx= np.arange(line_start[1], line_end[1]-1, -1)
            
            #upward left
            elif line_start[0] > line_end[0] and line_start[1] > line_end[1]:
                #this is functionally the same as downward right if I swap start and end
                #which is what I have done
                x_idx = np.arange(line_end[0], line_start[0]+1)
                y_idx= np.arange(line_end[1], line_start[1]+1)
                
            else:
                print('missed', line_start, line_end)
            
        print(line_start, line_end)
        #print(x_idx, y_idx)
        line_map[y_idx, x_idx] += 1
        test_map = np.zeros((dimension, dimension))
        test_map[y_idx, x_idx] += 1
        #print(test_map)
        print('')
    
    print(line_map)
    #how many where at least two lines overlap
    return np.argwhere(line_map >= 2).shape[0], line_map
    
# %%
if __name__ == '__main__':
    puzzle = Puzzle(year=2021, day=5)
    # print(puzzle.input_data_fname)
    # print(puzzle.input_data)
    
    coords_start, coords_end = parse(puzzle.input_data)
    # soln_a = part1(coords_start, coords_end)
    
    #submit(soln_a, part = 'a', day = 5, year=2021)
    soln_b, line_map = part2(coords_start, coords_end)
    print(soln_b)
    submit(soln_b, part="b", year = 2021, day = 5)
# %%
