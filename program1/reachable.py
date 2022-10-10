# Submitter: gicarbon(Carbonero, Gabriella)
# Partner  : knluc(Luc, Keisun)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody
import prompt
from collections import defaultdict

def read_graph(file : open) -> {str:{str}}:
    dic = {line.strip()[0]:set() for line in file}
    for k,v in dic.items():
        file.seek(0)
        for l in file:
            if k==l.strip()[0]:v.add(l.strip()[-1])
    return dic
    
def graph_as_str(graph : {str:{str}}) -> str:
    return ''.join("  " + str(key) + " -> " + str(sorted([i for i in graph[key]]))+ "\n" for key in sorted(graph.keys()))
            
def reachable(graph : {str:{str}}, start : str, trace : bool = False) -> {str}:  
    past_nodes= []  
    past_nodes.append(start)
    def search(node,graph, product):
        product.add(node)
        for n in graph[node]: 
            product.add(n)
            if n in graph.keys() and graph[n] not in past_nodes:
                past_nodes.append(graph[node])
                search(n,graph,product)
        return(product)
    return(search(start,graph, set()))
    







if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
