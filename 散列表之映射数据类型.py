class HashTable:
    def __init__(self, size):
        self.size = size  # size最好传入素数
        self.sloat = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key):
        return key % self.size

    def rehash(self, oldhash):
        return oldhash + 1

    def put(self, key, data):
        hashvalue = self.hashfunction(key)
        if self.sloat[hashvalue] == None:
            self.sloat[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.sloat[hashvalue] == key:
                self.data[hashvalue] == data  # replace
            else:
                nextsloat = self.rehash(hashvalue)
                while self.sloat[nextsloat] != None and self.sloat[nextsloat] != key:
                    nextsloat = self.rehash(nextsloat)

                if self.sloat[nextsloat] == None:
                    self.sloat[nextsloat] = key
                    self.data[nextsloat] = data
                else:
                    self.data[nextsloat] = data  # replace

    def get(self, key):
        startsloat = self.hashfunction(key)
        stop = False
        found = False
        data = None
        postition = startsloat
        while self.sloat[postition] != None and not found and not stop:
            if self.sloat[postition] == key:
                found = True
                data = self.data[postition]
            else:
                postition = self.rehash(postition)
                if postition == startsloat:  # 回到起点
                    stop = True
        return data

    def __getitem__(self, key):  # 实现通过map[key]的方式访问散列表
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)


h = HashTable(11)
h.put(11, 'hello')
h.put(86, 'wooo')
h.put(22, 'java')
h.put(24, 'Python')

print(h.get(22))
print(h[86])
h.put(22, 'c')
print(h[22])

'''
最好情况下，时间复杂度为O(1)，但因为散列冲突存在，需要加上查找过程。
评估散列冲突最大因素是负载因子的大小

'''
