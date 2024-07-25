#!/usr/bin/env python3
""" docs Class """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ class child """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ put data """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get data """
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data[key]
