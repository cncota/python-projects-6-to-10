# Submitter: cncota(Cota, Claudia) 
from goody       import safe_open
from collections import defaultdict # Use defaultdict for prefix and query


def all_prefixes(fq : (str,)) -> {(str,)}:
    prefix_dict = set()
    all_items= ()
    for item in fq:
        all_items = all_items + (item,)  
        prefix_dict.add(all_items)
    return prefix_dict


def add_query(prefix : {(str,):{(str,)}}, query : {(str,):int}, new_query : (str,)) -> None:
    all_items = ()
    for item in new_query:
        all_items = all_items + (item,)   
        prefix[all_items].add((new_query))
    query[new_query] += 1
    return None


def read_queries(open_file : open) -> ({(str,):{(str,)}}, {(str,):int}):
    p,q = defaultdict(set), defaultdict(int)
    for line in open_file:
        item = tuple(line.strip().split(" "))
        add_query(p, q, item)
    return (p, q)


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    dict_str = "  "
    for k in sorted(d, key=key, reverse=reverse):
        dict_str += str(k) +' -> '+ str(d.get(k)) +'\n  '
    return dict_str[0:-2]


def top_n(a_prefix : (str,), n : int, prefix : {(str,):{(str,)}}, query : {(str,):int}) -> [(str,)]:
    n_list = []
    
    if a_prefix not in prefix:
        return n_list
    n_prefix = prefix.get(a_prefix)
    
    n_query = {}
    k_list = []
    for l in n_prefix:
        dict2 = {l:query.get(l)}
        n_query.update(dict2)
    
    for k in sorted(n_query, key = lambda x : (-n_query[x],x)):
        if len(n_prefix) == 0:
            return n_list
        else:
            k_list.append(k)
    if len(n_prefix) < int(n):
        return k_list
    else:
        for num in range(n):
            n_list.append(k_list[num])
    return n_list
              
            
        


if __name__ == '__main__':
    p,q = read_queries(safe_open("Enter the name of a file with the full queries",'r','',default=''))
    print("\nPrefix dictionary")
    print(dict_as_str(p,lambda x : (len(x),x)))
    print("Query dictionary")
    print(dict_as_str(q,lambda x : (-q[x],x)))
    running = True
    while running:
        x = input("Enter a prefix (or quit): ")
            
        if x == "quit":
            running = False
            break
    
        x_in = ()
        for item in x.strip().split(" "):
            x_in = x_in + (item,)

        print("  Top 3 (at the most) full queries =" + str(top_n(x_in, 3, p, q)))
        
        y = input("Enter a full query (or quit): ")
       
        if y == "quit":
            running = False
            break
        y_in = ()
        for items in y.strip().split(" "):
            y_in = y_in + (items,)

        add_query(p, q, y_in)
        print("\nPrefix dictionary")
        print(dict_as_str(p,lambda x : (len(x),x)))
        print("Query dictionary")
        print(dict_as_str(q,lambda x : (-q[x],x)))
    
    

    print()
    import driver
    driver.default_file_name = "bsc5.txt"

    driver.driver()
