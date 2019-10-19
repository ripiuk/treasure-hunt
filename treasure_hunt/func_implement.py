import typing as typ


def _make_treasure_path(treasure_map: typ.Tuple[typ.Tuple[int, ...], ...],
                        curr_i: int = 1, curr_j: int = 1) -> typ.List[int]:
    """
    Recursion functional implementation of treasure search

    :param treasure_map: treasure path
    :param curr_i: current row
    :param curr_j: current column
    :return: treasure path
    :raise RecursionError: if loops found in the input treasure map
    """
    res = [curr_i * 10 + curr_j]
    next_i, next_j = divmod(treasure_map[curr_i - 1][curr_j - 1], 10)
    if (curr_i, curr_j) == (next_i, next_j):
        return res
    return res + _make_treasure_path(treasure_map, curr_i=next_i, curr_j=next_j)


def _list_to_str(data: typ.Union[tuple, list]) -> str:
    """
    Convert list with some data to space separated string

    :param data: list with data
    :return: space separated string
    """
    return ' '.join(map(str, data))


def find_treasure(treasure_map: typ.Tuple[typ.Tuple[int, ...], ...]) -> str:
    """
    Find the treasure path

    :param treasure_map: treasure path
    :return: treasure path or error message
    :raise RecursionError: if loops found in the treasure map input
    """
    try:
        result = _make_treasure_path(treasure_map)
    except RecursionError as err:
        err.args = ('Loops found in the treasure map input',) + err.args[1:]
        raise
    else:
        return _list_to_str(result)
