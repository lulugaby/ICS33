from goody import irange
from goody import type_as_str

import math

class Fraction:
    # Call as Fraction._gcd(...); no self parameter
    # Helper method computes the Greatest Common Divisor of x and y
    @staticmethod
    def _gcd(x : int, y : int) -> int:
        assert x >= 0 and y >= 0, 'Fraction._gcd: x('+str(x)+') and y('+str(y)+') must be >= 0'
        while y != 0:
            x, y = y, x % y
        return x

    # Returns a string that is the decimal representation of a Fraction, with
    #   decimal_places digitst appearing after the decimal points.
    # For example: if x = Fraction(23,8), then x(5) returns '2.75000'
    def __call__(self, decimal_places):
        answer = ''
        num = self.num
        denom = self.denom
    
        # handle negative values
        if num < 0:
            num, answer = -num, '-'
    
        # handle integer part
        if num >= denom:
            answer += str(num//denom)
            num     = num - num//denom*denom
            
        # handle decimal part
        answer += '.'+str(num*10**decimal_places//denom)
        return answer
    
    @staticmethod
    # Call as Fraction._validate_arithmetic(..); with no self parameter
    # Helper method raises exception with appropriate message if type(v) is not
    #   in the set of types t; the message includes the values of the strings
    #   op (operator), lt (left type) and rt (right type)
    # An example call (from my __add__ method), which checks whether the type of
    #   right is a Fraction or int is...
    # Fraction._validate_arithmetic(right, {Fraction,int},'+','Fraction',type_as_str(right))
    def _validate_arithmetic(v, t : set, op : str, lt : str, rt : str):
        if type(v) not in t:
            raise TypeError('unsupported operand type(s) for '+op+
                            ': \''+lt+'\' and \''+rt+'\'')        

    @staticmethod
    # Call as Fraction._validate_relational(..); with no self parameter
    # Helper method raises exception with appropriate message if type(v) is not
    #   in the set of types t; the message includes the values of the strings
    #   op (operator), and rt (right type)
    def _validate_relational(v, t : set, op : str, rt : str):
        if type(v) not in t:
            raise TypeError('unorderable types: '+
                            'Fraction() '+op+' '+rt+'()')        


    def __init__(self,num=0,denom=1):
        if type(num)!= int or type(denom)!= int: raise AssertionError()
        
        self.num = num 
        self.denom = denom

        # if num ==0 
        if num == 0:
            self.denom = 1

        #simplify 
        elif denom < 0 :
            self.num = -num
            self.denom = abs(denom)
            if num < 0: self.denom = abs(denom)
        
        #simplyfing the fractions
        for i in range(num+1):
            if i != 1 and i != 0:
                if self.num%i==0 and self.denom%i==0:
                    self.num = int(self.num/i) 
                    self.denom = int(self.denom/i)
            
        

    def __repr__(self):
        return 'Fraction('+str(self.num)+','+str(self.denom)+')'
    
    def __str__(self):
        return str(self.num)+'/'+str(self.denom)
   

    def __bool__(self):
        if self.num == 0: return False
        else: return True
    
    

    def __getitem__(self,i):
        if i in self.__dict__.keys():
            return self.__dict__[i]

        else:
            if type(i)==int:
                if i == 0: return self.num
                elif i == 1: 
                    return self.denom
                else: raise TypeError()
            else:
                if 'd' in i: return self.denom
                elif 'n' in i : return self.num
                else: raise TypeError()
    
    
 
    def __pos__(self):
        return  str(self.num) + '/' + str(self.denom)
    
    def __neg__(self):
        return  str(-self.num) + '/' + str(abs(self.denom))
    
    def __abs__(self):
        return  str(abs(self.num)) + '/' + str(abs(self.denom))
    

    def __add__(self,right):
        #print('add')
        if type(right)== int:
            right = Fraction(right, 1)
        elif type(right)== float : raise TypeError()
        denom = self.denom * right.denom
        num_a = self.num * right.denom 
        num_b = right.num * self.denom
        num = num_a + num_b
        return Fraction(num, denom)

    def __radd__(self,left):
        #print('add')
        right = left 
        if type(right)== int:
            right = Fraction(right, 1)
        elif type(right)== float : raise TypeError()
        denom = self.denom * right.denom
        num_a = self.num * right.denom 
        num_b = right.num * self.denom
        num = num_a + num_b
        return Fraction(num, denom)

    def __sub__(self,right):
        #print('sub')
        if type(right)== int:
            right = Fraction(right, 1)
        elif type(right)== float : raise TypeError()
        denom = self.denom * right.denom
        num_a = self.num * right.denom 
        num_b = right.num * self.denom
        num = num_a - num_b
        return Fraction(num, denom)
     
    def __rsub__(self,left):
        #print('sub')
        right = left
        if type(right)== int:
            right = Fraction(right, 1)
        elif type(right)== float : raise TypeError()
        denom = self.denom * right.denom
        num_a = self.num * right.denom 
        num_b = right.num * self.denom
        num = num_b - num_a
        return Fraction(num, denom)

     
    def __mul__(self,right):
        if type(right)== float : raise TypeError()
        elif type(right)==str: 
            right = right.split('/')
            right = Fraction(int(right[0]), int(right[-1]))
        elif type(right)== int:right = Fraction(right, 1)
        denom = self.denom * right.denom
        num = right.num * self.num
        return Fraction(num, denom)
        

    def __rmul__(self,left):
        #print('mul2')
        right = left
        if type(right)== float : raise TypeError()
        elif type(right)==str: 
            right = right.split('/')
            right = Fraction(int(right[0]), int(right[-1]))
        elif type(right)== int:right = Fraction(right, 1)
        elif type(right)== float : raise TypeError()
        denom = self.denom * right.denom
        num = right.num * self.num
        return Fraction(num, denom)

    
    def __truediv__(self,right):
        #print('div')
        if type(right)== float : raise TypeError()
        elif type(right)== int:right = Fraction(right, 1)
        num = self.num * right.denom
        denom = self.denom * right.num
        return Fraction(num, denom)

    def __rtruediv__(self,left):
        #print('div')
        right = left
        if type(right)== float : raise TypeError()
        elif type(right)== int:right = Fraction(right, 1)
        num = right.num * self.denom
        denom = right.denom * self.num
        return Fraction(num, denom)


    def __pow__(self,right):
        #print('pow')
        if type(right)!= int : raise TypeError()
        if self.num != 1: 
            self.denom = self.num 
            self.num = 1
        num = self.num 
        denom = self.denom ** abs(right)
        return Fraction(num, denom)


    def __eq__(self,right):
        if type(right)== float : raise TypeError()
        elif type(right) == int:
            return False
        elif right.num == self.num and right.denom==self.denom: return True
        else: return False
    

    def __lt__(self,right):
        
        if type(right)== float: raise TypeError()
            
        if type(right) == int: 
            s = self.num/self.denom
            if s < right: return True
            else : return False
        s = self.num/self.denom
        r= right.num/ right.denom
        if s < r: return True
        else : return False

    
    def __gt__(self,right):
        if type(right)== float: raise TypeError()
            
        if type(right) == int: 
            s = self.num/self.denom
            if s > right: return True
            else : return False
        s = self.num/self.denom
        r= right.num/ right.denom
        if s > r: return True
        else : return False

    # Uncomment this method when you are ready to write/test it
    # If this is pass, then no attributes will be set!
    def __setattr__(self,name,value):
        if name in self.__dict__.keys() and name=='num':
            if value == self.__dict__[name]: raise NameError()   
        self.__dict__[name]=value
 


##############################


# Newton: pi = 6*arcsin(1/2); see the arcsin series at http://mathforum.org/library/drmath/view/54137.html
# Check your results at http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html
#   also see http://www.numberworld.org/misc_runs/pi-5t/details.html

def compute_pi(n):
    pass




if __name__ == '__main__':
    # Put in simple tests for Fraction before allowing driver to run
 
    print()
    import driver
    
    driver.default_file_name = 'bscq31F21.txt'
#     driver.default_show_traceback= True
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
    driver.driver()
