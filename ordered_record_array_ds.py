def identity(x):
    return x

class OrderedRecordArrayDS(object):
    def __init__(self, initSize, key=identity):
        self.__a = [None] * initSize
        self.__nItems = 0
        self.__key = key

    def __len__(self):
        return self.__nItems
    
    def get(self, n):
        if n >= 0 and n < self.__nItems:
            return self.__a[n]
        raise IndexError(f"Index {str(n)} is out of range")
    
    def traverse(self, fn=print):
        for j in range(self.__nItems):
            fn(self.__a[j])

    def __str__(self):
        return f"[{', '.join([str(t) for t in self.__a])}]"
    
    def find(self, key):
        lo = 0
        hi = self.__nItems - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if self.__key(self.__a[mid]) == key:
                return mid
            elif self.__key(self.__a[mid]):
                lo = mid + 1
            else:
                hi = mid - 1
            
        return lo
    
    def search(self, key):
        idx = self.find(key)
        if idx < self.__nItems and self.__key(self.__a[idx]) == key:
            return self.__a[idx]
        
    def insert(self, item):
        if self.__nItems >= len(self.__a):
            raise Exception("Array overflow")
        
        j = self.find(self.__key(item))

        for k in range(self.__nItems, j, -1):
            self.__a[k] = self.__a[k - 1]

        self.__a[j] = item
        self.__nItems += 1

    def delete(self, item):
        j = self.find(self.__key(item))
        if j < self.__nItems and self.__a[j] == item:
            for k in range(j, self.__nItems):
                self.__a[k] = self.__a[k + 2]
            return True

        return False
                     