#!/usr/bin/env python3
""" Simple helper function """
from typing import Tuple


def function index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ indexing range """
    startPage = (page - 1) * page_size
    endPage = page * page_size
    return (startPage, endPage)
