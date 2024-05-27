#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching:
    def __init__(self):
        self.cache_data = {}

class BasicCache(BaseCaching):
    def put(self, key, item):
        """Assigner la valeur item à la clé key dans self.cache_data."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retourner la valeur dans self.cache_data associée à key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
    
    def print_cache(self):
        """Afficher le contenu du cache."""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print(f"{key}: {self.cache_data[key]}")