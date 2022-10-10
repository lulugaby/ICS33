# Submitter: gicarbon(Carbonero, Gabriella)
# Partner  : knluc(Luc, Keisun)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody


def read_voter_preferences(file : open):
    return {line.strip().split(";")[0]:line.strip().split(";")[1:] for line in file}
    
def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    if key != None: return ''.join("  " + str(t[0]) + " -> " + str(t[1])+ "\n" for t in ([(a,num) for num in sorted([b for k,b in d.items()], reverse= reverse) for a,v in d.items() if v==num]))
    return ''.join("  " + str(_k) + " -> " + str(d[_k])+ "\n" for _k in sorted(d.keys(),reverse=reverse))

def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    dic = {name:0 for name in cie}
    for k,v in vp.items():
        for can in v:
            if can in cie:
                dic[can] +=1
                break
    return dic
        
def remaining_candidates(vd : {str:int}) -> {str}:
    dic = {v:{ a for a,b in vd.items() if v==b}for k,v in vd.items()}
    if len(dic.keys()) == 1: return set()
    return ({t[1] for t in sorted([(v,k) for k,v in vd.items()],reverse=True)[:-1]})
    
def run_election(vp_file : open) -> {str}:
    dic = read_voter_preferences(vp_file)
    vp_file.seek(0)
    cie = {i for i  in [v for k,v in read_voter_preferences(vp_file).items()][0]}
    while len(cie) != 2:
        cie = remaining_candidates(evaluate_ballot(dic,cie))
    return remaining_candidates(evaluate_ballot(dic,cie))

  
  
  
  
    
if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
