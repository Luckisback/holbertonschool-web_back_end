#!/usr/bin/env python3

""" A type-annotated function that returnsi
a tuple, after computing some values"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v**2)
