# Submitter: cncota(Cota, Claudia)
import goody


def read_fa(file : open) -> {str:{str:str}}:
    fa_dict = {}
    for line in sorted(file):
        inlines = (line[:].strip()).split(';')
        iner_dictionary = {}
        ninlines = inlines[1:]
        num = 0
        for iner in range(int(len(ninlines)/2)):
            dict2 = {ninlines[num]: ninlines[num+1]}
            iner_dictionary.update(dict2)
            num+=2
        dict3 = {inlines[0]:iner_dictionary}
        fa_dict.update(dict3)
    return fa_dict


def fa_as_str(fa : {str:{str:str}}) -> str:
    fa_str = ""
    nfa = sorted(fa)
    for item in nfa:
        fa_list = list(fa[item].items())
        fa_list.sort(key=lambda tup: tup[0])
        fa_str += ("  "+(str(item)+" transitions: "+ str((fa_list))+"\n"))
    return fa_str

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    fa_list = [state]
    x = state
    for num in inputs:
        if num == "x":
            fa_list.append((num, None))
        else:
            y = fa[x][num]
            fa_list.append((num, fa[x][num]))
            x = y
    return fa_list


def interpret(fa_result : [None]) -> str:
    fa_str = ""
    fa_str += str("Start state = "+ fa_result[0]+ "\n")
    for line in fa_result[1:]:
        if line[1] == None:
            fa_str += str("  Input = "+ line[0]+"; illegal input: simulation terminated\n")
        else:
            fa_str += str("  Input = "+ line[0]+"; new state = "+line[1]+"\n")
    fa_str += "Stop state = " + str(fa_result[-1][1])+"\n"
    return fa_str




if __name__ == '__main__':
    fa_dict = read_fa(goody.safe_open("Enter the name of a file with a finite automaton",'r','',default=''))
    print("\nFinite Automaton")
    print(fa_as_str(fa_dict))
    ss_fa = goody.safe_open("Enter the name of a file with the start-state and input",'r','',default='')
    print(" ")
    for line in ss_fa:
        ss = line.strip().split(";")
        print("Starting new simulation")
        print(interpret(process(fa_dict, ss[0], ss[1:])))   

    print()
    import driver
    driver.default_file_name = "bsc3.txt"
    driver.driver()
