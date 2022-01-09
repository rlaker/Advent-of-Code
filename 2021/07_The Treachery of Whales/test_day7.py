import pathlib as path
import pytest
import day7 as mycode
import io
from aocd.models import Puzzle
import numpy as np


@pytest.fixture
def example1():
    return "16,1,2,0,4,2,7,1,2,14"

def test_parse(example1):
    assert np.allclose(mycode.parse(example1), np.array([16,1,2,0,4,2,7,1,2,14]))

def test_part1(example1):
    start_position = mycode.parse(example1)
    end_position, fuel = mycode.find_best_position(start_position)
    assert end_position == 2
    assert fuel == 37
    
def test_part2(example1):
    start_position = mycode.parse(example1)
    end_position, fuel = mycode.find_best_position(start_position, mycode.fuel_part2)
    assert end_position == 5
    assert fuel == 168