#!/usr/bin/env python3
""" Simple helper function for pagination. """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Calculate the start and end index for pagination. """
    if page and page_size:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index
