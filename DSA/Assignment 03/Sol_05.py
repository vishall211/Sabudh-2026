# Problem 5: LRU Cache

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):

        # Return -1 if key does not exist
        if key not in self.cache:
            return -1

        # Move recently used key to the end
        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key, value):

        # Update existing key
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        # Remove the least recently used item
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


lru = LRUCache(2)

lru.put(1, 1)
lru.put(2, 2)

print(lru.get(1))

lru.put(3, 3)

print(lru.get(2))

lru.put(4, 4)

print(lru.get(1))
print(lru.get(3))
print(lru.get(4))