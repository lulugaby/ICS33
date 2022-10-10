# Submitter: gicarbon(Carbonero, Gabriella)
# Partner  : knluc(Luc, Keisun)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody

def read_ndfa(file : open) -> {str:{str:{str}}}:
    dic = {}
    for line in file: 
        values = []
        for x in enumerate(line.strip().split(';')[1:]):
            if x[0] == 0 or x[0]%2 == 0:
                key = x[1]
            else: 
                values.append((key,x[1]))  
        keys = {tup[0] for tup in values}
        dic[line.strip().split(';')[0]] = {key:{tup[1] for tup in values if key==tup[0]} for key in keys}       
    return dic
    
def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    return ''.join("  " + k +" transitions: "+ str(sorted([(a,sorted([i for i in b])) for a,b in v.items()])) + "\n" for k,v in {key:ndfa[key] for key in sorted(ndfa.keys())}.items())
           
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    product = [state]
    states = [state]
    for i in inputs:
        product_states=set()
        states = {s for s in states if i in ndfa[s].keys()}
        for x in states:
            for a in ndfa[x][i]: 
                product_states.add(str(a))
        product.append((i, product_states)) 
        if product_states == set(): break
        states = product_states            
    return product

def interpret(result : [None]) -> str:
    return ("Start state = " + str(result[0]) + "\n" + "".join("  Input = " + x[0] + "; new possible states = " + str(sorted([i for i in x[1]])) + "\n" for x in result[1:]) + "Stop state(s) = "+ str(sorted([i for i in result[-1][1]]))+ "\n")



if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
