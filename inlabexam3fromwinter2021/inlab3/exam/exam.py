from ile3helper import ints, primes, is_prime, hide, nth, nth_for_m, Memoize
from collections import defaultdict
from goody import irange


def tail(*iterables):
    
    iterables = [iter(x) for x in iterables]
    _list = []
    while iterables:
        l = iterables[0]
        x = next(l,'stop')
        if x!='stop':
            iterables.remove(l)
            iterables.append(l)
            if type(x)!=int :_list.append(x)
        if x == 'stop':
            iterables.remove(l)
    s = sorted(list(set(_list)))
    for i in s: 
        print('in ')
        if _list.count(i)==1: yield i
    print('end')
    
        


def iter_set(n,s):
    #print(s)
    if s==[]: return 0
    if s[0] == n:
        return s[0]
    else: return  s[0] + iter_set(n-s[0],s[1:]) 
    
     
def NWSD(n : int, s : {int}) -> int:
    _sum = 0
    for num in sorted(list(s), reverse=True):
        _sum += num + iter_set(n-num,sorted(list(s), reverse=True)[1:])
    return _sum
    #print(_sum)


    ''''
    #print(s, n)
    l = sorted(list(s))
    print(l)
    
    if l == []: return None
    num = l[0]
    #for num in sorted(list(s), reverse= True):
    if num == n:
        if len(l) > 1: 
            #print('greater', set(l[1:]))
            print(num)
            return num
            #return num + NWSD(n-num, set(l[1:])) 
        
    #print('stop')
    
    else: 
        print('else')
        if n-num > 0:
                #print('head', num)
                #return sum([num] + [NWSD(n-num, s)])
            #return(str(num) + '+'+  str(NWSD(n-num, set(l[1:]))))
            #break
            return num + NWSD(n-num, set(l[1:])) 
    '''

    


    
class history_dict(dict):
    def __init__(self,n):
        pass
    
    # Prewritten: ensure your attributes in __init__ are _counts and _history
    def see_count(self):
        return self._counts
            
    def see_history(self):
        return self._history
        
    # Not required, but I found this method useful for debugging      
    def __str__(self):
        pass
         
         
    def __setitem__(self,key,value):
        pass


    def __getitem__(self,key):
        pass


    def iter_frequency(self):
        pass



  

if __name__ == '__main__':

    print('\n\nTesting tail')
    print("for tail('abc', 'abcdef', 'ab')... should produce d e f")
    for i in tail('abc', 'abcdef', 'ab'):
        print(' ',i)
        
    print("\nfor tail(hide('abc'), hide('abcdef'), hide([1,2]))... should produce d e f")
    for i in tail(hide('abc'), hide('abcdef'), hide([1,2])):
        print(' ',i)
    '''   
    print("\nfor nth_for_m(tail(hide('abcdef'),ints(),hide('abc')),1,10)... should produce 7 through 16")
    for i in nth_for_m(tail(hide('abcdef'),ints(),hide('abc')),1,10):
        print(' ',i)
        
    print("\nfor nth_for_m(tail(hide('abcdef'),ints(),hide('abc')),100,10)... should produce 106 through 115")
    for i in nth_for_m(tail(hide('abcdef'),ints(),hide('abc')),100,10):
        print(' ',i)
        
    print("\nfor nth_for_m(tail(hide('abcdef'),ints(),hide('abc')),100,10)... should produce [106 through 115]")
    print(' ',list(nth_for_m(tail(hide('abcdef'),ints(),hide('abc')),100,10)))
    '''
    

    print('\n\nTesting NWSD. Feel free to test other cases: e.g, base cases you choose')
    print('  NWSD(7,{2,3,5})  =',NWSD(7,{2,3,5}),  '...should be 2')
    print('  NWSD(12,{2,3,4}) =',NWSD(12,{2,3,4}), '...should be 7')
    print('See the correct results below these 10 calculations')
    for i in irange (1,10):
        s = set(x for x in irange(1,i))
        print(f'  NWSD({i},{s}) =',NWSD(i,s))
    print("""The results (with set arguments elided) should be
  NWSD(1,{1})    = 1
  NWSD(2, {...}) =  2
  NWSD(3, {...}) =  3
  NWSD(4, {...}) =  5
  NWSD(5, {...}) =  7
  NWSD(6, {...}) = 11
  NWSD(7, {...}) = 15
  NWSD(8, {...}) = 22
  NWSD(9, {...}) = 30
  NWSD(10,{...}) = 42""")
    
    print('\n\nTesting history_dict. Feel free to test other cases')
    print('Setup d = history_dict(2), with 4 values for a, 3 for b, 2 for c, 1 for d')
    d = history_dict(2)
    d['a'] = 'a1'
    d['a'] = 'a2'
    d['a'] = 'a3'
    d['a'] = 'a4'
    d['b'] = 'b1'
    d['b'] = 'b2'
    d['b'] = 'b3'
    d['c'] = 'c1'
    d['c'] = 'c2'
    d['d'] = 'd1'
    
    print('\nShowing _count and _history attributes')
    print('  d.see_count   =',d.see_count(),"\n                    ...should be             {'a': 4, 'b': 3, 'c': 2, 'd': 1}")
    print('  d.see_history =',d.see_history(), " \n                    ...should be              {'a': ['a1', 'a3'], 'b': ['b1', 'b2'], 'c': ['c1']}")

    print('\nTesting current associations')
    print('  Current/last a =',d['a'],'...should be a4')
    print('  Current/last b =',d['b'],'...should be b3')
    print('  Current/last c =',d['c'],'...should be c2')
    print('  Current/last d =',d['d'],'...should be d1')
    try:
        d['x']
        print("  ERROR: d['x'] should have raised exception")
    except KeyError:
        print("  d['x'] correctly raised exception")

    print('\nTesting 1st previous (-1) associations')
    print('  1st Previous a =',d['a',-1],'...should be a3')
    print('  1st Previous b =',d['b',-1],'...should be b2')
    print('  1st Previous c =',d['c',-1],'...should be c1')
    try:
        d['d',-1]
        print('  ERROR: 1st Previous d should have raised exception')
    except KeyError:
        print('  1st Previous d correctly raised exception')
    try:
        d['x',-1]
        print("  ERROR: d['x',-1] should have raised exception")
    except KeyError:
        print("  d['x',-1] correctly raised exception")
        
    print('\nTesting 2nd previous (-2) associations')
    print('  2nd Previous a =',d['a',-2],'...should be a2')
    print('  2nd Previous b =',d['b',-2],'...should be b1')
    try:
        d['c',-2]
        print('  ERROR: 2nd Previous c should have raised exception')
    except KeyError:
        print('  2nd Previous c correctly raised exception')
        
    print('\nTesting 3rd previous (-3) associations: only 2 preivous kept so all should be exceptions')
    try:
        d['a',-3]
        print('  ERROR: 3rd Previous a should have raised exception')
    except KeyError:
        print('  3rd Previous a correctly raised exception')
    try:
        d['a',-3]
        print('  ERROR: 3rd Previous b should have raised exception')
    except KeyError:
        print('  3rd Previous b correctly raised exception')
        

    print('\nIterator over key/value by association frequency (order is important)')
    for k,v in d.iter_frequency():    # __iterator__ shows all keys,values for errors
        print('  current association: ',repr(k),'->',repr(v))
   
    
    print()
    import driver
    #Uncomment the following lines to see MORE details on exceptions
    driver.default_file_name = 'bscile3S20.txt'
    #But better to debug putting testing code above
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
    driver.driver()
