#!/usr/bin/env python3


""" 0. Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):

    """ A class BasicCache that inherits from BaseCaching"""

    def put(self, key, item):
        """Assign the value item to the key key in self.cache_data."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data associated with key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
