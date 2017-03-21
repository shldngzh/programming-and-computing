### search a node in an XML file with T-SQL and return the XML file (Entry)
```sql
select tmp.Entry
from 
  (select *
  from DB..table as A
    where A.Date > '2016-12-20' and A.Date < '2016-12-22'
      and A.Entry.value('(/root/root/root/root)[1]', 'varchar(50)') = 'Key1'
      and A.Entry.value('(/root/root/root/root)[1]', 'varchar(50)') like 'Key2%'
  ) as tmp
```

### table merge

```t-s
CREATE TABLE #Target(ID int, Date Date, Name varchar(10), Value int, UpdateDate datetime)
CREATE TABLE #Source(ID int, Date Date, Name varchar(10), Value int, UpdateDate datetime)

INSERT #Target(ID, Date, Name, Value, UpdateDate) VALUES(101, '3/17/2017', 'A', 1, '3/17/2017');
INSERT #Target(ID, Date, Name, Value, UpdateDate) VALUES(102, '3/17/2017', 'B', 2, '3/17/2017');
INSERT #Target(ID, Date, Name, Value, UpdateDate) VALUES(103, '3/17/2017', 'C', 3, '3/17/2017');

INSERT #Source(ID, Date, Name, Value, UpdateDate) Values(101,'3/17/2017', 'A', 1, '3/20/2017');
INSERT #Source(ID, Date, Name, Value, UpdateDate) Values(102,'3/17/2017', 'B', 3, '3/20/2017');
INSERT #Source(ID, Date, Name, Value, UpdateDate) Values(104,'3/17/2017', 'D', 4, '3/20/2017');
--INSERT #Source(ID, Date, Name, Value, UpdateDate) Values(101,'3/18/2017', 'A', 5);

--SELECT * FROM #Target
--SELECT * FROM #Source


-- 
MERGE #Target AS T
USING #Source AS S
ON (T.ID = S.ID and T.Name = S.Name and T.Date = S.Date) 
WHEN NOT MATCHED BY Target 
    THEN INSERT(ID, Date, Name, Value, UpdateDate) VALUES(S.ID, S.Date, S.Name, S.Value, S.UpdateDate)
WHEN MATCHED 
	then update set T.value = S.value, T.updatedate = S.updatedate
--when not matched by source
--	then delete
;

SELECT * FROM #Target
--SELECT * FROM #Source


Drop table #Target
drop TABLE #Source



```
