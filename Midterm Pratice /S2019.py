def consolidate(lsts):
    d = {}
    for lst in lsts:
        for val in lst:
            if val in d:
                d[val] += 1
            else:
                d[val] = 1
    return d

class ArrayList:

    def __init__(self):
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def insert_all(self, idx, other):
        newa = [None] * (len(self.data) + len(other))
        for i in range(0, idx):
            newa[i] = self.data[i]
        for i in range(idx, len(other)+idx):
            newa[i] = other[i-idx]
        for i in range(len(other)+idx, len(newa)):
            newa[i] = self.data[i-len(other)]
        self.data = newa

    def __repr__(self):
        return self.data.__repr__()