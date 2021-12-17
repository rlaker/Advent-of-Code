#%%
from aocd.models import Puzzle
from aocd import submit
puzzle = Puzzle(year=2021, day=4)
print(puzzle.input_data_fname)
print(puzzle.input_data)
#%%
import numpy as np

def parse(puzzle_input):
    """
    Need to split into the drawn balls and each bingo card
    """
    split_n = puzzle_input.split('\n')
    drawn_balls = np.asarray(split_n[0].split(',')).astype(int)
    
    #now split the boards into an array No boardsx5x5
    #then hopefully I can make a check board function that can be applied
    #over axis=0
    
    count = 0
    all_numbers = np.array([])
    for row in split_n[1:]:
        if len(row) > 0:
            if count == 0:
                shape_card = len(row.split())
            #empty separator does it by whitespace
            all_numbers = np.concatenate([all_numbers, np.asarray(row.split()).astype(int)])
            
    N = all_numbers.shape[0]//(shape_card**2)
    print(f'{N} cards, each shaped {shape_card}x{shape_card}')
    #convert all rows and add to an array, then reshape
    cards = all_numbers.reshape(N, shape_card, shape_card).astype(int)
    
    return cards, drawn_balls

def check_card(card):
    """this will check a single card, which can be upscaled by applying along an axis"""
    #card wins if there is a complete row or column
    #go across rows
    if np.all(card == True, axis = 1).any() or np.all(card == True, axis = 0).any():
        return True
    else:
        return False
    
    
    
def part1(cards, drawn_balls):
    winning_idx = []
    for i, ball in enumerate(drawn_balls):
        print(ball)
        #cross of all the balls so far
        crossed_off = np.in1d(cards, drawn_balls[:i+1]).reshape(cards.shape)
        
        #now check if any card has won
        for idx, card in enumerate(crossed_off):
            
            if check_card(card):
                winning_idx.append(idx)
                
                #get the sum of unchecked numbers
                sum_unmarked = np.sum(cards[idx][~crossed_off[idx]])
                answer = sum_unmarked * ball
                
                return answer, winning_idx
                #what happens if two cards win at the same time

def part2(cards, drawn_balls):
    
    #same but now if a card wins remove it from the array until the last card exists
    
    #I should do this to improve performance but cba
    #losing_cards = cards
    
    losing_idc = [i for i in range(cards.shape[0])]
    #start at -1 so first value is 0
    ball_idx  = -1
    has_won = False
    while len(losing_idc) > 1 or has_won == False:
        
        ball_idx += 1
        ball = drawn_balls[ball_idx]
        
        crossed_off = np.in1d(cards, drawn_balls[:ball_idx+1]).reshape(cards.shape)
        
        if len(losing_idc)<5:
            print(f'ball no {ball}, idx {ball_idx}')
            print(losing_idc)
            print('')
            
        #now check if any card has won
        for idx, card in enumerate(crossed_off):
            if idx in losing_idc:
                if check_card(card):
                    
                    #if only one left then I am waiting until it wins
                    if len(losing_idc) == 1:
                        #get the sum of unchecked numbers
                        losing_idx = losing_idc[0]
                        print(f"card {losing_idx}, when idx {ball_idx} is picked")
                        sum_unmarked = np.sum(cards[losing_idx][~crossed_off[losing_idx]])
                        answer = sum_unmarked * ball
    
                        return answer, losing_idx
                    
                    else:
                        #remove from losing list because it won
                        losing_idc.remove(idx)
                    
    
        
    
    
    
    
#%%       
if __name__ == '__main__':
    puzzle_input = puzzle.input_data
    cards, drawn_balls = parse(puzzle_input)
    #soln_a, winning_idx = part1(cards, drawn_balls)
    #print(f'this card won {winning_idx}')
    #submit(soln_a, part='a', day = 4, year = 2021)
    soln_b, losing_idx = part2(cards,drawn_balls)
    submit(soln_b, part='b', day = 4, year = 2021)

# %%
