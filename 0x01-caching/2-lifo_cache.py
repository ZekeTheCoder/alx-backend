#!/usr/bin/env python3
""" LIFO caching system """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Class that implements a LIFO caching system """

    def __init__(self):
        """Function that initialize class instances"""

        super().__init__()
        # keep track of the most recently added item’s key.
        self.last_item = ""

    def put(self, key, item):
        """Function that prints the key of the item being discarded and
         removes the most recently added item in the dictionary(cache). """

        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last_item))
                self.cache_data.pop(self.last_item)
            self.last_item = key

    def get(self, key):
        """Function that Get an item by key from dictionary(cache)"""

        if key is None or self.cache_data.get(key) is None:
            return None

        if key in self.cache_data:
            return self.cache_data[key]
