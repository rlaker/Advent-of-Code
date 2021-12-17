import pathlib as path
import pytest
import day5 as mycode
import io
from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2021, day=5)

PUZZLE_DIR = path.Path(puzzle.input_data_fname).parent
example_fname = PUZZLE_DIR / f"{puzzle.year}_{puzzle.day:02}_example_input.txt"

@pytest.fixture
def example1():
    with io.open(example_fname, encoding="utf-8") as f:
        puzzle_example = f.read()
    
    return puzzle_example

def test_parse_example1(example1):
    coords_start, coords_end = mycode.parse(example1)
    assert np.allclose(coords_start, np.array([[0,9], [8,0], [9,4],[2,2],[7,0],[6,4],[0,9],[3,4],[0,0],[5,5]]))

def test_part1(example1):
    coords_start, coords_end = mycode.parse(example1)
    assert mycode.part1(coords_start, coords_end) == 5
    
def test_part2(example1):
    coords_start, coords_end = mycode.parse(example1)
    assert mycode.part2(coords_start, coords_end) == 12