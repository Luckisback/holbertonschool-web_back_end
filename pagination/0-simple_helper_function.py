#!/usr/bin/env python3

"""Simple helper function"""


def index_range(page, page_size):
    """
    Calculate start and end indexes for pagination.

    Parameters:
    - page (int): Page number (1-indexed).
    - page_size (int): Number of items per page.

    Returns:
    Tuple[int, int]: Start and end indexes for the given page and page size.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Both page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index
