import pathlib as path
import pytest
import day6 as mycode
import io
from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2021, day=5)

PUZZLE_DIR = path.Path(puzzle.input_data_fname).parent
example_fname = PUZZLE_DIR / f"{puzzle.year}_{puzzle.day:02}_example_input.txt"

@pytest.fixture
def example1():
    return "3,4,3,1,2"

def test_parse_example1(example1):
    assert np.allclose(mycode.parse(example1), np.array([3,4,3,1,2]))
    
    
def test_part1(example1):
    start_fish = mycode.parse(example1)
    assert mycode.part1(start_fish) == 5934
    
def test_part1_better(example1):
    start_fish = mycode.parse(example1)
    assert mycode.part2(start_fish, 80) == 5934
    
def test_part2(example1):
    start_fish = mycode.parse(example1)
    assert mycode.part2(start_fish, 256) == 26_984_457_539