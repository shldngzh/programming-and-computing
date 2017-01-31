# The best interaction between Python & MSSQL
## pyodbc + pandas

```python
import pyodbc
import pandas as pd

conn = pyodbc.connect('DSN=xxx')
df = pd.read_sql_query('SQL QUERY', conn)

conn.close()
```    
    
