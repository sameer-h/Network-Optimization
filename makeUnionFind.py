from collections import defaultdict

# Sameer Hussain - CSCE 629 - Network Optimization

class Union:
    def __init__(self): #init
        self.rank = {}
        self.parent = {}
    
    def __iter__(self): #iterable
        return iter(self.parent)
    
    def __getitem__(self, key): #get
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
    
    def unionFind(self, *keys): #union command for kruskal's
        srcs = [self[i] for i in keys]
        maximum = max([(self.rank[s], s) for s in srcs])[1]
        for s in srcs:
            if s != maximum:
                self.rank[maximum] += self.rank[s]
                self.parent[s] = maximum



        
        
        
        


    