'''
Created on Feb 14, 2016

@author: Claudia Nazareth
'''
import keyword
from imp import reload
import pcollections,inspect
reload(pcollections)
from pcollections import pnamedtuple as pnt
# Test pnamedtuple (as pnt)
Triple1    = pnt('Triple1', 'a b c')
print(Triple1.source_code)
print(Triple1.source_code)
print(keyword.kwlist)   