# Submitter: cncota(Cota, Claudia)
import goody
from collections import defaultdict

def read_ndfa(file : open) -> {str:{str:{str}}}:
    ndfa_dict = {}
    for line in file:
        inlines = (line[:].strip()).split(';')
        ninlines = inlines[1:]
        num = 0
        fa_tuples = []
        for iner in range(int(len(ninlines)/2)):
            fa_tuples.append((ninlines[num], ninlines[num+1]))
            #iner_dictionary.update(dict2)
            num+=2
        d = defaultdict(set)
        for v, b in fa_tuples:
            d[v].add((b))
        dict3 = {inlines[0]:d}
        ndfa_dict.update(dict3)
    return ndfa_dict


def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    fa_str = ""
    nfa = sorted(ndfa)
    for item in nfa:
        fa_list = list(ndfa[item].items())
        nfa_list = [] 
        for items in fa_list:
            inner_list = []
            for y in (items[1]):
                inner_list.append(y)
            inner_list.sort()
            nfa_list.append((items[0],inner_list))
        nfa_list.sort(key=lambda tup: tup[0])
        fa_str += ("  "+(str(item)+" transitions: "+ str(list(nfa_list))+"\n"))
    return fa_str

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    fa_list = [state]
    x = [state]
    for num in inputs:
        k_list = set() 
        remove_list = []
        for k in x:
            h = ndfa[k]
            if ndfa[k] == []:
                remove_list.append(str(k))
            elif num not in h.keys():
                remove_list.append(str(k))
            else:
                remove_list.append(str(k))
                g = list(ndfa[k][num])
                for item in g:
                    k_list.add(item)
        for i in remove_list:
            x.remove(i)
        fa_list.append((num, k_list))
        if len(k_list) == 0:
            return fa_list
        for items in list(k_list):
            x.append(items)
    return fa_list
        

def interpret(result : [None]) -> str:
    fa_str = ""
    fa_str += str("Start state = "+ result[0]+ "\n")
    for line in result[1:]:
        if line[1] == None:
            fa_str += str("  Input = "+ line[0]+"; illegal input: simulation terminated\n")
        else:
            str_in = sorted(list(line[1]))
            fa_str += str("  Input = "+ str(line[0])+"; new possible states = "+str(str_in)+"\n")
    fa_str += "Stop state(s) = " + str(sorted(list(result[-1][1])))+"\n"
    return fa_str





if __name__ == '__main__':
    fa_dict = read_ndfa(goody.safe_open("Enter the name of a file with a non-deterministic finite automaton",'r','',default=''))
    print("\nNon-Deterministic Finite Automaton")
    print(ndfa_as_str(fa_dict))
    ss_fa = goody.safe_open("Enter the name of a file with the start-state and input",'r','',default='')
    print(" ")
    for line in ss_fa:
        ss = line.strip().split(";")
        print("Starting new simulation")
        print(interpret(process(fa_dict, ss[0], ss[1:]))) 
              

    print()
    import driver
    driver.default_file_name = "bsc4.txt"  
    driver.driver()
