
from collections import defaultdict
from goody import type_as_str

class Bag:
    def __init__(self, item_list = []):
        self.__bagdict = defaultdict(int)
        self.__item_list = item_list
        if len(item_list) >= 1:
            for k in item_list:
                self.__bagdict[k] += 1
            
    def __repr__(self):
        return "Bag("+str(self.__item_list)+")"
    
    def __str__(self):
        r_str = 'Bag('
        if len(self.__bagdict) < 1:
            return "Bag()"  
        for x,y in self.__bagdict.items():
            r_str += str(str(x) + str([y])+',')
        return str(r_str[:-1]+'}')
    
    def __len__(self):
        return len(self.__item_list)
    
    def unique(self):
        r_set = []
        for k,v in self.__bagdict.items():
            r_set.append(v)
        return len(r_set)
    
    def __contains__(self, item):
        for v in self.__bagdict.keys():
            if item == v:
                return True
        return False
    
    def add(self, item):
        self.__item_list.append(item)
        self.__bagdict[item] += 1
    
    def count(self, item):
        num = 0
        for i in self.__item_list:
            if i == item:
                num += 1
        return num
    
    def __add__(self, right):
        n_list = []
        if type(right) is not Bag:
            raise TypeError('unsupported operand type(s) for +'+
                            ': \''+type_as_str(self)+'\' and \''+type_as_str(right)+'\'') 
        n_list.extend(self.__item_list)
        n_list.extend(right.__item_list)
        return Bag(n_list)
    
    def remove(self, item):
        if item not in self.__bagdict.keys():
            raise ValueError("Argument must be inside in Bag")
        if self.__bagdict.get(item) > 1:
            self.__bagdict[item] -= 1
            self.__item_list.remove(item)
        elif self.__bagdict.get(item) == 1:
            self.__bagdict.pop(item)
            self.__item_list.remove(item)
            
    def __eq__(self, right):
        if type(right) is not Bag:
            return False
        return self.__bagdict == right.__bagdict
        
    def __ne__(self, right):
        if type(right) is not Bag:
            return True
        return self.__bagdict != right.__bagdict
            
    def __iter__(self):
        class bag_iter:
            def __init__(self,item_list):
                self.i_l = list(item_list)
            def __next__(self):
                for i in range(len(self.i_l)):
                    answer = self.i_l[i]
                return answer
        return bag_iter(self.__item_list)
        
            
             





if __name__ == '__main__':

    print()
    import driver
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.default_file_name = 'bsc1.txt'
    driver.driver()
