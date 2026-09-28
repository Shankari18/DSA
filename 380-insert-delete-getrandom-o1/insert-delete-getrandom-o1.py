class RandomizedSet:

    def __init__(self):
        self.values = []
        self.map = {}
    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.values)
        self.values.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        index = self.map[val]
        last = self.values[-1]
        self.values[index] = last
        self.map[last] = index
        self.values.pop()
        del self.map[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.values)