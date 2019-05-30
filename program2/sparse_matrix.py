# Submitter: cncota(Cota, Claudia)
from builtins import int, TypeError
from goody import type_as_str

class Sparse_Matrix:
    def __init__(self, row, col, *mat):
        if type(row) is not int:
            raise AssertionError('Sparse_Matrix.__init__:Argument row'+': \''+str(row)+'\' must be int \'')
        if type(col) is not int:
            raise AssertionError('Sparse_Matrix.__init__:Argument col'+': \''+str(col)+'\' must be int \'')
        if row <= 0:
            raise AssertionError('Sparse_Matrix.__init__:Argument row'+': \''+str(row)+'\' must be greater than 0 \'')
        if col <= 0:
            raise AssertionError('Sparse_Matrix.__init__:Argument col'+': \''+str(col)+'\' must be greater than 0 \'')
        list_index = []
        for i in mat:
            if type(i[2]) not in [int, float]:
                raise AssertionError('Sparse_Matrix.__init__:Argument mat'+': \''+str(mat)+'\' must be int or float \'')
            if i[0] < 0 or i[0] > row-1:
                raise AssertionError('Sparse_Matrix.__init__:Argument row index in tuple'+': \''+str(i[0])+'\' must be between 0 and row index\'')
            if i[1] < 0 or i[1] > col-1:
                raise AssertionError('Sparse_Matrix.__init__:Argument col index in tuple'+': \''+str(i[1])+'\' must be between 0 and col index\'')
            if (i[0], i[1]) in list_index:
                raise AssertionError('Sparse_Matrix.__init__: repeated index ' +str((i[0], i[1])))
            list_index.append((i[0],i[1]))
            
        self.rows = row
        self.cols = col
        self.matrix = {}
        for m in mat:
            if m[2] != 0:
                dict2 = {(m[0],m[1]):m[2]}
                self.matrix.update(dict2)
                
    def size(self):
        return (self.rows, self.cols)
    
    def __len__(self):
        return self.rows*self.cols
    
    def __bool__(self):
        if len(self.matrix) >= 1:
            return True
        return False
    
    def __repr__(self):
        strl = ''
        for index in self.matrix.keys():
            k = self.matrix.get((index))
            strl += ','+'('+str(index[0])+","+str(index[1])+','+str(k)+')'
        return 'Sparse_Matrix('+str(self.rows)+','+str(self.cols)+strl+')'
    
    def __getitem__(self, index):
        if type(index[0]) is not int:
            raise TypeError('Sparse_Matrix.__getitem__:Argument row'+': \''+str(index[0])+'\' must be int \'')
        if type(index[1]) is not int:
            raise TypeError('Sparse_Matrix.__getitem__:Argument col'+': \''+str(index[1])+'\' must be int \'')
        if index[0] < 0:
            raise TypeError('Sparse_Matrix.__getitem__:Argument row'+': \''+str(index[0])+'\' must be greater than 0 \'')
        if index[1] < 0:
            raise TypeError('Sparse_Matrix.__getitem__:Argument col'+': \''+str(index[1])+'\' must be greater than 0 \'')
        if index[0] > self.rows-1:
            raise TypeError('Sparse_Matrix.__getitem__:Argument row'+': \''+str(index[0])+'\' must be within index \'')
        if index[1] > self.cols-1:
            raise TypeError('Sparse_Matrix.__getitem__:Argument col'+': \''+str(index[1])+'\' must be within index \'')
        if len(index) != 2:
            raise TypeError('Sparse_Matrix.__getitem__:Argument must tuple of 2\'')
        return self.matrix.get(index, 0)
    
    def __setitem__(self, index, val):
        if type(index[0]) is not int:
            raise TypeError('Sparse_Matrix.__setitem__:Argument row'+': \''+str(index[0])+'\' must be int \'')
        if type(index[1]) is not int:
            raise TypeError('Sparse_Matrix.__setitem__:Argument col'+': \''+str(index[1])+'\' must be int \'')
        if index[0] < 0:
            raise TypeError('Sparse_Matrix.__setitem__:Argument row'+': \''+str(index[0])+'\' must be greater than 0 \'')
        if index[1] < 0:
            raise TypeError('Sparse_Matrix.__setitem__:Argument col'+': \''+str(index[1])+'\' must be greater than 0 \'')
        if index[0] > self.rows-1:
            raise TypeError('Sparse_Matrix.__setitem__:Argument row'+': \''+str(index[0])+'\' must be within index \'')
        if index[1] > self.cols-1:
            raise TypeError('Sparse_Matrix.__setitem__:Argument col'+': \''+str(index[1])+'\' must be within index \'')
        if len(index) != 2:
            raise TypeError('Sparse_Matrix.__setitem__:Argument must tuple of 2\'')
        if type(val) not in [int, float]:
            raise TypeError('Sparse_Matrix.__setitem__:Argument value must be an int or float(numeric)')
        if val > 0: 
            dict2 = {index:val}
            self.matrix.update(dict2)
        if index not in self.matrix.keys():
            return
        if val == 0 and self.matrix.get(index) != 0:
            self.matrix.pop(index)
        else:
            dict2 = {index:val}
            self.matrix.update(dict2)
            
    def __delitem__(self, index):
        if type(index[0]) is not int:
            raise TypeError('Sparse_Matrix.__delitem__:Argument row'+': \''+str(index[0])+'\' must be int \'')
        if type(index[1]) is not int:
            raise TypeError('Sparse_Matrix.__delitem__:Argument col'+': \''+str(index[1])+'\' must be int \'')
        if index[0] < 0:
            raise TypeError('Sparse_Matrix.__delitem__:Argument row'+': \''+str(index[0])+'\' must be greater than 0 \'')
        if index[1] < 0:
            raise TypeError('Sparse_Matrix.__delitem__:Argument col'+': \''+str(index[1])+'\' must be greater than 0 \'')
        if index[0] > self.rows-1:
            raise TypeError('Sparse_Matrix.__delitem__:Argument row'+': \''+str(index[0])+'\' must be within index \'')
        if index[1] > self.cols-1:
            raise TypeError('Sparse_Matrix.__delitem__:Argument col'+': \''+str(index[1])+'\' must be within index \'')
        if len(index) != 2:
            raise TypeError('Sparse_Matrix.__delitem__:Argument must tuple of 2\'')
        if index not in self.matrix.keys():
            return
        self.matrix.pop(index)
        
    def row(self, num):
        if type(num) is not int:
            raise AssertionError('Sparse_Matrix.row:Argument row'+': \''+str(num)+'\' must be int \'')
        if num < 0:
            raise AssertionError('Sparse_Matrix.row:Argument row'+': \''+str(num)+'\' must be greater than 0 \'')
        if num > self.rows-1:
            raise AssertionError('Sparse_Matrix.row:Argument row'+': \''+str(num)+'\' must be within index \'')
        nums = []
        t = ()
        for x in range(self.cols):
            nums.append((self.matrix.get((num,x), 0)))
        for n in nums:
            t = t+(n,)
        return t
        
    def col(self, num):
        if type(num) is not int:
            raise AssertionError('Sparse_Matrix.col:Argument col'+': \''+str(num)+'\' must be int \'')
        if num < 0:
            raise AssertionError('Sparse_Matrix.col:Argument col'+': \''+str(num)+'\' must be greater than 0 \'')
        if num > self.rows-1:
            raise AssertionError('Sparse_Matrix.col:Argument col'+': \''+str(num)+'\' must be within index \'')
        nums = []
        t = ()
        for x in range(self.rows):
            nums.append((self.matrix.get((x,num), 0)))
        for n in nums:
            t = t+(n,)
        return t
    
    def details(self):
        t = ()
        for i in range(self.rows):
            t = t + (self.row(i),)
        return str(self.rows)+"x"+str(self.cols)+" -> "+str(self.matrix)+" -> "+ str(t)
    
    def __call__(self, nrow, ncol):
        if type(nrow) is not int:
            raise AssertionError('Sparse_Matrix.__init__:Argument row'+': \''+str(nrow)+'\' must be int \'')
        if type(ncol) is not int:
            raise AssertionError('Sparse_Matrix.__init__:Argument col'+': \''+str(ncol)+'\' must be int \'')
        if nrow <= 0:
            raise AssertionError('Sparse_Matrix.__init__:Argument row'+': \''+str(nrow)+'\' must be greater than 0 \'')
        if ncol <= 0:
            raise AssertionError('Sparse_Matrix.__init__:Argument col'+': \''+str(ncol)+'\' must be greater than 0 \'')
        self.rows = nrow
        self.cols = ncol
        m = self.matrix.copy()
        l = m.keys()
        for item in l:
            if item[0] > nrow-1:
                self.matrix.pop(item)
                
            elif item[1] > ncol-1:
                self.matrix.pop(item)
                
        
    def __iter__(self):
        mat = []
        for item in self.matrix.keys():
            mat.append((item[0],item[1],self.matrix.get(item)))
        nmat = sorted(mat,key = lambda t: t[2])
        for i in range(len(nmat)):
            yield nmat[i]
            
    def __neg__(self):
        newdict = []
        for item in self.matrix.keys():
            newdict.append((item[0],item[1], -self.matrix.get(item)))
        return Sparse_Matrix(self.rows, self.cols,*newdict)
    
    def __pos__(self):
        newdict = []
        for item in self.matrix.keys():
            newdict.append((item[0],item[1], self.matrix.get(item)))
        return Sparse_Matrix(self.rows, self.cols,*newdict)
    
    def __abs__(self):
        newdict = []
        for item in self.matrix.keys():
            newdict.append((item[0],item[1], abs(self.matrix.get(item))))
        return Sparse_Matrix(self.rows, self.cols,*newdict)
    
    def __add__(self, right):
        if type(right) not in [int, float, Sparse_Matrix]:
            raise TypeError('unsupported operand type(s) for +'+
                            ': \''+type_as_str(self)+'\' and \''+type_as_str(right)+'\'')
        if type(self) is Sparse_Matrix and type(right) is Sparse_Matrix:
            if self.size() != right.size():
                raise AssertionError("Size of two Sparse_Matrix are not equal")
            nm = Sparse_Matrix(self.rows, self.cols)
            for index in range(self.rows):
                for indexs in range(self.cols):
                    fr = self.matrix.get((index, indexs),0) + right.matrix.get((index,indexs),0)
                    nm[index,indexs] = fr
            return nm
        if type(right) in [int, float]:
            nm = Sparse_Matrix(self.rows, self.cols)
            for index in range(self.rows):
                for indexs in range(self.cols):
                    fr = self.matrix.get((index, indexs),0) + right
                    nm[index,indexs] = fr
            return nm
        
    def __radd__(self, left):
        if type(left) not in [int, float, Sparse_Matrix]:
            raise TypeError('unsupported operand type(s) for +'+
                            ': \''+type_as_str(self)+'\' and \''+type_as_str(left)+'\'')
        if type(left) in [int, float]:
            nm = Sparse_Matrix(self.rows, self.cols)
            for index in range(self.rows):
                for indexs in range(self.cols):
                    fr = left + self.matrix[index, indexs] 
                    nm[index,indexs] = fr
            return nm
        
    def __sub__(self, right):
        nright = -right
        if type(right) not in [int, float, Sparse_Matrix]:
            raise TypeError('unsupported operand type(s) for +'+
                            ': \''+type_as_str(self)+'\' and \''+type_as_str(nright)+'\'')
        if type(self) is Sparse_Matrix and type(nright) is Sparse_Matrix:
            if self.size() != nright.size():
                raise AssertionError("Size of two Sparse_Matrix are not equal")
            nm = Sparse_Matrix(self.rows, self.cols)
            for index in range(self.rows):
                for indexs in range(self.cols):
                    fr = self.matrix.get((index, indexs),0) + nright.matrix.get((index,indexs),0)
                    nm[index,indexs] = fr
            return nm
        if type(nright) in [int, float]:
            nm = Sparse_Matrix(self.rows, self.cols)
            for index in range(self.rows):
                for indexs in range(self.cols):
                    fr = self.matrix.get((index, indexs),0) + nright
                    nm[index,indexs] = fr
            return nm
        
    def __rsub__(self, left):
        if type(left) not in [int, float, Sparse_Matrix]:
            raise TypeError('unsupported operand type(s) for +'+
                            ': \''+type_as_str(self)+'\' and \''+type_as_str(left)+'\'')
        if type(left) in [int, float]:
            nm = Sparse_Matrix(self.rows, self.cols)
            for index in range(self.rows):
                for indexs in range(self.cols):
                    fr = self.matrix.get((index, indexs),0) - left
                    nm[index,indexs] = fr
            return nm
    
    def __mul__(self, right):
        if type(right) not in [int, float, Sparse_Matrix]:
            raise TypeError('unsupported operand type(s) for +'+
                            ': \''+type_as_str(self)+'\' and \''+type_as_str(right)+'\'')
        if type(self) is Sparse_Matrix and type(right) is Sparse_Matrix:
            if self.cols != right.rows:
                raise AssertionError("Size of two Sparse_Matrix are not equal")
            nm = Sparse_Matrix(self.rows, right.cols)
            for index in range(self.rows):
                for indexs in range(right.cols):
                    num = self.row(index)
                    nums = right.col(indexs)
                    xs = 0
                    xy = None
                    if len(num) > len(nums):
                        xy = num
                    else:
                        xy = nums
                    for x in range(len(xy)):
                        xs += num[x]*nums[x]
                    nm[index,indexs] = xs
            return nm
        
        if type(right) in [int, float]:
            nm = Sparse_Matrix(self.rows, self.cols)
            for index in range(self.rows):
                for indexs in range(self.cols):
                    fr = self.matrix.get((index,indexs),0) * right
                    nm[index,indexs] = fr
            return nm
        
    def __rmul__(self, left):
        if type(left) not in [int, float]:
            raise TypeError('unsupported operand type(s) for +'+
                            ': \''+type_as_str(self)+'\' and \''+type_as_str(left)+'\'')
        if type(left) in [int, float]:
            nm = Sparse_Matrix(self.rows, self.cols)
            for index in range(self.rows):
                for indexs in range(self.cols):
                    if self.matrix.get((index, indexs)) != 0:
                        fr = self.matrix.get((index, indexs),0) * left 
                        nm[index,indexs] = fr
            return nm
        
    def __pow__(self, right):
        if type(right) is not int:
            raise TypeError('unsupported operand type(s) for +'+
                            ': \''+type_as_str(self)+'\' and \''+type_as_str(right)+'\'')
        if right < 1:
            raise AssertionError('number must be greater than 0')
        if self.cols != self.rows:
            raise AssertionError('Sparse_Matrix must be square(rows and columns must be equal)')
        nm = Sparse_Matrix(self.rows, self.cols)
        for idex in range(nm.rows):
            for indexs in range(nm.cols):
                power = int(self.matrix.get((idex, indexs), 0)) ** int(right)
                nm[idex,indexs] = power
        return nm
    
    def __eq__(self, right):
        if type(right) not in [int,float,Sparse_Matrix]:
            return False
        if type(self) is Sparse_Matrix and type(right) is Sparse_Matrix:
            if self.size() == right.size():
                for c,v in self.matrix.items():
                    if right.matrix.get(c,0) == v:
                        continue
                    else:
                        return False
                return True
            else:
                return False
        if type(right) in [int, float]:
            for x in range(self.rows):
                for y in self.col(x):
                    if y!= right:
                        return False
            return True
        else:
            return False
        return False
    def __ne__(self, right):
        if type(right) not in [int,float,Sparse_Matrix]:
            return True
        if type(self) is Sparse_Matrix and type(right) is Sparse_Matrix:
            if self.size() == right.size():
                for c,v in self.matrix.items():
                    if right.matrix.get(c) == v:
                        continue
                    else:
                        return True
                return False
            return True
        if type(right) in [int, float]:
            for x in range(self.rows):
                for y in self.col(x):
                    if y!= right:
                        return True
            return False
        else:
            return True
        return True

    
   
            
            
            
                
  
    def __str__(self):
        size = str(self.rows) + 'x' + str(self.cols)
        width = max(len(str(self.matrix.get((r,c),0))) for c in range(self.cols) for r in range(self.rows))
        return size+':['+('\n'+(2+len(size))*' ').join ('  '.join('{num: >{width}}'.format(num=self.matrix.get((r,c),0),width=width) for c in range(self.cols))\
                                                                                             for r in range(self.rows))+']'





if __name__ == '__main__':
    print('Printing')
    m = Sparse_Matrix(3,3, (0,0,1),(1,1,3),(2,2,1))
    print(m)
    print(repr(m))
    print(m.details())
   
    print('\nsize and len')
    print(m.size(),len(m))
     
    print('\ngetitem and setitem')
    print(m[1,1])
    m[1,1] = 0
    m[0,1] = 2
    print(m.details())
 
    print('\niterator')
    for r,c,v in m:
        print((r,c),v)
     
    print('\nm, m+m, m+1, m==m, m==1')
    print(m)
    print(m+m)
    print(m+1)
    print(m==m)
    print(m==1)
    print()

    import driver
    driver.default_file_name = 'bsc2.txt'
    driver.driver()
