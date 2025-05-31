import autograd.numpy as np

class Matrica:
    pass

eps = 10 ** -12
class Matrica:
    n=0
    m=0
    def readFromFile(strPath):
        with open(strPath,'r') as file:
            newValues = []
            for line in file:
                row = [float(x) for x in line.strip().split()]
                newValues.append(row)

            return Matrica(newValues)
    def get(self,i,j):
        return self.values[i][j]
    def set(self, i, j, x):
        self.values[i][j] = x


    def __init__(self, values):
        self.values = np.array(values)
        self.n, self.m = self.values.shape

    def __add__(self, other):
        newValues = [[0 for _ in range(self.m)] for _ in range(self.n)]
        for i in range(0,self.n):
            for j in range(0,self.m):
                newValues[i][j] = self.get(i,j)+other.get(i,j)
        return Matrica(newValues)

    def __sub__(self, other):
        newValues = [[0 for _ in range(self.m)] for _ in range(self.n)]
        for i in range(0,self.n):
            for j in range(0,self.m):
                newValues[i][j] = self.get(i,j)-other.get(i,j)
        return Matrica(newValues)

    def __mul__(self, other):
        if isinstance(other, (int,float)):
            newValues = [[0 for _ in range(self.m)] for _ in range(self.n)]
            for i in range(0, self.n):
                for j in range(0, self.m):
                    newValues[i][j] = self.get(i,j) * other
            return Matrica(newValues)
        if self.m != other.n:
            return None
        n,m,kk = self.n, other.m,other.n
        newValues = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(0, n):
            for j in range(0, m):
                for k in range(0,kk):
                    newValues[i][j] += self.get(i,k) * other.get(k,j)

        return Matrica(newValues)

    def __isub__(self, other):
        for i in range(self.n):
            for j in range(self.m):
                self.set(i, j, self.get(i, j) - other.get(i, j))

    def __iadd__(self, other):
        for i in range(self.n):
            for j in range(self.m):
                self.set(i,j,self.get(i,j)+other.get(i,j))
        return self

    def _transpose(self):
        return self.__invert__()

    def __invert__(self):
        newValues = [[0 for _ in range(self.n)] for _ in range(self.m)]
        for i in range(0,self.n):
            for j in range(0,self.m):
                newValues[j][i] = self.get(i,j)
        return Matrica(newValues)

    def __eq__(self, other):
        if self.n != other.n or self.m != other.m:
            return False
        for i in range(0, self.n):
            for j in range(0, self.m):
                if self.get(i,j) == other.get(i,j):
                    return False
        return True

    def _equal_precise(self, other):
        if self.n != other.n or self.m != other.m:
            return False
        for i in range(0, self.n):
            for j in range(0, self.m):
                if abs(self.get(i,j) - other.get(i,j)) >eps :
                    return False
        return True

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            for j in range(0, self.m):
                s+= str(self.get(i,j)) + " "
            s+= "\n"
        return s

    def __neg__(self):
        newValues = [[-x for x in row] for row in self.values]
        return Matrica(newValues)

    def __truediv__(self, value):
        copy = self._copy()
        for i in range(0, self.n):
            for j in range(0, self.m):
                copy.set(i,j,copy.get(i,j)/value)
        return copy

    def _copy(self):

        copy_values = [[0 for _ in range(self.m)] for _ in range(self.n)]

        for i in range(self.n):
            for j in range(self.m):
                copy_values[i][j] = self.get(i,j)

        return Matrica(copy_values)

    def _save_to_file(self, string_path):
        with open(string_path, "w") as file:
            file.write(self.__str__())

    def _supst_unaprijed(self, b:Matrica):
    #Ly=b
        bcopy = b._copy()
        for i in range(self.n-1):
            for j in range(i+1,self.n):
                bcopy.values[j][0] -= self.get(j,i) * bcopy.get(i,0)
        return bcopy

    def _supst_unatrag(self,b:Matrica):
    # Ux=y
        bcopy = b._copy()
        for i in reversed(range(self.n)):
            if abs(self.get(i,i)) < eps:
                raise Exception("element 0 ili blizu nule, supst_unatrag nemoguca, singularna matrica")
            bcopy.values[i][0] /= self.get(i,i)
            for j in range(i):
                bcopy.values[j][0] -= self.get(j,i) * bcopy.get(i,0)
        return bcopy

    def LU(self):
        copy = self._copy()
        for i in range(self.n-1):

            for j in range(i+1,self.n):
                if abs(copy.get(i,i)) < eps :
                    raise Exception("nemoguc LU")
                copy.values[j][i] /= copy.get(i,i)
                for k in range(i+1,self.n):
                    copy.values[j][k] -= copy.get(j,i)*copy.get(i,k)
        return copy

    def LUP(self):

        copy = self._copy()
        P = [i for i in range(copy.n)]

        for i in range(copy.n-1):
            pivot = i
            for j in range(i+1,copy.n):
                if abs( copy.get(P[j],i)) > abs(copy.get(P[pivot],i) ):
                    pivot = j

            tmp = P[i]
            P[i] = P[pivot]
            P[pivot] = tmp

            for j in range(i+1,copy.n):
                if abs(copy.get(P[i],i)) < eps :
                    raise Exception("nemoguc LUP")
                copy.values[P[j]][i] /= copy.get(P[i],i)
                for k in range(i+1,copy.n):
                    copy.values[P[j]][k] -= copy.get(P[j],i) * copy.get(P[i],k)

        P_matrix = [[0 for _ in range(copy.m)] for _ in range(copy.n)]
        for index in range(len(P)) :
            P_matrix[index][P[index]] = 1
        return copy, Matrica(P_matrix)

    def _inverse(self):
        if self.determinanta() < eps:
            raise Exception("singularna matrica, determinanta 0")
        E_arr = [[1 if i == j else 0 for j in range(self.n)] for i in range(self.n)]
        E = Matrica(E_arr)

        lu,P = self.LUP()
        lu = P * lu
        A_inv = self._copy()

        for i in range(self.n):
            y = lu._supst_unaprijed(P * E._get_column(i) )
            x = lu._supst_unatrag(y)
            A_inv._set_column(i,x)
        return  A_inv

    def _get_column(self,index):
        column = [[0] for _ in range(self.n)]
        for i in range(self.n):
            column[i][0] = self.get(i,index)
        return Matrica(column)
    def _set_column(self,index,column:Matrica):
        for i in range(self.n):
            self.set(i,index, column.get(i,0))

    def determinanta(self):
        lu ,P = self.LUP()
        lu = P*lu
        print("LUP")
        print(lu)
        det = 1
        p_det = 1
        for i in range(self.n):
            det *= lu.get(i,i)
            if P.get(i,i) != 1: p_det*=-1
        return - det * p_det