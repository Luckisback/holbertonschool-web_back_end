#!/usr/bin/env python3

""" A type-annotated function that
returns the sum of a list's elements """


from typing import List


def sum_list(input_list: List[float]) -> float:
    """ calculates the sum of the list """
    return sum(input_list)
