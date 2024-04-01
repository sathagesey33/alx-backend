#!/usr/bin/env python3
"""
Helper function for pagination
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start index and end index for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index
        for the given page and page size.
    """
    if page < 1 or page_size < 1:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


if __name__ == "__main__":
    # Example usage
    res = index_range(1, 7)
    print(type(res))  # <class 'tuple'>
    print(res)        # (0, 7)

    res = index_range(3, 15)
    print(type(res))  # <class 'tuple'>
    print(res)        # (30, 45)
