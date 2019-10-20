"""
Task:
There is a table with values. The values in the table are clues.
Each cell contains a number between 11 and 55, where the ten’s
digit represents the row number and the unit’s digit represents
the column number of the cell containing the next clue. Starting
with the upper left corner (at 1,1), use the clues to guide your
search through the table. The treasure is a cell whose value is
the same as its coordinates. The program must first read in the
treasure map data into a 5 by 5 array.

Input example:
55 14 25 52 21
44 31 11 53 43
24 13 45 12 34
42 22 43 32 41
51 23 33 54 15

Output example:
11 55 15 21 44 32 13 25 43
"""

import argparse

from treasure_hunt import func_implement, oop_implement
from treasure_hunt.treasure_map import get_treasure_map_from_file


TREASURE_PATH_SEARCH_IMPLEMENTATIONS = {
    'func': func_implement.find_treasure,
    'oop': oop_implement.find_treasure,
}


def main():
    """
    Entry point. Requires some input CLI arguments to run the project
    It will run :func:`treasure_hunt.func_implement.find_treasure` or
    :func:`treasure_hunt.oop_implement.find_treasure` if everything is ok

    :return:
    """
    parser = argparse.ArgumentParser(description="Treasure Hunt", allow_abbrev=False)
    parser.add_argument(
        'implement',
        choices=TREASURE_PATH_SEARCH_IMPLEMENTATIONS,
        help='choose the implementation',
        default='func',
        const='func',
        nargs='?')
    args = parser.parse_args()

    treasure_map = get_treasure_map_from_file()
    print('Implementation:', args.implement)
    print('Input:', treasure_map)

    find_treasure = TREASURE_PATH_SEARCH_IMPLEMENTATIONS[args.implement]
    print('Output:', find_treasure(treasure_map))


if __name__ == '__main__':
    main()
