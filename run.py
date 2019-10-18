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

from treasure_hunt.treasure_map import get_treasure_map_from_file


if __name__ == '__main__':
    treasure_map = get_treasure_map_from_file()
    print(treasure_map)
