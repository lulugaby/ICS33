import re, traceback, keyword
# Submitter: gicarbon(Carbonero, Gabriella)
# Partner  : vogb(Gia Bao Vo)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming


def pnamedtuple(type_name, field_names, mutable = False,  defaults =  {}):
    if type(field_names) == set: raise SyntaxError
    try:
        for i in field_names.split():
            if i =='if': raise SyntaxError
            if i[0]== '_':raise SyntaxError
            if ord(i[0]) >= 49 and ord(i[0]) <= 57: raise SyntaxError
    except AttributeError: pass
        
    def show_listing(s):
        for ln_number, text_of_ln in enumerate(s.split('\n'),1):       
            print(f' {ln_number: >3} {text_of_ln.rstrip()}')

    #print('debug',field_names)
    if type(field_names)== str:
        #print('str', field_names)
        if ',' in field_names: field_names = field_names.split(',')
        else:field_names = field_names.split()
        field_names = [i.strip() for i in field_names]
        #print (field_names)
    #else: print(type(field_names))

    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    class_template = '''\
class {name}:
    filter = set({init})
    mutable = {bool}
    defaults = {contain}

    def __init__(self, {args}):
        {iargs}
    
    def __repr__(self): 
        return f'{name}({repr})'
    
    {get_x}

    def __getitem__(self, index):
        if type(index)==int: 
            i  = {field_names}[index]
            return self.__dict__[i]
        else:
            if index not in  self.__dict__: raise IndexError()
            return self.__dict__[index]
    
    def __eq__(self, other):
        if str(self)!=str(other): return False
        return True
    
    def _asdict(self):
        return self.__dict__

    def _make(list):      
        return {name}(list[0],list[1],list[2])

    def _replace(self, **kargs):
        print({bool})
        if {bool} is True: 
            for k,v in kargs.items():
                if k not in self.__dict__: raise TypeError()
                self.__dict__[k] = v
            print({name}({repr}))
            
        else:
            dic = dict()

            for k,v in kargs.items():
                if k not in self.__dict__: raise TypeError()
                dic[k] = v
        
            for a,b in self.__dict__.items():
                if a not in dic:
                    dic[a]=b
            vals = ''.join(k+'='+str(v)+"," for k,v in dic.items())[:-1]
            l = [b for a,b in dic.items()]
            return {name}._make(l)
                      

'''  
    class_definition= \
      class_template.format(init ='['+','.join(["'"+i+"'" for i in field_names if i !=',' and i!=' '])+']', 
                            field_names= field_names,
                            name=type_name, 
                            bool= mutable, 
                            contain=defaults, 
                            args= ''.join(f+", " for f in field_names)[:-2],
                            iargs= ''.join("self."+f+" = "+f+"\n        " for f in field_names)[:-2],
                            repr = ''.join(f[1] + '={self.' + f[1] + '},' for f in enumerate(field_names,1))[:-1],
                            get_x = ''.join('def get_'+f+"(self):\n        return self."+ f +'\n    ' for f in field_names),
                            vals = None
                            )

    #__repr__ = 'meow'
    #print(''.join(f[1] + '=' + str(f[0]) + ',' for f in enumerate(field_names,1))[:-1] )
    for f in enumerate(field_names,1):
        print(f)
    # Debugging aid: uncomment show_listing below so it always displays source code
    show_listing(class_definition)
    
    # Execute class_definition's str from name_space; followed by binding the
    #   attribute source_code to the class_definition; after the try/except bloc
    #   return this created class object; if any syntax errors occur, show the
    #   listing of the class and trace the error, in the except clause
    name_space = dict( __name__ = f'pnamedtuple_{type_name}' )
    #print('result', name_space)
    try:
        exec(class_definition,name_space)  
    except: raise SyntaxError    

    try:
        name_space[type_name].source_code = class_definition
    except (TypeError,SyntaxError):                   
        show_listing(class_definition)
        traceback.print_exc()
    #print(name_space[type_name].__dict__)
    return name_space[type_name]


    
if __name__ == '__main__':
    # Test simple pnamedtuple below in script: Point=pnamedtuple('Point','x,y')
    
    #t1 = Triple1(1,2,3)
    #print('test',repr(t1),t1.a)
    #driver tests
    import driver  
    driver.default_file_name = 'bscp3F21.txt'
#     driver.default_show_exception_message = True
#     driver.default_show_traceback = True
    driver.driver()
