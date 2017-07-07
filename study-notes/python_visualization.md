# python visualization

## fill under line
```python
fig, ax = plt.figure()
ax.fill_between(x, 0, y1)
```

## 3d surface plot
```python
x = np.array([1,2,3,4,5])
y = np.array([2, 5, 10, 30])
x, y = np.meshgrid(x, y)
z = <some value>

fig = plt.figure(figsize=(12, 12))
ax = fig.gca(projection='3d')
ax.plot_surface(x, y, z, alpha=0.5)
plt.show()
```


## import
```python
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from rpy2.robjects.vectors import DataFrame, Vector
from rpy2.robjects import numpy2ri
from rpy2.robjects.lib import ggplot2
import seaborn
#seaborn.set(style='ticks')
mpl.style.use('seaborn-paper')
```
