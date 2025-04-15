#https://leetcode.com/problems/insert-delete-getrandom-o1/
import random
class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}  # Maps value to its index in the list
        self.values = []        # List of current elements

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        # Get the index of the value to remove
        idx_to_remove = self.val_to_index[val]
        last_val = self.values[-1]
        
        # Move the last element to the place of the element to remove
        self.values[idx_to_remove] = last_val
        self.val_to_index[last_val] = idx_to_remove
        
        # Remove the last element
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()