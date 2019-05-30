
import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    nodes_dict = defaultdict(set)
    for line in file:
        nodes = line[0:3].split(';')
        nodes_dict[nodes[0]].add(nodes[1])
    return nodes_dict   


def graph_as_str(graph : {str:{str}}) -> str:
    str_graph = '  '
    keylist = []
    keylist.extend(graph.items())
    keylist.sort(key=lambda tup: tup[0])
    for item in range(len(keylist)):
        valuelist = sorted(keylist[item][1])
        str_graph += str(keylist[item][0])+' -> '+ str((valuelist)) +'\n  '
    return str_graph[0:-2]
        

        
def reachable(graph : {str:{str}}, start : str) -> {str}:
    reached_nodes = set()
    explore_nodes = [str(start)]
    running = True
    while running:
        try:
            for k in explore_nodes:
                for item in range(len(explore_nodes)):
                    if explore_nodes[item] not in reached_nodes:
                        to_add = list(graph.get(k))
                        for node in to_add:
                            if node not in reached_nodes:
                                explore_nodes.append(node)
                x = explore_nodes.pop(item)
                reached_nodes.add(x)
                if len(explore_nodes) == 0:
                    running=False
                    break
                else:
                    pass
        finally:
            pass
    return reached_nodes
    
        
        





if __name__ == '__main__':
    dict_graph = read_graph(goody.safe_open(" Enter the name of a file with a graph",'r','',default=''))
    str_graph = graph_as_str(dict_graph)
    print(' ')
    print('Graph: source -> {destination} edges')
    print(str_graph)
    print(" ")
    starting_nodes = []
    for line in dict_graph:
        starting_nodes.append(line[0])
    running = True
    while running:
        starting_node = str(input("Enter the name of a starting node: "))
        
        if starting_node == "quit":
            running = False
            break
        elif starting_node not in dict_graph:
            print("  Entry Error: "+starting_node+" ;  Illegal: not a source node\n  Please enter a legal String\n")

        else:
            print_set = reachable(dict_graph, starting_node)
            print("From "+ starting_node+" the reachable nodes are " +(print_set))
              

    print()
    import driver
    driver.default_file_name = "bsc1.txt"
    driver.driver()
