import pytest

from treasure_hunt.treasure_map import _transform_raw_map, WrongInputDataError


@pytest.mark.parametrize(
    'raw_map_inp, dimension, expected_map', (
        ('11 12\\n\\n21 22\\n.some\\ntrash\\nhere', 2, (
                (11, 12),
                (21, 22))),
        ('55 14 25 52 21\n\n44 31 11 53 43\n\n24 13 45 12 34'
         '\n\n42 22 43 32 41\n\n51 23 33 54 15', 5, (
                (55, 14, 25, 52, 21),
                (44, 31, 11, 53, 43),
                (24, 13, 45, 12, 34),
                (42, 22, 43, 32, 41),
                (51, 23, 33, 54, 15))),
    ))
def test_raw_map_ok_inp_transformation(raw_map_inp, dimension, expected_map):
    assert _transform_raw_map(raw_map_inp, n=dimension) == expected_map


@pytest.mark.parametrize(
    'raw_map_inp, dimension', (
        ('13 12 21 22', 2),
        ('11 12 21 222', 2),
        ('31 12 21 22', 2),
        ('11 12 21 22', 7),
    ))
def test_raw_map_bad_inp_transformation(raw_map_inp, dimension):
    with pytest.raises(WrongInputDataError):
        _transform_raw_map(raw_map_inp, n=dimension)
