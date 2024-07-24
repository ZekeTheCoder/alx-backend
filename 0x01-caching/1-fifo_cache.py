#!/usr/bin/python3
""" FIFO caching system """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Class that implements a FIFO caching system """

    def __init__(self):
        """Function that initialize class instances"""

        super().__init__()
        self.data = {}  # dictionary to track the order of items.
        # to track the sequence of added and removed items.
        self.push_in = 0
        self.pop_out = 0

    def push(self, key, item):
        """Function that push data into the dictionary(cache)"""

        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            # prints key of the item being discarded remove the oldest item
            print("DISCARD: {}".format(self.data[self.pop_out + 1]))
            self.pop()

        # Adds the new item to self.cache_data.
        self.cache_data[key] = item
        self.push_in += 1
        self.data[self.push_in] = key

    def pop(self):
        """Function that pop data out of dictionary(cache) using the key"""

        self.pop_out += 1
        key = self.data[self.pop_out]

        del self.data[self.pop_out]
        del self.cache_data[key]

    def put(self, key, item):
        """Function that Adds or Updates an item in the dictionary(cache)"""

        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                self.push(key, item)

    def get(self, key):
        """Function that Get an item by key from dictionary(cache)"""

        if key is None or self.cache_data.get(key) is None:
            return None

        if key in self.cache_data:
            return self.cache_data[key]
