#!/usr/bin/python3

""" A type-annotated function that
returns the sum of a list's elements """


from typing import List


def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
