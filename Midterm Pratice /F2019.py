class ArrayList:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def move(self, idx_src, idx_dst):
        first = self.data[idx_src]
        if idx_src < idx_dst:
            for i in range(idx_src, idx_dst):
                data[i] = data[i+1]
        else:
            for i in range(idx_src, idx_dst, -1):
                data[i] = self.data[i-1]
        self.data[idx_dst] = first

"""
3, 2, 4, 6, 0, 7, 5, 1
0, 2, 4, 6, 3, 7, 5, 1



"""