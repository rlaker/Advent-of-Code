import pathlib as path
import pytest
import day9 as mycode
import io
from aocd.models import Puzzle
import numpy as np

@pytest.fixture
def example():
    return "2199943210\n3987894921\n9856789892\n8767896789\n9899965678"

def test_parse(example):
    height_map = mycode.parse(example)
    
    assert np.allclose(height_map[0, :], np.array([2,1,9,9,9,4,3,2,1,0]))
    
def test_part1(example):
    height_map = mycode.parse(example)
    assert mycode.part1(height_map) == 15
    
def test_part2(example):
    height_map = mycode.parse(example)
    assert mycode.part2(height_map) == 1134 