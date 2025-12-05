"""
class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def unique(self):
        return set(self.data[self.index:])
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return item
"""
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

    def __next__(self):
        while True:
            item = next(self.items)  
            
           
            if self.ignore_case and isinstance(item, str):
                key = item.lower()
            else:
                key = item
            
            
            if key not in self.seen:
                self.seen.add(key)
                return item
            

    def __iter__(self):
        return self




lazy_unique = Unique(['A','z', "a", 'A'], ignore_case=True)
lazy_unique1 = Unique(['A','z', "a", 'A'], ignore_case=False)
l=[]
l1=[]
for item in lazy_unique:
    l.append(item)
print(f"Get: {l}")
for item in lazy_unique1:
    l1.append(item)
print(f"Get: {l1}")
"""
l=Iterator(['A','z', "a", 'A'])
print(*l.unique(), sep=', ')
"""