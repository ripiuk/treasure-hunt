import pytest

from treasure_hunt.treasure_map import _transform_raw_map, \
    WrongInputDataError, get_treasure_map_from_file


@pytest.mark.parametrize('raw_map_inp, dimension, expected_map', (
    ('11 12 21 22', 2, (
        (11, 12),
        (21, 22))),

    ('11', 1, ((11,),)),

    ('11 12\n\\n21 22\n.some\ntrash\nmetal.here\nTestament?', 2, (
        (11, 12),
        (21, 22))),

    ('12.23     \n 33 11 13.21  22\n31 32', 3, (
        (12, 23, 33),
        (11, 13, 21),
        (22, 31, 32))),

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


@pytest.mark.parametrize('raw_map_inp, dimension', (
    ('13 12 21 22', 2),  # first element units is wrong
    ('10 12 21 22', 2),  # first element units is wrong
    ('31 12 21 22', 2),  # first element tens is wrong
    ('01 12 21 22', 2),  # first element tens is wrong
    ('11 12 21 222', 2),  # last element is wrong
    ('11 12 21 22', 7),  # wrong dimension number
    ('11 12 21 22', 0),  # dimension number not in range 1..9
    ('11 12 21 22', 10),  # dimension number not in range 1..9
    ('only text here', 2),  # no digits in the map
))
def test_raw_map_bad_inp_transformation(raw_map_inp, dimension):
    with pytest.raises(WrongInputDataError):
        _transform_raw_map(raw_map_inp, n=dimension)


def test_ok_input_map_from_file(tmpdir):
    mocked_treasure_map_f = tmpdir.mkdir("tmp").join("mocked_map.txt")
    mocked_treasure_map_f.write('12 21 22 22')
    assert get_treasure_map_from_file(mocked_treasure_map_f, 2) == ((12, 21), (22, 22))


def test_bad_input_map_from_file(tmpdir):
    mocked_treasure_map_f = tmpdir.mkdir("tmp").join("mocked_map.txt")
    mocked_treasure_map_f.write('32 21 22 22')  # first element tens is wrong
    with pytest.raises(WrongInputDataError):
        get_treasure_map_from_file(mocked_treasure_map_f, 2)
