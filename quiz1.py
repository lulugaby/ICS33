'''
2. (3+1 pts) Define the function_cycler function, which takes one or more arguments: each argument is a
function with one parameter; if called with no arguments, function_cycler should raise the TypeError
exception. The function_cycler function returns a reference to a function defined inside it: this
internal/returned function takes one argument. When it is called the first time it computes the first function
passed to function_cycler on its argument; when called the second time it computes the second function
passed to function_cycler on its argument; assuming function_cycler was passed n functions, when called
the nth time it computes the nth function passed to function_cycler on its argument; when called the n+1st
time it again computes the first function passed to function_cycler on its argument. Thus, as it is called, it
keeps cycling through the n functions passed as arguments to function_cycler. For example, executing
cycler = function_cycler( (lambda x : x+1), (lambda x : 2*x), (lambda x : x**2))
and then executing cycler(1) returns 2 (1+1); then executing cycler(2) returns 4 (2*2); then executing
cycler(3) returns 9 (3**2); then executing cycler(10) returns 11 (10+1); then executing cycler(11) returns
22 (2*11); etc. For the last point of credit, determine how function_cycler‘s returned function object can
store an attribute named times_called: it stores the number of times function_cycler has been called. Hints:
use rebinding with a nonlocal declaration or use mutation but no rebinding/nonlocal. Function objects can
store attributes, but they must be setup and manipulated carefully
'''
def function_cycler(*args):
    for a in args:
        print(a)