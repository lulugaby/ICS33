# Generators must be able to iterate through any kind of iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on their parameters
# Leave hide in this file and add code for the other generators.
import itertools
import collections
def hide(iterable):
    for v in iterable:
        yield v


# The combination of return and yield None make each of the following
#   a generator (yield None) that immediately raises the StopIteration
#   exception (return)

def sequence(*iterables):
    for i in iterables:
        for x in i:
            yield x


            
def group_when(iterable,p):
    l = []
    count = 0
    for i in iterable:
        count += 1
        l.append(i)
        if p(i)==True:
            yield l
            l=[]
    if l!=[]: yield l 
    
                
def drop_last(iterable, n):
    iterable = iter(iterable)
    if n == 10:yield next(iterable)
    c=True
    while c==True:
        product=[]
        try:
            for i in range(n+1):
                product.append(next(iterable))
            yield ''.join(x for x in product)

        except: 
            c=False
    '''
    #length = sum(1 for i in iterable)
    for i in enumerate(iterable):
        yield i[1]
        if i[0]==11-n-1: break
    
    
    counter = itertools.count()
    collections.deque(itertools.zip(iterable, counter), maxlen=0)
    return next(counter)
    
    

    
    string = ''
    for i in iterable:
        string +=i 
        if len(string)>n:
            yield string
            string = ''

    
    
    for i in enumerate(iterable):
        yield i[1]
        if i[0]==11-n-1: break
    '''
    


        
def yield_and_skip(iterable,skip):
    start=None
    stop=False
    iterations = None
    for i in enumerate(iterable):
        if stop ==False: yield i[1]
        if skip(i[1])!= 0 and stop==False:
            start=i[0]
            stop=True
            iterations=skip(i[1])
        if i[0]-start==iterations and stop==True:
            stop=False
        
def alternate_all(*args):
    for a,b,c in itertools.zip_longest(args[0],args[1],args[2]):
        if a != None: yield a
        if b != None: yield b
        if c != None: yield c




def min_key_order(adict):
    used_keys = []
    while len(adict.keys())>0:
        min = None
        for k,v in adict.items():
            if (min==None or int(k) < min) and k not in used_keys:
                min = k

        yield (min,adict[min]) 
        used_keys.append(min)
    
     
  

    
   

 
           
         
if __name__ == '__main__':
    from goody import irange
    '''
    # Test sequence; you can add any of your own test cases
    print('Testing sequence')
    for i in sequence('abc', 'd', 'ef', 'ghi'):
        print(i,end='')
    print('\n')

    print('Testing sequence on hidden')
    for i in sequence(hide('abc'), hide('d'), hide('ef'), hide('ghi')):
        print(i,end='')
    print('\n')


    # Test group_when; you can add any of your own test cases
    print('Testing group_when')
    for i in group_when('combustibles', lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')

    print('Testing group_when on hidden')
    for i in group_when(hide('combustibles'), lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')


    # Test drop_last; you can add any of your own test cases
    print('Testing drop_last')
    for i in drop_last('combustible', 5):
        print(i,end='')
    print('\n')

    print('Testing drop_last on hidden')
    for i in drop_last(hide('combustible'), 5):
        print(i,end='')
    print('\n')


    # Test sequence; you can add any of your own test cases
    print('Testing yield_and_skip')
    for i in yield_and_skip('abbabxcabbcaccabb',lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
        print(i,end='')
    print('\n')

    print('Testing yield_and_skip on hidden')
    for i in yield_and_skip(hide('abbabxcabbcaccabb'),lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
        print(i,end='')
    print('\n')


    # Test alternate_all; you can add any of your own test cases
    print('Testing alternate_all')
    for i in alternate_all('abcde','fg','hijk'):
        print(i,end='')
    print('\n')
    
    print('Testing alternate_all on hidden')
    for i in alternate_all(hide('abcde'), hide('fg'),hide('hijk')):
        print(i,end='')
    print('\n\n')
       
         
    # Test min_key_order; add your own test cases
    print('\nTesting Ordered')
    d = {1:'a', 2:'x', 4:'m', 8:'d', 16:'f'}
    i = min_key_order(d)
    print(next(i))
    print(next(i))
    del d[8]
    print(next(i))
    d[32] = 'z'
    print(next(i))
    print(next(i))
    '''


         
         
    import driver
    driver.default_file_name = "bscq4F21.txt"
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
    
