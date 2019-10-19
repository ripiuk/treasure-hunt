"""
OOP implementation
"""

import reprlib
import itertools
import typing as typ

from treasure_hunt.utils import list_to_str


class SearchForTreasurePath:
    """
    Object-oriented implementation of treasure search
    """

    __slots__ = ('_treasure_map', '_curr_row', '_curr_col')

    def __init__(self, treasure_map: typ.Tuple[typ.Tuple[int, ...], ...],
                 curr_i: int = 1, curr_j: int = 1):
        """
        Create new :class:`SearchForTreasurePath`

        :param treasure_map: treasure map input
        """
        self.treasure_map = treasure_map
        self._curr_row = curr_i
        self._curr_col = curr_j

    @property
    def treasure_map(self):
        return self._treasure_map

    @treasure_map.setter
    def treasure_map(self, treasure_map: typ.Tuple[typ.Tuple[int, ...], ...]) -> None:
        """
        Set treasure map for the class

        :param treasure_map: treasure map input
        :return:
        :raise ValueError: if treasure map format is not valid
        """
        if not treasure_map:
            raise ValueError('Got empty value')
        if not isinstance(treasure_map, (list, tuple)):
            raise ValueError(f'Treasure map should be list or tuple instance, '
                             f'got {type(treasure_map)} instead')
        if not all(isinstance(row, (list, tuple))
                   and len(row) == len(treasure_map)
                   for row in treasure_map):
            raise ValueError(f'The treasure map should be 2D array '
                             f'{len(treasure_map)}x{len(treasure_map)}')

        self._treasure_map = treasure_map

    def _get_next_row_and_col_nums(self) -> typ.Tuple[int, int]:
        """
        Get next path cell containing the next clue

        :return: next row and next column address
        """
        return divmod(self.treasure_map[self._curr_row - 1][self._curr_col - 1], 10)

    def __call__(self) -> typ.List[int]:
        """
        Implementation of treasure search

        :return: treasure path
        :raise ValueError: if loops found in the treasure map input
        """
        res = list()
        max_loop_count = len(self._treasure_map) * len(self._treasure_map)
        for i in itertools.count():
            if i > max_loop_count:
                raise ValueError('Loop found in the treasure map input')
            res.append(self._curr_row * 10 + self._curr_col)
            next_row, next_col = self._get_next_row_and_col_nums()
            if (self._curr_row, self._curr_col) == (next_row, next_col):
                break
            self._curr_row, self._curr_col = next_row, next_col
        return res

    def __repr__(self):
        return '<SearchForTreasurePath {}>'.format(reprlib.repr(self.treasure_map))


def find_treasure(treasure_map: typ.Tuple[typ.Tuple[int, ...], ...]) -> str:
    """
    Find the treasure path

    :param treasure_map: treasure map input
    :return: treasure path
    """
    treasure_path = SearchForTreasurePath(treasure_map)()
    return list_to_str(treasure_path)
