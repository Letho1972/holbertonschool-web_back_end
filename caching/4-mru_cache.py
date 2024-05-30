#!/usr/bin/env python3


"""Create a class MRUCache that inherits
from BaseCaching and is a caching system"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ A class MRUCache that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the MRUCache """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value """
        if key is None or item is None:
            return

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop(0)
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key is None or key not in self.cache_data:
            return None

        """ Update the order to reflect recent use """

        self.stack.remove(key)
        self.stack.append(key)

        return self.cache_data[key]
