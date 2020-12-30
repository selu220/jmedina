
"""Print a pyramid to the terminal

get get expected final width

A pyramid of height 3 would look like:

--=--
-===-
=====


my pseudo-code to decode pattern

---=--- f(row 1, height = 4 ) = 7 across, 7/2 = 3.5
--===-- f(row 2, height = 4 ) = 7 across, with 3 equal ( 2 * 3 = 6 - 1 = 5 , etc.
-=====-  +2 equals, -1 dashes given the dash_factor
=======



"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter


def print_pyramid(rows):
    """Print a pyramid of a given height

    :param int rows: total height
    """
    # set starting values which we'll increment / decrement according to pattern
    dash_factor = ((rows * 2) - 1) / 2
    dash_count = int(dash_factor)
    equal_count = 1

    for i in range(0, rows):
        d = dash_count * "-"
        e = equal_count * "="
        print(d + e + d)

        dash_count -= 1
        equal_count += 2


if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-r", "--rows", default=3, help="Number of rows")

    args = parser.parse_args()
    print_pyramid(args.rows)