
import numpy

class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0


    def add(self, name):
        self.names.append(name)


    def __iter__(self):
        return self


    def __next__(self):
        if self.current_num < len(self.names):
            res = self.names[self.current_num]
            self.current_num += 1
            return res
        else:
            raise StopIteration

Classmate = Classmate()
Classmate.add("张三")
Classmate.add("李四")
Classmate.add("王五")

for name in Classmate:
    print(name)


def triangles():
    L = [1]
    while 1:
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]

triangles()
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 15:
        break