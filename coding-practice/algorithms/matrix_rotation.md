# Matrix Rotation

### Acknowledgement  
This coding challenge is posted on hackerrank.com, by [Heraldo](https://www.hackerrank.com/Heraldo). Thanks to him for contributing this algo problem that I spent 2 hours to finish. And yes it is recognized as __hard__.

## Problem Statement  
You are given a 2D matrix, a, of dimension MxN and a positive integer R. You have to rotate the matrix R times and print the resultant matrix. Rotation should be in anti-clockwise direction.  
Rotation of a 4x5 matrix is represented by the following figure. Note that in one rotation, you have to shift elements by one step only (refer sample tests for more clarity).  
![alt tag] (https://github.com/shldngzh/programming-and-computing/blob/master/pic/matrix-rotation.png)  
It is guaranteed that the minimum of M and N will be even.
### Input Format
First line contains three space separated integers, M, N and R, where M is the number of rows, N is number of columns in matrix, and R is the number of times the matrix has to be rotated.   
Then M lines follow, where each line contains N space separated positive integers. These M lines represent the matrix.  
### Output Format  
Print the rotated matrix.  
### Constraints   
2 <= M, N <= 300  
1 <= R <= 109   
min(M, N) % 2 == 0   
1 <= aij <= 108, where i ∈ [1..M] & j ∈ [1..N]  

## code below

```python
# fetch inputs
M, N, R = [int(i_) for i_ in input().strip().split()]
mat = [[ele_ for ele_ in list(map(int, input().strip().split()))] for m_ in range(M)]

# split mat into loops
def mat_to_loops(mat, M, N):
    P = int(min(M, N) / 2) # how many loops to generate
    loops = {}
    # generate matrices with zeros
    for p_ in range(P):
        loops[p_] = [[0 for n_ in range(N)] for m_ in range(M)]
    # fetch loops values
    for p_ in range(P):
        # for each loop
        imax = M - p_
        jmax = N - p_
        for i in [p_, M - p_ - 1]:
            for j in range(p_, jmax):
                #print(p_, i, j, mat[i][j])
                loops[p_][i][j] = mat[i][j]
        for j in [p_, N - p_ - 1]:
            for i in range(p_, imax):
                loops[p_][i][j] = mat[i][j]
    return loops  


# because we use linked-list here, so define a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = next
                    
# rotate a loop
def rotate_loop(loop, p_, R):
    
        
    def loop_to_lk(loop):
        ll = []
        i = p_
        for j in range(p_, N - p_):
            ll.append(loop[i][j])
            
        j = N - p_ - 1
        for i in range(p_ + 1, M - p_):
            ll.append(loop[i][j])
            
        i = M - p_ - 1
        for j in range(N - p_ - 2, p_ - 1, -1):
            ll.append(loop[i][j])

        j = p_
        for i in range(M - p_ - 2, p_, -1):
            ll.append(loop[i][j])
        
        lk = [0 for i in range(len(ll))]
        
        for i in range(len(ll)):
            lk[i] = Node(ll[i])
            
        for i in range(len(ll)):
            if i == len(ll) - 1:
                lk[i].next = lk[0]
            else:
                lk[i].next = lk[i+1]
            
        return lk
    
    lk = loop_to_lk(loop)
    #for i in range(len(lk)):
    #    print('lk', lk[i].data)
    
    # rotate
  
    head = lk[0]
    for r in range(R):
        head = head.next

    lk2 = [0 for i_ in range(len(lk))]
    for i in range(len(lk)):
        lk2[i] = head
        head = head.next
        
    #for i in range(len(lk2)):
    #    print('lk2', lk2[i].data)
    
            
    def lk_to_loop(lk, M, N):
        loop = [[0 for n_ in range(N)] for m_ in range(M)]
        head = lk[0]
        i = p_
        for j in range(p_, N - p_):
            loop[i][j] = head.data
            head = head.next
        
        j = N - p_ - 1
        for i in range(p_ + 1, M - p_):
            loop[i][j] = head.data
            head = head.next
            
        i = M - p_ -1
        for j in range(N - p_ - 2, p_ - 1, -1):
            loop[i][j] = head.data
            head = head.next
            
        j = p_
        for i in range(M - p_ - 2, p_, -1):
            loop[i][j] = head.data
            head = head.next
 
        return loop

    return lk_to_loop(lk2, M, N)

def rotate_mat(mat, M, N, R):
    loops = mat_to_loops(mat, M, N)
    P = int(min(M, N) / 2)
    for p_ in range(P):
        loops[p_] = rotate_loop(loops[p_], p_, R)
    for m_ in range(M):
        for n_ in range(N):
            mat[m_][n_] = sum([v[m_][n_] for k,v in loops.items()])
    return mat
        
    
            
          
res = rotate_mat(mat, M, N, R)
for i in range(len(res)):
    print(*res[i])



```









