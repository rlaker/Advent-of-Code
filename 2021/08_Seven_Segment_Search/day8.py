#%%
from aocd.models import Puzzle
from aocd import submit

import numpy as np
#%%

def parse(puzzle_input):
    lines = puzzle_input.split('\n')
    split_lines = []
    for line in lines:
        line_split = line.split(' ')
        split_lines.append(line_split[:10] + line_split[-4:])
        
    return split_lines


def part1(split_lines): 
    count = 0
    
    for line in split_lines:
        set_of_4 = line[-4:]
        for group in set_of_4:
            length_of_group = len(group)
            unique_digits = [2,3,4,7]
            if length_of_group in unique_digits:
                count += 1
    
    return count

#decoding

def diff_groups(group1, group2):
    if len(group1) > len(group2):
        diff = [x for x in group1 if x not in group2]
    else:
        diff = [x for x in group2 if x not in group1]
    

    return diff


def sim_groups(group1, group2):
    if len(group1) > len(group2):
        sim = [x for x in group1 if x in group2]
    else:
        sim = [x for x in group2 if x in group1]
    

    return sim
    
    
def get_digit_encoding(row):
    
    #reorder by length since I need to go in order
    sorted_row = sorted(row, key=len)
    
    digits = {}
    
    #get all the known numbers
    for i, group in enumerate(sorted_row):
        length = len(group)
        
        if length == 2:
            digits[1] = group

        elif length == 3:
            digits[7] = group

        elif length == 4:
            digits[4] = group
            
        elif length == 7:
            digits[8] = group
            
        elif length == 6:
            #compare all the length 6 with 1
            #if it only differs by 1 then it is the 6
            # print(group, sim_groups(group, digits[1]))
            if len(sim_groups(group, digits[1])) == 1:
                digits[6] = group
            else:
                #now we know this one isn't a six
                #compare with 4 if only three different and not a 6 then a 0
                if len(sim_groups(group, digits[4])) == 3:
                    digits[0] = group
                else:
                    #has to be a 9 then
                    digits[9] = group
        
        elif length == 5:
            #compare 3 and 1. if they share 2 segments then it has to be a three
            if len(sim_groups(group, digits[1])) == 2:
                digits[3] = group
            else:
                #now wether a 2 or 5. so compare with 4
                if len(sim_groups(group, digits[4])) == 2:
                    digits[2] = group
                else:
                    digits[5] = group            

    return digits



def get_row_answer(row, digits):
    #last 4 groups
    answer = ''
    for number in row[-4:]:
        for key in digits.keys():
            
            if sorted(number) == sorted(digits[key]):
                answer += str(key)
    return int(answer)

def part2(split_lines):
    summ = 0
    for row in split_lines:
        digits = get_digit_encoding(row)
        row_answer = get_row_answer(row, digits)
        print(row_answer)
        print('')
        summ+=row_answer

    return summ


#now do the actual task
test = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe\nedbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc\nfgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg\nfbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb\naecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea\nfgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb\ndbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe\nbdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef\negadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb\ngcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
split_lines = parse(test)
print(part2(split_lines))

#%%
if __name__ == '__main__':
    puzzle = Puzzle(year = 2021, day = 8)
    
    split_lines = parse(puzzle.input_data)
    #soln_a = part1(split_lines)
    
    #submit(soln_a, part='a', year=2021,day=8)
    
    soln_b = part2(split_lines)
    print(soln_b)
    
    submit(soln_b, part='b',year = 2021, day = 8)

# %%
