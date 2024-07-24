#!/usr/bin/env python3
""" LFU (Least Frequently Used) caching system """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Class that implements a LFU caching system"""

    def __init__(self):
        """Initialize class instances"""
        super().__init__()
        self.block = []
        self.frequency = {}

    def _evict_item(self):
        """Evict the least frequently used item, using LRU for ties"""
        LFU = min(self.frequency.values())
        lfu_keys = {k: self.block.index(k) for k, v in self.frequency.items()
                    if v == LFU}

        discard_key = min(lfu_keys, key=lfu_keys.get)

        print("DISCARD: {}".format(discard_key))
        del self.cache_data[discard_key]
        del self.frequency[discard_key]
        self.block.remove(discard_key)

    def put(self, key, item):
        """Assign data to the dictionary (cache)"""
        if not key or not item:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in \
                self.cache_data:
            self._evict_item()

        self.cache_data[key] = item
        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

        if key in self.block:
            self.block.remove(key)
        self.block.append(key)

    def get(self, key):
        """Retrieve an item by key from the dictionary (cache)"""
        if key is None or key not in self.cache_data:
            return None

        self.block.remove(key)
        self.block.append(key)
        self.frequency[key] += 1

        return self.cache_data[key]
