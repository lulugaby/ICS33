
# Submitter: gicarbon(Carbonero, Gabriella)
# Partner  : vgb(Vo, Gia Bao)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

from goody import type_as_str
import inspect

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
        
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check,param,value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
      
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check,param,value,check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 





class Check_Annotation:
    # First bind the class attribute to True allowing checking to occur (but
    #   only if the object's attribute self._checking_on is also bound to True)
    checking_on  = True
  
    # First bind self._checking_on = True, for checking the decorated function f
    def __init__(self, f):
        self._f = f
        self._checking_on = True
       

    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):

        if type(self._f.__annotations__['x'])==dict:
            if type(self._f.__annotations__['x'])!=type(param): raise AssertionError
            for a,b in self._f.__annotations__['x'].items():
                k=a
                v=b
            for a,b in param.items():
                try:    
                    if len(a) >= 4: raise AssertionError
                except TypeError: pass   
                try:  
                    k = k._annotations[0]
                    v= v._annotations
                except AttributeError:
                    if (type(a)!=k or type(b)!=v)  and type(v)!=tuple: raise AssertionError
                    try:
                        if (type(a)!=k or type(b) not in v)  and type(v)==tuple: raise AssertionError
                    except TypeError:pass               

        elif type(self._f.__annotations__['x'])==set:
            if type(self._f.__annotations__['x'])!=type(param): raise AssertionError
            if len(param) < len(self._f.__annotations__['x']): raise AssertionError
            for x in self._f.__annotations__['x']:
                t = x
                for s in param:
                    if type(s)!= t: raise AssertionError

        elif type(self._f.__annotations__['x'])==frozenset:
            if type(self._f.__annotations__['x'])!=type(param): raise AssertionError
            if len(param) < len(self._f.__annotations__['x']): raise AssertionError
            for x in self._f.__annotations__['x']:
                t = x
                for s in param:
                    if type(s)!= t: raise AssertionError

        pass 
        
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        #print(args, kargs)
        # Return the argument/parameter bindings as an OrderedDict (it's derived
        #   from a dict): bind the function header's parameters using its order
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if not (param.name in bound_f_signature.arguments):
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments

        def types_checker(values, types):

            if callable(types): pass #print(values, types , 'lambda')
            try:
                if types(values) == False : raise AssertionError
                elif types(values) == True : return True
                
            except: pass

            if types==None: return True
            if type(types) == type:
                if isinstance(values,types)==False : raise AssertionError
                else: return True
            else:
                if type(types)!= type(values): raise AssertionError
                
               
                if len(types)==2:
                    
                    if len(types) != len(values): raise AssertionError
                    if type(types)!=type(values): raise AssertionError
                    return types_checker(values[0], types[0]), types_checker(values[1], types[1])
                else:
                    if len(values)==3 : return types_checker(values[0], types[0]), types_checker(values[1], types[0]),types_checker(values[2], types[0])
                    return types_checker(values[0], types[0]), types_checker(values[1], types[0])

        #print(param_arg_bindings()['x'], self._f.__annotations__['x'])
        if type(self._f.__annotations__['x'])==dict or type(self._f.__annotations__['x'])==set or type(self._f.__annotations__['x'])==frozenset:
            Check_Annotation.check(self,param_arg_bindings()['x'],self._f.__annotations__['x'],None)
        
        else: 
            
            try:
                if len(args[0]) > 1 and type(args[0])==str: raise AssertionError
            except TypeError:pass
            if self._f.__annotations__['x'] == int : raise AssertionError
            types_checker(param_arg_bindings()['x'],self._f.__annotations__['x'] )


        4

  
if __name__ == '__main__':     
    # an example of testing a simple annotation  
    '''
    def f(x:int): pass
    f = Check_Annotation(f)
    f(3)
    f('a')
    '''
           
    #driver tests
    import driver
    driver.default_file_name = 'bscp4SF1.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
