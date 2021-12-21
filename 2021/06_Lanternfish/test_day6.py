import pathlib as path
import pytest
import day6 as mycode
import io
from aocd.models import Puzzle
import numpy as np

@pytest.fixture
def example1():
    return "3,4,3,1,2"

def test_parse_example1(example1):
    assert np.allclose(mycode.parse(example1), np.array([3,4,3,1,2]))
    
    
def test_part1(example1):
    assert mycode.part1(mycode.parse(example1)) == 5934
    
def test_part1_better(example1):
    assert mycode.part2(mycode.parse(example1), 80) == 5934
    
def test_part2(example1):
    assert mycode.part2(mycode.parse(example1), 256) == 26_984_457_539

def test_part2_arr(example1):
    assert mycode.part2_arr(mycode.parse(example1), 256) == 26_984_457_539
