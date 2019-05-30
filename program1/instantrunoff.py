# Submitter: cncota(Cota, Claudia)
import goody
from tkinter.test.runtktests import this_dir_path


def read_voter_preferences(file : open):
    vote_dict = {}
    for line in file:
        candidates = (line[2:].strip()).split(';')
        dict2 = {line[0]: candidates}
        vote_dict.update(dict2)
    return vote_dict


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    dict_str = "  "
    new_dict = None
    if key != None:
        new_dict = sorted(d.items(), key=lambda x: x[1], reverse=reverse)
    else:
        new_dict = sorted(d.items() , key = key, reverse = reverse)
    for item in new_dict:
        dict_str += str(item[0])+' -> '+ str(item[1]) +'\n  '
    return dict_str[0:-2]


def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    v_dict = {}
    for voter in cie:
        votes = 0
        dict2 = {voter:votes}
        v_dict.update(dict2)
    for item in vp.keys():
        for char in vp[item]:
            if char in cie:
                v_dict[char] += 1
                break
    return v_dict        


def remaining_candidates(vd : {str:int}) -> {str}:
    remaining_candidate = set()
    new_list = []
    new_list.extend(vd.items())
    x = min(new_list, key = lambda t: t[1])
    if len(set(vd.values())) == 1:
        return remaining_candidate
    else:
        new_list.remove(x)
    for item in new_list:
        remaining_candidate.add(item[0])
    return remaining_candidate
    


def run_election(vp_file : open) -> {str}:
    vp_dict = read_voter_preferences(vp_file)
    print(" ")
    print('Voter Preferences')
    print(dict_as_str(vp_dict))

    ballot_num = 1
    #new_vp_dict = vp_dict 
    #c_set = remaining_candidates(vp_dict)
    #print(c_set)
    #e_str =evaluate_ballot(vp_dict, c_set)
    #print(e_str)
    #new_dict_num = dict_as_str(new_vp_dict,key=lambda x : new_vp_dict[x])
    #n_set = remaining_candidates(new_dict_num)
    #n_e_str = evaluate_ballot(vp)
    cie_candidates = set()
    l = vp_dict.values()
    l.sort()
    for item in l:
        for x in item:
            cie_candidates.add(x)
        
    print("Vote count on ballot #"+str(ballot_num) +" with candidates(alphabetical order): remaining candidates = "+ str(cie_candidates))
    print(dict_as_str(evaluate_ballot(vp_dict, cie_candidates)))
    num_cie_candidates = (dict_as_str(evaluate_ballot(vp_dict, cie_candidates), key=lambda x : vp_dict[x], reverse = True))
    g = num_cie_candidates.rstrip().split('\n')
    new_cie_candidates = set()
    for y in g:
        new_cie_candidates.add(y[2])
    print("Vote count on ballot #"+str(ballot_num) +" with candidates(numerical order): remaining candidates = "+ str(new_cie_candidates))
    print(num_cie_candidates)   
    return print('set')

  
  
  

    
if __name__ == '__main__':


    print()
    import driver
    driver.default_file_name = "bsc2.txt"
    driver.driver()
