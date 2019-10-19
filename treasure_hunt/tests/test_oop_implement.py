import pytest

from treasure_hunt.utils import list_to_str
from treasure_hunt.oop_implement import SearchForTreasurePath, find_treasure


def test_search_for_treasure_path(treasure_map_and_expected_path):
    treasure_map, expected_path = treasure_map_and_expected_path
    assert SearchForTreasurePath(treasure_map)() == expected_path


def test_find_treasure_path(treasure_map_and_expected_path):
    treasure_map, expected_path = treasure_map_and_expected_path
    assert find_treasure(treasure_map) == list_to_str(expected_path)


def test_search_for_treasure_path_with_loops(treasure_map_with_loop):
    with pytest.raises(ValueError):
        SearchForTreasurePath(treasure_map_with_loop)()


def test_find_treasure_path_with_loops(treasure_map_with_loop):
    with pytest.raises(ValueError):
        find_treasure(treasure_map_with_loop)


def test_empty_treasure_path():
    with pytest.raises(ValueError):
        SearchForTreasurePath([])


def test_wrong_treasure_path_type():
    with pytest.raises(ValueError):
        SearchForTreasurePath('some text here')


def test_wrong_treasure_path_size():
    with pytest.raises(ValueError):
        SearchForTreasurePath(((11, 13, 33), (12, 21, 13)))
