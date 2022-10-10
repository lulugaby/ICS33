# Submitter: gicarbon(Carbonero, Gabriella)
# Partner  : knluc(Luc, Keisun)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import re                               # used in my sentence_at_a_time generator function
import math                           # use in cosine_meteric
import prompt                           # for use in script
import goody                            # for use in script
from collections import defaultdict     #  dicts and defaultdicts are == when they have the same keys/associations


# For use in build_semantic_dictionary: see problem specifications
def sentence_at_a_time(open_file : open, ignore_words : {str}) -> [str]:
    end_punct    = re.compile('[.?\!;:]')
    remove_punct = re.compile(r'(,|\'|"|\*|\(|\)|--)')

    prev   = []
    answer = []
    for l in open_file:
        l = remove_punct.sub(' ',l.lower())
        prev = prev + l.split()
        while prev:
            w = prev.pop(0)
            if end_punct.search(w):
                while end_punct.search(w):
                    w = w[0:-1]
                if w != '' and w not in ignore_words:
                    if end_punct.search(w):
                        print(w)
                    answer.append(w)
                    yield answer
                    answer = []
            else:
                if w != '' and w not in ignore_words:
                    answer.append(w)
                    
    # handle special case of last sentence missing final punctuation                
    if answer:
        yield answer


def build_semantic_dictionary(training_files : [open], ignore_file : open) -> {str:{str:int}}:
    
    
    tuples = [(word.lower(),w.lower()) for f in training_files for line in sentence_at_a_time(f,{i.strip() for i in ignore_file}) for word in line  for w  in line if w !=word]
    for f in training_files: f.seek(0)
    dic = {word.lower():{} for f in training_files for line in sentence_at_a_time(f,{i.strip() for i in ignore_file}) for word in line}
    dic= {k:{tup[1].lower():sum([1 for t in tuples if t[0].lower()==k and t[1].lower()==tup[1].lower()]) for tup in tuples if tup[1].lower()!=k.lower() and tup[0].lower()==k} for k,v in dic.items()}
    return{k:{a:b for a,b in v.items() if b!={}} for k,v in dic.items() if v!={}}
    
        


def dict_as_str(semantic : {str:{str:int}}) -> str:
    _max = sorted([len(v) for k,v in semantic.items()])[-1]
    _min = sorted([len(v) for k,v in semantic.items()])[0]
    return " " + ''.join(' context for ' + k + ' = ' + ''.join(sk + "@" + str(semantic[k][sk]) + ", " for sk in sorted(semantic[k].keys()))[:-2] + "\n " for k in sorted(semantic.keys())) + ' min/max context lengths = ' + str(_min) + "/" + str(_max) + '\n'
   
       
def cosine_metric(context1 : {str:int}, context2 : {str:int}) -> float:
    top = sum([context1[k]*context2[k] for k in [k for k in set(context1.keys()).intersection(context2.keys())]])
    bottom_a = math.sqrt(sum([v**2 for v in context1.values()]))
    bottom_b = math.sqrt(sum([v**2 for v in context2.values()]))
    return top/(bottom_a * bottom_b)


def most_similar(word : str, choices : [str], semantic : {str:{str:int}}, metric : callable) -> str:
    try:
        return sorted([(cosine_metric(semantic[word], semantic[c]),c) for c in choices])[-1][1]
    except:
        for c in choices:
            if c not in semantic[word].keys():
                return "Metric failure: could not choose synonym for "



def similarity_test(test_file : open, semantic : {str:{str:int}}, metric : callable) -> str:
    correct = 0
    total = 0
    product = ''
    for line in test_file:
        total += 1
        test = line.split()[-1]
        result = most_similar(line.split()[0],line.split()[1:-1], semantic, metric)
        if result==test:
            product = product + "  Correct: " + "\'"+  line.split()[0] + "\'"+ " is most like " + "\'"+  result + "\'"+ " from " + str(line.split()[1:-1]) + "\n"
            correct +=1
        elif result == "Metric failure: could not choose synonym for ":
            product = product + "  Metric failure: could not choose synonym for " + "\'"+  line.split()[0] + "\'"+   " from " + str(line.split()[1:-1]) + "\n"
        else:
            product = product + "  Incorrect: " + "\'"+  line.split()[0] + "\'"+  " is most like " + "\'"+  test + "\'"+  ", not " + "\'"+  result + "\'"+  " from " + str(line.split()[1:-1]) + "\n"
    return product + str((correct/total) * 100) + "% correct\n"
    
        




# Script

if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
'''
# Test dict_as_str
c-->s1 = {'i': {'went': 1, 'gym': 1, 'this': 1, 'morning': 2, 'later': 1, 'rested': 1, 'was': 1, 'tired': 1}, 'went': {'i': 1, 'gym': 1, 'this': 1, 'morning': 1}, 'gym': {'i': 1, 'went': 1, 'this': 1, 'morning': 1}, 'this': {'i': 1, 'went': 1, 'gym': 1, 'morning': 1}, 'morning': {'i': 2, 'went': 1, 'gym': 1, 'this': 1, 'later': 1, 'rested': 1}, 'later': {'morning': 1, 'i': 1, 'rested': 1}, 'rested': {'later': 1, 'morning': 1, 'i': 1}, 'was': {'i': 1, 'tired': 1}, 'tired': {'i': 1, 'was': 1}}
e-->repr(sy.dict_as_str(s1))-->'  context for gym = i@1, morning@1, this@1, went@1\n  context for i = gym@1, later@1, morning@2, rested@1, this@1, tired@1, was@1, went@1\n  context for later = i@1, morning@1, rested@1\n  context for morning = gym@1, i@2, later@1, rested@1, this@1, went@1\n  context for rested = i@1, later@1, morning@1\n  context for this = gym@1, i@1, morning@1, went@1\n  context for tired = i@1, was@1\n  context for was = i@1, tired@1\n  context for went = gym@1, i@1, morning@1, this@1\n  min/max context lengths = 2/8\n'
c-->s2 = pickle.load(open('pickle_simple12.pkl','rb'))
==-->repr(sy.dict_as_str(s2))-->repr(open('simple12_dict_as_str.txt').read())

# Load main semantic dictionary
c-->s1 = pickle.load(open('pickle_abdsw.pkl','rb'))

# Test cosine_metric
c-->cd1 = {'a':1, 'b':2, 'c':3}
c-->cd2 = {'a':5, 'c':7, 'd':8}
c-->print('      Computed cosine_metric 1:',sy.cosine_metric(cd1,cd2))
e-->math.isclose(sy.cosine_metric(cd1,cd2),0.5915204817512771,abs_tol=.00001)-->True
c-->print('      Computed cosine_metric 2:',sy.cosine_metric(s1['trip'],s1['journey']))
e-->math.isclose(sy.cosine_metric(s1['trip'],s1['journey']),0.3149744528481997,abs_tol=.00001)-->True
c-->print('      Computed cosine_metric 3:',sy.cosine_metric(s1['trip'],s1['party']))
e-->math.isclose(sy.cosine_metric(s1['trip'],s1['party']),0.23208313896731933,abs_tol=.00001)-->True
c-->print('      Computed cosine_metric 4:',sy.cosine_metric(s1['trip'],s1['dog']))
e-->math.isclose(sy.cosine_metric(s1['trip'],s1['dog']),0.25247681215625717,abs_tol=.00001)-->True
c-->print('      Computed cosine_metric 5:',sy.cosine_metric(s1['study'],s1['examine']))
e-->math.isclose(sy.cosine_metric(s1['study'],s1['examine']),0.35442968785576745,abs_tol=.00001)-->True
c-->print('      Computed cosine_metric 6:',sy.cosine_metric(s1['study'],s1['waste']))
e-->math.isclose(sy.cosine_metric(s1['study'],s1['waste']),0.21800003546873528,abs_tol=.00001)-->True
^-->sy.cosine_metric(s1['study'],{})-->ZeroDivisionError
^-->sy.cosine_metric({},s1['examine'])-->ZeroDivisionError

# Test most_similar
e-->sy.most_similar('trip',['journey','party','dog'],s1,sy.cosine_metric)-->journey
e-->sy.most_similar('trip',['party','journey','dog'],s1,sy.cosine_metric)-->journey
e-->sy.most_similar('trip',['party','dog','journey'],s1,sy.cosine_metric)-->journey
e-->sy.most_similar('study',['examine','waste'],s1,sy.cosine_metric)-->examine
e-->sy.most_similar('study',['waste','examine'],s1,sy.cosine_metric)-->examine

# Test similarity_test
==-->repr(sy.similarity_test(open('synonym_problems1.txt'),s1,sy.cosine_metric))-->'"  Correct: \'trip\' is most like \'journey\' from [\'party\', \'journey\', \'dog\']\\n  Correct: \'study\' is most like \'examine\' from [\'waste\', \'examine\']\\n  Correct: \'strike\' is most like \'beat\' from [\'beat\', \'complain\']\\n  Metric failure: could not choose synonym for \'bring\' from [\'fetch\', \'irvine\', \'develop\']\\n75.0% correct\\n"'
==-->repr(sy.similarity_test(open('synonym_problems.txt'),s1,sy.cosine_metric))-->'"  Incorrect: \'draw\' is most like \'paint\', not \'walk\' from [\'walk\', \'paint\']\\n  Incorrect: \'duty\' is most like \'task\', not \'example\' from [\'task\', \'example\']\\n  Correct: \'earnest\' is most like \'serious\' from [\'serious\', \'amusing\']\\n  Correct: \'picture\' is most like \'painting\' from [\'painting\', \'chair\']\\n  Correct: \'vexed\' is most like \'annoyed\' from [\'amused\', \'annoyed\']\\n  Correct: \'watch\' is most like \'see\' from [\'hear\', \'see\']\\n  Correct: \'tidy\' is most like \'clean\' from [\'mess\', \'clean\']\\n  Correct: \'youthful\' is most like \'young\' from [\'young\', \'complex\']\\n  Correct: \'strike\' is most like \'beat\' from [\'beat\', \'complain\']\\n  Correct: \'tearful\' is most like \'crying\' from [\'frowning\', \'crying\']\\n  Correct: \'lonely\' is most like \'alone\' from [\'alone\', \'together\']\\n  Correct: \'ardent\' is most like \'keen\' from [\'keen\', \'wise\']\\n  Correct: \'thief\' is most like \'robber\' from [\'robber\', \'postman\']\\n  Incorrect: \'authentic\' is most like \'genuine\', not \'false\' from [\'genuine\', \'false\']\\n  Correct: \'trip\' is most like \'journey\' from [\'party\', \'journey\']\\n  Correct: \'stroll\' is most like \'walk\' from [\'walk\', \'destroy\']\\n  Correct: \'speak\' is most like \'talk\' from [\'talk\', \'crawl\']\\n  Correct: \'begin\' is most like \'start\' from [\'sit\', \'start\']\\n  Correct: \'voyage\' is most like \'journey\' from [\'dog\', \'journey\']\\n  Correct: \'stone\' is most like \'rock\' from [\'rock\', \'chair\']\\n  Incorrect: \'detest\' is most like \'hate\', not \'regard\' from [\'regard\', \'hate\']\\n  Correct: \'genuine\' is most like \'real\' from [\'real\', \'interesting\']\\n  Correct: \'bring\' is most like \'fetch\' from [\'fetch\', \'develop\']\\n  Incorrect: \'shout\' is most like \'yell\', not \'smell\' from [\'smell\', \'yell\']\\n  Incorrect: \'ruin\' is most like \'destroy\', not \'dare\' from [\'destroy\', \'dare\']\\n  Incorrect: \'leap\' is most like \'jump\', not \'sit\' from [\'sit\', \'jump\']\\n  Correct: \'evade\' is most like \'avoid\' from [\'explore\', \'avoid\']\\n  Incorrect: \'infringe\' is most like \'violate\', not \'walk\' from [\'walk\', \'violate\']\\n  Incorrect: \'charge\' is most like \'accusation\', not \'admission\' from [\'accusation\', \'admission\']\\n  Correct: \'ruddy\' is most like \'wrinkled\' from [\'reddish\', \'wrinkled\']\\n  Correct: \'threat\' is most like \'danger\' from [\'greeting\', \'danger\']\\n  Correct: \'error\' is most like \'mistake\' from [\'mistake\', \'robber\']\\n  Correct: \'toil\' is most like \'work\' from [\'jump\', \'work\']\\n  Correct: \'serene\' is most like \'quiet\' from [\'exciting\', \'quiet\']\\n  Correct: \'study\' is most like \'examine\' from [\'waste\', \'examine\']\\n  Correct: \'road\' is most like \'path\' from [\'path\', \'tree\']\\n  Correct: \'mean\' is most like \'cruel\' from [\'boring\', \'cruel\']\\n  Correct: \'honest\' is most like \'fair\' from [\'unfriendly\', \'fair\']\\n  Correct: \'wealthy\' is most like \'rich\' from [\'rich\', \'content\']\\n  Correct: \'genuine\' is most like \'true\' from [\'green\', \'true\']\\n77.5% correct\\n"'
'''