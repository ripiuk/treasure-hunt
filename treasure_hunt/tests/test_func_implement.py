import pytest

from treasure_hunt.func_implement import _make_treasure_path, _list_to_str, find_treasure


@pytest.mark.parametrize('treasure_map, expected_path', (
    (((11, 12), (21, 22)), [11]),
    (((21, 12), (21, 22)), [11, 21]),
    (((21, 12), (22, 22)), [11, 21, 22]),
    (((21, 12), (22, 12)), [11, 21, 22, 12]),
    (((55, 14, 25, 52, 21),
      (44, 31, 11, 53, 43),
      (24, 13, 45, 12, 34),
      (42, 22, 43, 32, 41),
      (51, 23, 33, 54, 15)), [11, 55, 15, 21, 44, 32, 13, 25, 43]),
))
def test_treasure_path(treasure_map, expected_path):
    assert _make_treasure_path(treasure_map) == expected_path
    assert find_treasure(treasure_map) == _list_to_str(expected_path)


@pytest.mark.parametrize('treasure_map', (
    ((22, 12), (21, 11)),  # 22 -> 11 -> 22
    ((22, 22), (21, 12)),  # 22 -> 12 -> 22 -> 12
    ((55, 14, 25, 52, 21),
     (44, 31, 11, 53, 43),
     (24, 13, 45, 12, 34),
     (42, 22, 43, 32, 41),
     (51, 23, 33, 54, 11)),  # 11 -> 55 -> 11
    ((55, 11, 25, 52, 21),
     (44, 31, 11, 53, 43),
     (24, 13, 45, 12, 34),
     (42, 22, 43, 32, 41),
     (51, 23, 33, 54, 12)),  # 11 -> 55 -> 12 -> 11 -> 55
    ((55, 14, 25, 52, 21),
     (44, 31, 11, 53, 43),
     (24, 13, 45, 12, 34),
     (42, 22, 43, 21, 41),
     (51, 23, 33, 54, 15)),  # 11 -> 55 -> 15 -> 21 -> 44 -> 21 -> 21 -> 44
))
def test_treasure_path_with_loops(treasure_map):
    with pytest.raises(RecursionError):
        _make_treasure_path(treasure_map)
    with pytest.raises(RecursionError):
        find_treasure(treasure_map)


@pytest.mark.parametrize('inp, expected_str', [
    ((1, 2, 3, 4), '1 2 3 4'),
    (('some text', 2, 3, 4), 'some text 2 3 4'),
    ([5, [2], 'a'], '5 [2] a'),
])
def test_list_to_str(inp, expected_str):
    assert _list_to_str(inp) == expected_str
