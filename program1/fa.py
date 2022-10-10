# Submitter: gicarbon(Carbonero, Gabriella)
# Partner  : knluc(Luc, Keisun)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody

def read_fa(file : open) -> {str:{str:str}}:  
    dic = {line.strip().split(";")[0]:line.strip().split(";")[1:]  for line in file}
    for k,v in dic.items():
        d_value = {}
        num=0
        for i in v:
            try:
                num = int(i) 
            except:
                d_value[str(num)]= i
        dic[k] = d_value
    return dic

def fa_as_str(fa : {str:{str:str}}) -> str:
    return ''.join("  " + key + " transitions: " + str([(i,fa[key][i]) for i in sorted(fa[key].keys())])+"\n" for key  in sorted(fa.keys()))
    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    product = [state]
    for i in inputs:
        if i not in sorted(list({x for i in fa.values() for x in i.keys()})): state=None
        else:
            state = fa[state][i]
        product.append((i, state))
    return product

def interpret(fa_result : [None]) -> str:
    product = 'Start state = '+ str(fa_result[0])+"\n" 
    state = fa_result[0]
    for i in fa_result:
        if type(i)!=str: 
            try: 
                checker_for_nonintegers = int(i[0])
                product += "  Input = " + str(i[0]) + "; "+ 'new state = '+str(i[1])+"\n" 
                state = i[1]
            except:
                state = None
                product += "  Input = " + str(i[0]) + "; "+ "illegal input: simulation terminated\n"
    product += "Stop state = " + str(state)+"\n" 
    return product
    

    



if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
