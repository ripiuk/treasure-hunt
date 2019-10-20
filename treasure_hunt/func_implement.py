"""
Implementation using functional programming approach
"""

import typing as typ

from treasure_hunt.utils import list_to_str


def _make_treasure_path(treasure_map: typ.Tuple[typ.Tuple[int, ...], ...],
                        curr_row: int = 1, curr_col: int = 1) -> typ.List[int]:
    """
    Recursion functional implementation of treasure search

    :param treasure_map: treasure map input
    :param curr_row: current row
    :param curr_col: current column
    :return: treasure path
    :raise RecursionError: if loops found in the input treasure map
    """
    # TODO: replace RecursionError with counter
    res = [curr_row * 10 + curr_col]
    next_row, next_col = divmod(treasure_map[curr_row - 1][curr_col - 1], 10)
    if (curr_row, curr_col) == (next_row, next_col):
        return res
    return res + _make_treasure_path(treasure_map, curr_row=next_row, curr_col=next_col)


def find_treasure(treasure_map: typ.Tuple[typ.Tuple[int, ...], ...]) -> str:
    """
    Find the treasure path

    :param treasure_map: treasure map input
    :return: treasure path
    :raise RecursionError: if loops found in the treasure map input
    """
    try:
        result = _make_treasure_path(treasure_map)
    except RecursionError as err:
        err.args = ('Loops found in the treasure map input',) + err.args[1:]
        raise
    else:
        return list_to_str(result)
