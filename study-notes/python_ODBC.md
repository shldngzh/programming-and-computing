# The best interaction between Python & MSSQL
## pyodbc + pandas

### method 1
```python
import pyodbc
import pandas as pd

conn = pyodbc.connect('DSN=xxx')
df = pd.read_sql_query('SQL QUERY', conn)

conn.close()
```    
### method 2
```python
import pyodbc
import pandas as pd

with pyodbc.connect('DSN=xxx') as conn:
    df = pd.read_sql_query('<QUERY>', conn)
    
df.head()
```

    
