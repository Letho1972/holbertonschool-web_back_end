#!/usr/bin/env python3
""" BaseCaching module
"""


class BaseCaching:

    def __init__(self):
        """A documentation is not a simple word, it’s a real sentence explaining
        what’s the purpose of the module,
        class or method (the length of it will be verified)"""
        self.cache_data = {}


class BasicCache(BaseCaching):
    def put(self, key, item):
        """Assign the value item to the key key in self.cache_data."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data associated with key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

    def print_cache(self):
        """Afficher le contenu du cache."""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print(f"{key}: {self.cache_data[key]}")
