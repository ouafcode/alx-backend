#!/usr/bin/env python3
""" docs Class """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ class child """

    def put(self, key, item):
        """ put data """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ get data """
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data[key]
