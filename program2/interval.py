from goody import type_as_str
from math import sqrt

global condition
condition = True

class Interval:
    # Helper Methods
    def __init__(self, min=None, max=None):
        self.min = min 
        self.max = max
        global condidition 
        condition=False
    
    @staticmethod
    def min_max(min, max=None):
        if type(min)!=int and type(min)!=float or type(max)!=int and type(max)!=float and max !=None: raise AssertionError()
        if max==None: return Interval(min,min)
        if min > max and min!=None: raise AssertionError()
        else: return Interval(min,max)
    
    @staticmethod
    def mid_err(mid, diff=0):
        if type(mid)!=int and type(mid)!=float or type(diff)!=int and type(diff)!=float : raise AssertionError()
        if abs(diff)!=diff :raise AssertionError()
        max = mid + diff
        min = mid - diff
        return Interval(min,max)

    def __repr__(self):
        return "Interval("+ str(self.min) +','+ str(self.max)+")"
    
    def __str__(self):
        diff = (self.max-self.min)/2
        middle = self.min+((self.max-self.min)/2)
        return str(middle)+'(+/-'+ str(diff)+')'

    def best(self):
        return self.min+((self.max-self.min)/2)

    
    def error(self):
        return (self.max-self.min)/2

    def relative_error(self):
        return abs((((self.max-self.min)/2) / (self.min+((self.max-self.min)/2))) *100)
    
    
    def __bool__(self):
        #print(self.error(self))
        if (self.max-self.min)/2 ==0: return False
        else: return True

    def prefix(self):
        print('in')

    
    def __add__(a,b):
        if type(a)==str or type(b)==str: raise TypeError()
        if type(a)==int or type(a)==float : a = Interval(a,a) #this is where the error is
        if type(b)==int or type(b)==float : b = Interval(b,b)
        #print(a.__dict__, b.__dict__,a.min + b.min,a.max+b.max)
        return Interval(a.min + b.min,a.max+b.max)

    def __radd__(a,b):
        if type(a)==str or type(b)==str: raise TypeError()
        if type(a)==int or type(a)==float : a = Interval(a,a) #this is where the error is
        if type(b)==int or type(b)==float : b = Interval(b,b)
        return Interval(a.min + b.min,a.max+b.max)

    def __sub__(a,b):
        if type(a)==str or type(b)==str: raise TypeError()
        if type(a)==int or type(a)==float : a = Interval(a,a) #this is where the error is
        if type(b)==int or type(b)==float : b = Interval(b,b)
        return Interval(a.min - b.max,a.max-b.min)
    
    def __rsub__(a,b):
        if type(a)==str or type(b)==str: raise TypeError()
        if type(a)==int or type(a)==float : a = Interval(a,a) #this is where the error is
        if type(b)==int or type(b)==float : b = Interval(b,b)
        return Interval(b.min - a.max,b.max-a.min)
    
    def __mul__(a,b):
        if type(a)==str or type(b)==str: raise TypeError()
        if type(a)==int or type(a)==float : a = Interval(a,a) #this is where the error is
        if type(b)==int or type(b)==float : b = Interval(b,b)
        l = sorted([x*y for x in [a.min,a.max] for y in [b.min, b.max]])
        return Interval(l[0], l[-1])
    
    def __rmul__(a,b):
        if type(a)==str or type(b)==str: raise TypeError()
        if type(a)==int or type(a)==float : a = Interval(a,a) #this is where the error is
        if type(b)==int or type(b)==float : b = Interval(b,b)
        l = sorted([x*y for x in [a.min,a.max] for y in [b.min, b.max]])
        return Interval(l[0], l[-1])

    def __truediv__(a,b):
        if type(a)==str or type(b)==str: raise TypeError()
        if type(a)==int or type(a)==float : a = Interval(a,a) #this is where the error is
        if type(b)==int or type(b)==float : b = Interval(b,b)
        if b.min < 0 and b.max > 0: raise ZeroDivisionError()
        l = sorted([x/y for x in [a.min,a.max] for y in [b.min, b.max]])
        return Interval(l[0], l[-1])
    
    def __rtruediv__(a,b):
        if type(a)==str or type(b)==str: raise TypeError()
        if type(a)==int or type(a)==float : a = Interval(a,a) #this is where the error is
        if type(b)==int or type(b)==float : b = Interval(b,b)
        if a.min < 0 and a.max > 0: raise ZeroDivisionError()
        l = sorted([y/x for x in [a.min,a.max] for y in [b.min, b.max]])
        return Interval(l[0], l[-1])

    def __pow__(a,b):
        if type(a)==str or type(b)==str or  type(a)==float or type(b)==float or type(b)!=int: raise TypeError()
        if type(a)==int or type(a)==float : a = Interval(a,a) #this is where the error is
        if type(b)==int or type(b)==float : b = Interval(b,b)
        l = sorted([x**y for x in [a.min,a.max] for y in [b.min, b.max]])
        return Interval(l[0], l[-1])

    def __eq__(a,b):
        if type(a)==str or type(b)==str: raise TypeError()
        if type(a)==int or type(a)==float : a = Interval(a,a) #this is where the error is
        if type(b)==int or type(b)==float : b = Interval(b,b)
        
        if a.min!=b.min or a.max!=b.max: return False
        return True
    
    def __gt__(a,b):
        if 'compare_mode' not in Interval.__dict__.keys(): raise AssertionError()
        if Interval.__dict__['compare_mode'] not in ['liberal', 'conservative']: raise AssertionError()
        if type(a)==str or type(b)==str: raise TypeError()
        if type(a)==int or type(a)==float : a = Interval(a,a) #this is where the error is
        if type(b)==int or type(b)==float : b = Interval(b,b)
        
        if Interval.__dict__['compare_mode'] == 'conservative':
            if a.min > b.min and a.min > b.max and a.max>b.min and a.max>b.max: return True
        if Interval.__dict__['compare_mode'] == 'liberal':
            if a.min+((a.max-a.min)/2) > b.min+((b.max-b.min)/2): return True

        return False

    def __ge__(a,b):
        if 'compare_mode' not in Interval.__dict__.keys(): raise AssertionError()
        if Interval.__dict__['compare_mode'] not in ['liberal', 'conservative']: raise AssertionError()
        if type(a)==str or type(b)==str: raise TypeError()
        if type(a)==int or type(a)==float : a = Interval(a,a) #this is where the error is
        if type(b)==int or type(b)==float : b = Interval(b,b)
        
        if Interval.__dict__['compare_mode'] == 'conservative':
            if a.min >= b.min and a.min >= b.max and a.max>=b.min and a.max>=b.max: return True
        if Interval.__dict__['compare_mode'] == 'liberal': 
            if a.min+((a.max-a.min)/2) >= b.min+((b.max-b.min)/2): return True
        return False


    def __lt__(a,b):
        #print(Interval.__dict__.keys())
        if 'compare_mode' not in Interval.__dict__.keys(): raise AssertionError()
        if Interval.__dict__['compare_mode'] not in ['liberal', 'conservative']: raise AssertionError()
        if type(a)==str or type(b)==str: raise TypeError()
        if type(a)==int or type(a)==float : a = Interval(a,a) #this is where the error is
        if type(b)==int or type(b)==float : b = Interval(b,b)
        #print(a.__dict__,b.__dict__)
        if Interval.__dict__['compare_mode'] == 'conservative':
            if a.min < b.min and a.min < b.max and a.max<b.min and a.max<b.max: return True
        if Interval.__dict__['compare_mode'] == 'liberal': 
            if a.min+((a.max-a.min)/2) < b.min+((b.max-b.min)/2): return True
        return False

    def __le__(a,b):
        if 'compare_mode' not in Interval.__dict__.keys(): raise AssertionError()
        if Interval.__dict__['compare_mode'] not in ['liberal', 'conservative']: raise AssertionError()
        if type(a)==str or type(b)==str: raise TypeError()
        if type(a)==int or type(a)==float : a = Interval(a,a) #this is where the error is
        if type(b)==int or type(b)==float : b = Interval(b,b)
        
        if Interval.__dict__['compare_mode'] == 'conservative':
            if a.min <= b.min and a.min <= b.max and a.max<=b.min and a.max<=b.max: return True
        if Interval.__dict__['compare_mode'] == 'liberal':
            if a.min+((a.max-a.min)/2) <= b.min+((b.max-b.min)/2): return True 
        return False
    
    def __abs__(self):
        min = self.min
        if self.min < 0 and self.max> 1: min=0.0
        l= sorted([abs(min), abs(self.max)])
        return Interval(l[0],l[-1])

    def sqrt(self):
        if self.min <= 0 or self.max <= 0 : raise ValueError()
        return Interval(sqrt(self.min), sqrt(self.max))
    
    def __pos__(self):
        return str(self)
    
    def __neg__(self):
        return '-'+str(self)

    def _includes0(self):
        return self.min <= 0 <= self.max

    def __setattr__(self, name, value):
        if name not in ['min', 'max']: raise AssertionError()
        if name in self.__dict__ : raise AssertionError()
        self.__dict__[name]=value
        


   
    @staticmethod
    def _order2(a,b):
        return min(a,b),max(a,b)

    
    @staticmethod
    def _order4(a,b,c,d):
        return min(a,b,c,d),max(a,b,c,d)

     
    @staticmethod
    def _validate_arguments(l,r):
        return type(l) in [int,float,Interval] and type(r) in [int,float,Interval]
 



    
if __name__ == '__main__':
    
    g = Interval.mid_err(9.8,.05)
    print(repr(g))
    g = Interval.min_max(9.75,9.85)
    print(repr(g))
    d = Interval.mid_err(100,1)
    t = (d/(2*g)).sqrt()
    print(t,repr(t),t.relative_error())    
    
    import driver    
    driver.default_file_name = 'bscp22F21.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
