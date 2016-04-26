# Dynamic Programming

#### maximum subarray sum

```python
def max_subarr(arr, N):
    # N = len(arr)
    res = [arr[n_] for n_ in range(N)]
    for i in range(1, N):
        for j in range(i):
            if arr[i] > arr[j] and res[i] < res[j] + arr[i]:
                    res[i] = res[j] + arr[i]
    return max(res)
````
