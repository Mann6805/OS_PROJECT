class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.ma = {}

    def refer(self, key, value):
        if key not in self.ma.keys():
            if len(self.cache) == self.capacity:
                # Evict least recently used element
                last = self.cache[-1]
                del self.ma[last]
                self.cache.pop()

        else:
            # Remove the existing key from cache
            self.cache.remove(key)

        # Update reference
        self.cache.insert(0, key)
        self.ma[key] = value

    def get(self, key):
        if key not in self.ma:
            return -1
        else:
            # Move the accessed key to the front to mark it as most recently used
            self.cache.remove(key)
            self.cache.insert(0, key)
            return self.ma[key]

    def display(self):
        # Display cache content
        print(self.cache)

# Example usage:
cache = LRUCache(2)  # Capacity is 2

cache.refer(1, 1)
cache.refer(2, 2)
print(cache.get(1))  # Output: 1

cache.refer(3, 3)  # 2 is the least recently used key, so it will be evicted
print(cache.get(2))  # Output: -1 (not found)

cache.refer(4, 4)  # 1 is the least recently used key, so it will be evicted
print(cache.get(1))  # Output: -1 (not found)
print(cache.get(3))  # Output: 3
print(cache.get(4))  # Output: 4
