```python
from datetime import datetime 

time_str = '2001-3-21'
time = datetime.strptime(time_str, '%Y-%m-%D')
print(time)
```
