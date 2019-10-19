import re
import typing as typ


TREASURE_MAP_INP_PATH = 'treasure_hunt/treasure_map/treasure_map.txt'


class WrongInputDataError(Exception):
    """Input data validation exception"""


def _transform_raw_map(raw_inp: str, n: int = 5) -> typ.Tuple[typ.Tuple[int, ...], ...]:
    """
    Transform raw input map data from string to 2D tuple of ints

    :param raw_inp: raw map input
    :param n: number of columns/rows in the input map
    :return: 2D tuple of ints (n x n)
    :raise WrongInputDataError: if input data is not valid

    >>> _transform_raw_map('12 22\\n\\n21 21\\n.some\\ntrash\\nhere', n=2)
    ((12, 22), (21, 21))
    """
    flat_map = list(map(int, re.findall(r'\d+', raw_inp)))

    if not 1 <= n < 9:
        raise WrongInputDataError(
            f'Number of columns/rows in the input map '
            f'should be between 1 and 9')
    if not flat_map:
        raise WrongInputDataError(f'No digits found in the input: {raw_inp!r}')
    if len(flat_map) != n * n:
        raise WrongInputDataError(
            f'Treasure map cells number should be {n * n}, '
            f'got {len(flat_map)} instead')
    if not all(1 <= number // 10 <= n
               and 1 <= number % 10 <= n
               for number in flat_map):
        raise WrongInputDataError(
            f'Each cell should contains a number with ten’s '
            f'and unit’s between 1 and {n}')

    return tuple(tuple(flat_map[i:i + n]) for i in range(0, len(flat_map), n))


def get_treasure_map_from_file(
        file_path: str = TREASURE_MAP_INP_PATH,
        n: int = 5) -> typ.Tuple[typ.Tuple[int, ...], ...]:
    """
    Read input file with treasure map data into a n by n tuple

    :param file_path: path to the treasure map file
    :param n: number of columns/rows in the input map
    :return: 2D tuple of ints (n x n)
    """
    with open(file_path, 'r', encoding='utf-8') as treasure_map_f:
        raw_map = treasure_map_f.read()
        return _transform_raw_map(raw_map, n)
