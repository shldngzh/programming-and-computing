# hardcode for stats

### normal distribution N(mu, sigma) pdf & cdf

```python
import math

def npdf_std(x):
    return math.exp(-x**2 / 2)/math.sqrt(2*math.pi)

def npdf(x, mu, sigma):
    z = float(x-mu)/sigma
    return 1./sigma*npdf_std(z)

def ncdf(target, mu, sigma):
    target = float(target)
    x = target - 25*sigma
    N = 50000
    dx = (target-x)/N
    s = 0.
    while x < target:
        s += npdf(x,mu,sigma) * dx
        x += dx
    return s
    
```

### correlation
```python
import math

def get_mean(x):
    N = float(len(x))
    return sum(x)/N

def var(x):
    N = len(x)
    x_mean = get_mean(x)
    return sum([float((x[i]-x_mean)**2)/N for i in range(N)])

def cov(x, y):
    N = len(x)
    x_mean = get_mean(x)
    y_mean = get_mean(y)
    x_ = [float(x[i]-x_mean) for i in range(N)]
    y_ = [float(y[i]-y_mean) for i in range(N)]
    return sum([x_[i]*y_[i]/N for i in range(N)])

def pearson_rho(x, y):
    return cov(x,y)/(math.sqrt(var(x)*var(y)))

def spearman_rho(x,y):
    N = len(x)
    xs = sorted(x)
    ys = sorted(y)
    rx = [xs.index(x[i]) for i in range(N)]
    ry = [ys.index(y[i]) for i in range(N)]
    return cov(rx, ry)/(math.sqrt(var(rx)*var(ry)))
```
    
    
