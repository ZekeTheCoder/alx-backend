#!/usr/bin/env python3
""" LRU(Least Recently Used) caching system """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Class defining methods th@ assign to dict & return data from it"""

    def __init__(self):
        """Function to initialise class intances"""

        super().__init__()
        # dummy head and tail nodes of the doubly linked list.
        self.head = ""
        self.tail = ""

        # To maintain the previous and next pointers of each node (cache item)
        self.prev = {}
        self.next = {}

        # Initializes the dummy head and tail in the doubly linked list.
        self.link_nodes(self.head, self.tail)

    def link_nodes(self, head, tail):
        """
        Function that create or update the connections between
        nodes (cache items) in the doubly linked list."""

        self.next[head] = tail
        self.prev[tail] = head

    def pop(self, key):
        """Function to pop(remove) items out of dictionary(cache)"""

        self.link_nodes(self.prev[key], self.next[key])
        # Remove the key from the self.prev and self.next dictionaries.
        del self.prev[key]
        del self.next[key]
        # Removes the item from the cache data dictionary.
        del self.cache_data[key]

    def push(self, key, item):
        """Function to push(add) items in the dictionary(cache)"""

        # Adds the item to the cache data dictionary.
        self.cache_data[key] = item
        # Links the new node to the current last node (before self.tail).
        self.link_nodes(self.prev[self.tail], key)
        # Links the new node (with key) to the self.tail.
        self.link_nodes(key, self.tail)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # print the key of the discarded item and remove it.
            print("DISCARD: {}".format(self.next[self.head]))
            self.pop(self.next[self.head])

    def put(self, key, item):
        """Function that assigns item to dictionary(cache)"""

        if key and item:
            if key in self.cache_data:
                self.pop(key)  # remove key first (to update its position).
            self.push(key, item)  # Adds the new item to the cache.

    def get(self, key):
        """Function that Get an item by key from dictionary(cache)"""

        if key is None or self.cache_data.get(key) is None:
            return None

        if key in self.cache_data:
            cached_value = self.cache_data[key]
            # Removes the key from its current position in the cache
            self.pop(key)
            # Adds the key back to the cache as the most recently used item.
            self.push(key, cached_value)
            return cached_value  # the value associated with the key.
