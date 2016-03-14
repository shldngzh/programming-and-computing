import numpy as np
def lis(arr):
    L = [1] * len(arr)
    for i in range(1, len(L)):
        for j in range(i):

            if arr[j] < arr[i]:

                if L[i] < 1 + L[j]:
                    L[i] = 1 + L[j]

                print('i', i, 'j', j, 'arr_i', arr[i],
                      'arr_j', arr[j],
                      'L_j', L[j],
                      'L_i', L[i],
                      'L', L)
    return L


arr = [1,3,2,3,2,4,5,6,2]
#arr = [9,2,6,1,2,4]
#arr = [3,6,7,9,2,8,3,7]

print(arr)
print(len(arr), lis(arr))
