from random import random


class RandomizedSet:

    def __init__(self):
        self.numsMap = {}
        self.numsList = []
    def insert(self, val: int) -> bool:
        res =  val not in self.numsMap
        if res:
            self.numsMap[val] = len(self.numsList)
            self.numsList.append(val)
        return res
    def remove(self, val: int) -> bool:
        res = val in self.numsMap
        if res:
            index = self.numsMap[val]
            new_element = self.numsList.pop()
            if index < len(self.numsList):
                self.numsList[index] = new_element
                self.numsMap[new_element] = index
            del self.numsMap[val]
        return res
    def getRandom(self) -> int:
        random.choice(self.numsList)
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()