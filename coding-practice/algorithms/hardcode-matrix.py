class Matrix(object):
    
    def __init__(self, m, n, multi_list=None):
        
        self.shape = (m, n)
        mat = [[0]*n for m_ in range(m)]
            
        if multi_list:
            self.shape = (m, n)
            mat = [multi_list[m_] for m_ in range(m)]
   
        self.matrix = mat
    
    def __str__(self):
        return str(self.matrix)
    
    def ones(self, m, n):
        mat = [[1]*n for m_ in range(m)]
        return mat
    
    def get_transpose(self):
        m, n = self.shape
        mat = [[0]*m for n_ in range(n)]
        for i in range(n):
            for j in range(m):
                mat[i][j] = self.matrix[j][i]
                
        return Matrix(n, m, mat)


    def get_minor(self, i, j):
        m, n = self.shape
        M = self.matrix
        if m == 1 or n == 1:
            return M
        mat = [[ele_ for ele_ in M[k] if M[k].index(ele_) != j-1] for k in range(n) if k != i-1]  
        return Matrix(m-1, n-1, mat)
    
    
    def get_det(self):
        m, n = self.shape
        first_row = self.matrix[0]
        if (m,n)==(1,1):
            return self.matrix[0][0]
        else:
            s = []
            i = 1
            for j in range(n):
                s.append(first_row[j] * self.get_minor(i,j+1).get_det())
            sign = [(-1)**i for i in range(n)]  
            return sum([s[i]*sign[i] for i in range(n)])
        
        
    def get_cofactor(self):
        m, n = self.shape
        cofactor = Matrix(m, n)
        for i in range(m):
            for j in range(n):
                cofactor.matrix[i][j] = (-1)**(i+1+j+1)*(self.get_minor(i+1, j+1).get_det())
        return cofactor
    
    
    def get_adjugate(self):
        return self.get_cofactor().get_transpose()
        
        
    def get_inverse(self):
        m, n = self.shape
        det = float(self.get_det())
        adjugate = self.get_adjugate()
        for i in range(m):
            for j in range(n):
                adjugate.matrix[i][j] = adjugate.matrix[i][j]/det
        return adjugate
    
    def dot(self, Mat):
        m, n1 = self.shape
        n2, p = Mat.shape
        if n1!=n2:
            raise 'error: dimensions not compatable'
        else:
            n = n1
        
        if m!=1 and p!=1:
            prd = Matrix(m, p)
            MatT = Mat.get_transpose()
            for i in range(m):
                for j in range(p):
                    prd.matrix[i][j] = sum([self.matrix[i][k] * MatT.matrix[j][k] for k in range(n)])
        elif p==1 and m!=1:
            prd = Matrix(m, p)
            for i in range(m):
                prd.matrix[i] = sum([self.matrix[i][k] * Mat.matrix[k] for k in range(n)])
                
        elif m==1 and p==1:
            prd = Matrix(m, p)
            for i in range(p):
                prd.matrix[i] = sum([self.matrix[i][k] * Mat.matrix[k] for k in range(n)])
        return prd
