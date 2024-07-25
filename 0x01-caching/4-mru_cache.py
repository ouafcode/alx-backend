#!/usr/bin/env python3
""" docs Class """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ class LRU cache """
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ put data """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                remove = self.order.pop()
                self.cache_data.pop(remove)
                print("DISCARD: {}".format(remove))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ get data """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)
