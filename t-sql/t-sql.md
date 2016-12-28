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

