#!/usr/bin/env python3
"""
Pagination methods for a server class.
"""

import csv
import math
from typing import List, Dict, Union, Optional


def index_range(page: int, page_size: int) -> tuple[int, int]:
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
        assert (
            isinstance(page, int) and
            page > 0
        ), "Page must be a positive integer."

        assert (
            isinstance(page_size, int) and
            page_size > 0
        ), "Page size must be a positive integer."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]

    def get_hyper(
        self,
        page: int = 1,
        page_size: int = 10
     )    -> Dict[str, Union[int, List[List], Optional[int]]]:
        """
        Return hypermedia information for pagination.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Union[int, List[List], Optional[int]]]:
            A dictionary containing hypermedia information.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }


if __name__ == "__main__":
    # Example usage
    server = Server()
    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))
