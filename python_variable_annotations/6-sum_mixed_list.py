#!/usr/bin/env python3

""" a type-annotated function that
returns the sum of several lists"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ calculates the sum of the list """
    return sum(mxd_lst)
