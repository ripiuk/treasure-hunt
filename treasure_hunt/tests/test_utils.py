import pytest

from treasure_hunt.utils import list_to_str


@pytest.mark.parametrize('inp, expected_str', [
    ((1, 2, 3, 4), '1 2 3 4'),
    (('twilight zone', 1959), 'twilight zone 1959'),
    ([5, [2], 'a'], '5 [2] a'),
    (('nice', 'glasses'), 'nice glasses')
])
def test_list_to_str(inp, expected_str):
    assert list_to_str(inp) == expected_str


@pytest.mark.parametrize('inp', [
    [],
    43,
    2 + 3j,
    {'django': 'aiohttp?'},
    'its evening now, I need some more comfortable chair',
])
def test_list_to_str_bad_inp(inp):
    with pytest.raises(ValueError):
        list_to_str(inp)
