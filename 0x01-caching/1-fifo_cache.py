#!/usr/bin/env python3
""" docs Class """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ class Fifo cache """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ put data """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                remove = next(iter(self.cache_data))
                self.cache_data.pop(remove)
                print("DISCARD: {}".format(remove))
            self.cache_data[key] = item

    def get(self, key):
        """ get data """
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data[key]
