import pytest

from treasure_hunt.utils import list_to_str
from treasure_hunt.func_implement import _make_treasure_path, find_treasure


def test_make_treasure_path(treasure_map_and_expected_path):
    treasure_map, expected_path = treasure_map_and_expected_path
    assert _make_treasure_path(treasure_map) == expected_path


def test_find_treasure_path(treasure_map_and_expected_path):
    treasure_map, expected_path = treasure_map_and_expected_path
    assert find_treasure(treasure_map) == list_to_str(expected_path)


def test_make_treasure_path_with_loops(treasure_map_with_loop):
    with pytest.raises(RecursionError):
        _make_treasure_path(treasure_map_with_loop)


def test_find_treasure_path_with_loops(treasure_map_with_loop):
    with pytest.raises(RecursionError):
        find_treasure(treasure_map_with_loop)
