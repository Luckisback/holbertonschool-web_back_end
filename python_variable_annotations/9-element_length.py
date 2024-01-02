#!/usr/bin/python3

""" Bringing annotations on an existing function  """

from typing import Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> Tuple[Sequence, int]:
    return [(i, len(i)) for i in lst]
