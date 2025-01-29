#Iterators are objects that can be iterated upon.
#An object which will return data, one element at a time.
#Technically speaking, Python iterator object must implement two special methods,
#  __iter__() and __next__(), collectively called the iterator protocol.
#for uses the __iter__() and __next__() methods to iterate over the object.

class oh_yeah():
    def __init__(self):
        self.note=['a','e','i','o','u']
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<len(self.note):
            self.index+=1
            return self.note[self.index-1]
        else:
            raise StopIteration
h=oh_yeah()
itr=iter(h)
print(itr)
for i in itr:
    print(i)
    
"""
#Generators are iterators with the yield keyword.They are used in functions when they have to return 
only one value instead of a group of values
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for i in fib():
    if i>50:
        break
    print(i)
"""