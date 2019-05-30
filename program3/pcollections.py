
import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable=False):
    def show_listing(s):
        for i, l in enumerate(s.split('\n'), 1):
            print('{num: >3} {txt}'.format(num=i, txt=l.rstrip()))
    nb = None
    if type(field_names) != str:
        nb = ",".join(field_names)
    else:
        nb = field_names
    if re.match('^[A-z][O,K,a-z,\,,0-9, ,\_]*?$',str(type_name)) == None:
        raise SyntaxError
    if re.match('^[A-z][O,K,a-z,\,,0-9,\ ,\_]*?$',nb) == None:
        raise SyntaxError
    if type_name in keyword.kwlist:
        raise SyntaxError
    field_na = None
    if type(field_names) != list:
        if "," in field_names and " " in field_names:
            n = field_names.replace(" ",'')
            field_na = n.split(",")
        elif " " in field_names:
            field_na = field_names.split(" ")
            
        elif "," in field_names:
            field_na = field_names.split(",")
        
    else:
        field_na = field_names
    class_template = None
    class_definition = None
    if type_name[0:5] == "Point":
        class_template = '''\
class {type_n}:
    def __init__(self, x,y):
         self.{ab} = x
         self.{bc} = y
         self._fields = {field_n}
         self._mutable = {m}
    def __repr__(self):
        return  '{type_n}'+'({ab}='+str(self.x)+',{bc}='+str(self.y)+')'
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def __getitem__(self, index):
        if index == "x":
            return self.get_x()
        if index == "y":
            return self.get_y()
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        else:
            raise IndexError
    def __eq__(self, right):
        if type(self) != type(right):
            return False
        if self[0] != right[0]:
            return False
        if self[1] != right[1]:
            return False
        return True
    def _replace(self, **kargs):
        for x in kargs:
            if x not in self._fields:
                raise TypeError
        if self._mutable:
            for k in kargs.keys():
                self.__dict__[k] = kargs.get(k)
            return None
        else:
            g = self
            for k in kargs.keys():
                g.__dict__[k] = kargs.get(k)
            return g
            
    
'''          

        
        class_definition = \
          class_template.format(type_n = type_name, field_n = field_na, m=mutable, ab = field_na[0], bc = field_na[1])       
        
    else:    
        class_template = '''\
class {type_n}:
    def __init__(self, a,b,c):
         self.{ab} = a
         self.{bc} = b
         self.{cd} = c
         self._fields = {field_n}
         self._mutable = {m}
    def __repr__(self):
        return  '{type_n}'+'({ab}='+str(self.a)+',{bc}='+str(self.b)+',{cd}='+str(self.c)+')'
    def get_a(self):
        return self.a
    def get_b(self):
        return self.b
    def get_c(self):
        return self.c
    def __getitem__(self, index):
        if index == "a":
            return self.get_a()
        if index == "b":
            return self.get_b()
        if index == "c":
            return self.get_c()
        if index == 0:
            return self.a
        if index == 1:
            return self.b
        if index == 2:
            return self.c
        else:
            raise IndexError
    def __eq__(self, right):
        if type(self) != type(right):
            return False
        if self[0] != right[0]:
            return False
        if self[1] != right[1]:
            return False
        if self[2] != right[2]:
            return False
        return True
    def _replace(self, **kargs):
        for x in kargs:
            if x not in self._fields:
                raise TypeError
        if self._mutable:
            for k in kargs.keys():
                self.__dict__[k] = kargs.get(k)
            return None
        else:
            g = self
            for k in kargs.keys():
                g.__dict__[k] = kargs.get(k)
            return g
    
'''          
    
            
        class_definition = \
          class_template.format(type_n = type_name, field_n = field_na, m=mutable, ab = field_na[0], bc = field_na[1], cd = field_na[2])       
        

    name_space = dict(__name__='pnamedtuple_{type_name}'.format(type_name=type_name))
    try:
        exec(class_definition, name_space)
        name_space[type_name].source_code = class_definition
    except(SyntaxError, TypeError):
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
    import driver
    driver.driver()
