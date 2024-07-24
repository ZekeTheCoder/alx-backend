#!/usr/bin/env python3
""" MRU(Most Recently Used) caching system """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Class that implements a MRU caching system"""

    def __init__(self):
        """Function to initialise class instances"""

        super().__init__()
        self.head = ""
        self.tail = ""

        self.prev = {}
        self.next = {}

        self.link_nodes(self.head, self.tail)

    def link_nodes(self, head, tail):
        """
        Function that create or update the connections between
        nodes (cache items) in the doubly linked list."""

        self.next[head] = tail
        self.prev[tail] = head

    def pop(self, key):
        """Function to pop(remove) data out of dictionary(cache)"""

        self.link_nodes(self.prev[key], self.next[key])
        del self.prev[key]
        del self.next[key]
        del self.cache_data[key]

    def push(self, key, item):
        """Function to push (add) data onto dictionary(cache)"""

        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.prev[self.tail]))
            # removes the most recently used item (the one before the tail).
            self.pop(self.prev[self.tail])

        self.cache_data[key] = item
        self.link_nodes(self.prev[self.tail], key)
        self.link_nodes(key, self.tail)

    def put(self, key, item):
        """Function that assigns item to dictionary(cache)"""

        if key and item:
            if key in self.cache_data:
                self.pop(key)
            self.push(key, item)

    def get(self, key):
        """Function that Get an item by key from dictionary(cache)"""

        if key is None or self.cache_data.get(key) is None:
            return None

        if key in self.cache_data:
            cached_value = self.cache_data[key]
            self.pop(key)
            self.push(key, cached_value)
            return cached_value
