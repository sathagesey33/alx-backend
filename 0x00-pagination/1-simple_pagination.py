#!/usr/bin/env python3
"""
Helper function for pagination and Server class for baby names dataset.
"""

import csv
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a specific page of the dataset based on pagination parameters.

        Args:
            page (int): The page number to retrieve (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows representing the requested page
            from the dataset.
        """
        assert isinstance(page, int)
        assert (
            isinstance(page, int) and
            page > 0
        ), "page must be a positive integer"

        assert (
                isinstance(page_size, int) and
                page_size > 0
            ), "page_size must be a positive integer"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]


if __name__ == "__main__":
    # Example usage
    server = Server()

    try:
        should_err = server.get_page(-10, 2)
    except AssertionError:
        print("AssertionError raised with negative values")

    try:
        should_err = server.get_page(0, 0)
    except AssertionError:
        print("AssertionError raised with 0")

    try:
        should_err = server.get_page(2, 'Bob')
    except AssertionError:
        print("AssertionError raised when page and/or page_size are not ints")

    print(server.get_page(1, 3))
    print(server.get_page(3, 2))
    print(server.get_page(3000, 100))
