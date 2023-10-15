class ArrayDS(object):
    def __init__(self, initSize):
        self.__a = [None] * initSize
        self.__nItems = 0

    def insert(self, item):
        self.__a[self.__nItems] = item
        self.__nItems += 1

    def search(self, item):
        for j in range(self.__nItems):
            if (r := self.__a[j]) == item:
                return r
            
    def delete(self, item):
        for j in range(self.__nItems):
            if (r := self.__a[j]) == item:
                for k in range(j, self.__nItems):
                    self.__a[k] = self.__a[k + 1]
                self.__nItems -= 1
                return True
            
        return False
    
    def traverse(self, fn=print):
        for j in range(self.__nItems):
            fn(self.__a[j])
