from collections import defaultdict
from goody import type_as_str

# Iterators are covered in Week #4
# Implement all methods but iterators after Week #3

class Bag:
    def __init__(self, l=None):
        if l!=None: self.__dict__ = {k:l.count(k) for k in l}

    def __repr__(self):
        items = [k for k in (self.__dict__.keys()) for i in range(self.__dict__[k])]
        if len(items)==0: items =''
        return 'Bag(' + str(items) + ')'
    
    def __str__(self):
        items = ''.join(str(k) + "[" + str(v) + "], " for k,v in self.__dict__.items())
        return 'Bag('+items[:-1]+')'

    def __len__(self):
        return sum([v for v in self.__dict__.values()])

    def unique(self):
        return len(self.__dict__.keys())

    def __contains__(self,item):
        if item in self.__dict__.keys(): return True
        else: return False
    
    def count(self, item):
        if item not in self.__dict__.keys(): return 0
        else: return self.__dict__[item]

    def add(self,item):
        if item in self.__dict__.keys(): self.__dict__[item] = int(self.__dict__[item])+1
        else: self.__dict__[item]=1

    def __add__(b1, b2):
        if type(b2)==str: raise TypeError()
        keys = [x for i in [b1.__dict__.keys(), b2.__dict__.keys()] for x in i]
        tups1 = [(k,v) for k,v in b1.__dict__.items()]
        tups2 = [(k,v) for k,v in b2.__dict__.items()]
        tups = tups1 + tups2
        add_dict = {k: sum([i[1] for i in tups if k==i[0]]) for k in keys}
        return Bag([k for k,v in add_dict.items() for i in range(v)])

    

    def remove(self, item):
        if item not in self.__dict__.keys(): raise ValueError()
        self.__dict__[item] = self.__dict__[item]-1
        if self.__dict__[item] < 1: del self.__dict__[item]
    
    def __eq__(self, bag):
        
        if type(bag)==int :return False
        if self.__dict__.keys() != bag.__dict__.keys():return False
        condition = True 
        for k in self.__dict__.keys():
            if self.__dict__[k]!=bag.__dict__[k]: return False
        return True

    def __iter__(self):
        for k,v in self.__dict__.items():
            for x in range(v):
                yield k
                







if __name__ == '__main__':
    #Put your own test code here to test Bag before doing bsc tests
    #test = Bag(['a','a','a'])

    print('Start simple testing')

    import driver
    driver.default_file_name = 'bscp21F21.txt'
#     driver.default_show_exception =True
#     driver.default_show_exception_message =True
#     driver.default_show_traceback =True
    driver.driver()
