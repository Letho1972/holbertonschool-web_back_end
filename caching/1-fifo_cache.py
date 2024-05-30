#!/usr/bin/env python3

"""
1. FIFO caching
A class BasicCache that inherits from BaseCaching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ A class BasicCache that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the FIFOCache """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.queue.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
