# Day12
#Design a data structure that supports all following operations in average O(1) time.

# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
from random import choice
class RandomizedSet():
    def __init__(self):
        self.dictionary = {}
        self.Array = []

        
    def insert(self, val: int) -> bool:
        if val in self.dictionary:
            return False
        self.dictionary[val] = len(self.Array)
        self.Array.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.dictionary:
            last_element, idx_of_value_to_be_delted = self.Array[-1], self.dictionary[val]
            self.Array[idx_of_value_to_be_delted], self.dictionary[last_element] = last_element, idx_of_value_to_be_delted
            self.Array.pop()
            del self.dictionary[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.Array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()