# Treasure Hunt

[![Build Status](https://travis-ci.org/ripiuk/treasure-hunt.svg?branch=master)](https://travis-ci.org/ripiuk/treasure-hunt)

**Task:**

There is a table with values. The values in the table are clues.
Each cell contains a number between 11 and 55, where the ten’s
digit represents the row number and the unit’s digit represents
the column number of the cell containing the next clue. Starting
with the upper left corner (at 1,1), use the clues to guide your
search through the table. The treasure is a cell whose value is
the same as its coordinates. The program must first read in the
treasure map data into a 5 by 5 array.

**Input example:**

    55 14 25 52 21
    44 31 11 53 43
    24 13 45 12 34
    42 22 43 32 41
    51 23 33 54 15

**Output example:**

    11 55 15 21 44 32 13 25 43


#### How to run

Install python, create virtual environment and install all the requirements:

    make setup

Run the program with selected implementation:

* Functional programming implementation:

        python run.py func
        # or
        python run.py
        # or
        make run

* OOP implementation:

        python run.py oop
        # or
        make run-oop


#### How to run tests

Run the tests:

    make test

Check the tests coverage:

    make test-cov