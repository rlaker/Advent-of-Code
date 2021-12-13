# test_aoc_template.py

import pathlib as path
import pytest
import day3 as mycode
import io
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=3)


PUZZLE_DIR = path.Path(puzzle.input_data_fname).parent
example_fname = PUZZLE_DIR / f"{puzzle.year}_{puzzle.day:02}_example_input.txt"

@pytest.fixture
def example1():
    with io.open(example_fname, encoding="utf-8") as f:
        puzzle_example = f.read()
    print(puzzle_example)
    return mycode.parse(puzzle_example)



def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == ['00100','11110','10110','10111','10101','01111','00111','11100','10000', '11001', '00010', '01010']


def test_part1_example(example1):
    """Test part 1 on example input"""
    assert mycode.part1(example1) == 198


@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example1):
    """Test part 2 on example input"""
    
def test_gamma(example1):
    assert mycode.get_gamma(example1) == 22

def test_epsilon(example1):
    assert mycode.get_epsilon(example1) == 9

def test_oxygen_rating(example1):
    assert mycode.get_oxygen_rating(example1) == 23
    
def test_co2_rating(example1):
    assert mycode.get_co2_rating(example1) == 10
    
def test_life_support_rating(example1):
    assert mycode.get_life_support_rating(example1) == 230