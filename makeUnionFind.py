from collections import defaultdict

class Union:
    def __init__(self):
        self.rank = {}
        self.parent = {}
    
    def __iter__(self):
        return iter(self.parent)
    
    def __getitem__(self, key):
        if key not in self.parent:
            self.parent[key] = key
            self.rank[key] = 1
            return key
        

        pwd = [key]
        src = self.parent[key]

        while pwd[-1] != src:
            pwd.append(src)
            src = self.parent[src]
        
        for i in pwd:
            self.parent[i] = src
        
        return src
    
    def unionFind(self, *keys):
        srcs = [self[i] for i in keys]
        for s in srcs:
            x = max(self.rank[s], s)
            # print(x)
        for s in srcs:
            if s != x:
                self.rank[x] += self.rank[s]
                self.parent[s] = x
        
        
        
        


    