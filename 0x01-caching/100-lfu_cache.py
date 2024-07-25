#!/usr/bin/env python3
""" docs Class """

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """ class LFU cache """
    def __init__(self):
        super().__init__()
        self.frq = {}

    def put(self, key, item):
        """ put data """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frq[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frq.values())
                leaset_key = [k for k, v in self.frq.items() if v == min_freq]
                lfu_key = min(leaset_key, key=self.frq.get)
                self.cache_data.pop(lfu_key)
                self.frq.pop(lfu_key)
                print("DISCARD: {}".format(lfu_key))
            self.cache_data[key] = item
            self.frq[key] = 1

    def get(self, key):
        """ get data """
        if key in self.cache_data:
            self.frq[key] += 1
            return self.cache_data.get(key)
