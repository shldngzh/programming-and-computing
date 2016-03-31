# hardcode for normal distribution N(mu, sigma) pdf & cdf

```python
import math

def npdf_std(x):
    return math.exp(-x**2 / 2)/math.sqrt(2*math.pi)

def npdf(x, mu, sigma):
    z = float(x-mu)/sigma
    return 1./sigma*pdf_std(z)

def ncdf(target, mu, sigma):
    target = float(target)
    x = target - 25*sigma
    N = 50000
    dx = (target-x)/N
    s = 0.
    while x < target:
        s += pdf(x,mu,sigma) * dx
        x += dx
    return s
    
```
