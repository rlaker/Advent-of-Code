# test_aoc_template.py


import pytest
import day4 as mycode
import numpy as np

@pytest.fixture
def example1():
    
    return "98,99\n\n98 99\n10 10\n\n10 10\n10 10"

@pytest.fixture
def parsed(example1):
    cards, drawn_balls = mycode.parse(example1)
    return [cards, drawn_balls]


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    cards, drawn_balls = mycode.parse(example1) 
    assert np.allclose(drawn_balls, np.array([98,99]))
    assert np.allclose(cards, np.array([[[98,99],[10,10]],[[10,10],[10,10]]]))



def test_part1_example(example1):
    """Test part 1 on example input"""
    cards, drawn_balls = mycode.parse(example1)
    answer, _ = mycode.part1(cards, drawn_balls)
    assert  answer == 20*99


@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example1):
    """Test part 2 on example input"""