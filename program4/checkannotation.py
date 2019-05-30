# Submitter: cncota(Cota, Claudia)
from goody import type_as_str
import inspect
from builtins import AssertionError

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value, check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 


class Check_Annotation():
    checking_on  = True

    def __init__(self,f):
        self._f = f
        self.checking_on = True
          
    def check(self,param,annot,value,check_history=''):
        def check_dict():
            if isinstance(value, dict) == False:
                raise AssertionError
            if len(annot) > 1:
                raise AssertionError
            for i in value.keys():
                if type(i) not in annot.keys():
                    raise AssertionError 
            for v in value.values():
                if type(v) not in annot.values():
                    raise AssertionError
                           
        def check_list():
            if type(value) is not list:
                raise AssertionError
            elif len(annot) > 1:
                if len(annot) != len(value):
                    raise AssertionError
                for x in range(len(annot)):
                    if type(value[x]) != annot[x]:
                        raise AssertionError
            for a in annot:
                if type(a) == type([]):
                    for g in value:
                        for h in g:
                            for b in a:
                                if type(h) != (b):
                                    raise AssertionError
            for v in value:
                if type(v) != list:   
                    if type(v) not in annot:
                        raise AssertionError
                else:
                    pass
   
        def check_tuple():
            if type(value) is not tuple:
                raise AssertionError
            elif len(annot) > 1:
                if len(annot) != len(value):
                    raise AssertionError
                for x in range(len(annot)):
                    if type(value[x]) != annot[x]:
                        raise AssertionError
            for a in annot:
                if type(a) == type(()):
                    for g in value:
                        for h in g:
                            for b in a:
                                if type(h) != (b):
                                    raise AssertionError
            for v in value:
                if type(v) != tuple:   
                    if type(v) not in annot:
                        raise AssertionError
                else:
                    pass
        
        def check_set():
            if type(value) is not set:
                raise AssertionError
            if len(annot) > 1:
                raise AssertionError
            for x in value:
                if type(x) not in annot:
                    raise AssertionError
        
        def check_frozenset():
            if type(value) is not frozenset:
                raise AssertionError
            if len(annot) > 1:
                raise AssertionError
            for x in value:
                if type(x) not in annot:
                    raise AssertionError
        
        def check_lambda():
            try:
                if len(annot) > 1:
                    raise AssertionError
                if len(annot) < 1:
                    raise AssertionError
                try: 
                    if annot(value) == False:
                        raise AssertionError
                except:
                    raise AssertionError
            except:
                pass   
        
        if annot == None:
            pass
        elif type(annot) is type:
            if annot == type([]):
                if type(value) != annot:
                    raise AssertionError
            elif type(value) != type(annot):
                raise AssertionError
            else:
                pass
        elif type(annot) is list:
            check_list()
        elif type(annot) is tuple:
            check_tuple()
        elif isinstance(annot, dict) == True:
            check_dict()
        elif type(annot) is set:
            check_set()
        elif type(annot) is frozenset:
            check_frozenset()
        elif inspect.isfunction(annot) == True:
            check_lambda()  
            
        else:
            raise AssertionError
   

    def __call__(self, *args, **kargs):
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if param.name not in bound_f_signature.arguments:
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments

        try:
            if self.checking_on == True:
                p = param_arg_bindings()
                an = self._f.__annotations__
                for x in p:
                    return self.check(x,an.get(x),p.get(x))
              
            else:
                return self._f()           

        except AssertionError:
#            print(80*'-')
#             for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
#                 print(l.rstrip())
#            print(80*'-')
            raise

  
if __name__ == '__main__':     
           
    import driver
    driver.driver()
