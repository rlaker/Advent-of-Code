# test_aoc_template.py

import pathlib as path
import pytest
import day1 as mycode
import io
from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2021, day=1)


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
    assert example1 == [199,200,208,210,200,207,240,269,260,263]


def test_part1_example(example1):
    """Test part 1 on example input"""
    assert mycode.part1(example1) == 7


def test_part2_example(example1):
    """Test part 2 on example input"""
    assert mycode.part2(example1) == 5