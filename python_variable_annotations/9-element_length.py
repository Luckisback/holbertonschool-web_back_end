#!/usr/bin/env python3

""" Bringing annotations on an existing function  """

from typing import Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> Tuple[Sequence, int]:
    """ Return some values with the appropriate types """
    return [(i, len(i)) for i in lst]
