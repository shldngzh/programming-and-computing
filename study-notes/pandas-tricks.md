
how to join two DFs by A's column is conditioned to columns of B

````python
price = pd.DataFrame({'Time': pd.date_range('20180101', '20180105'), 'Price': [100, 101, 99, 100, 102]})

event = pd.DataFrame({'StartDate': pd.to_datetime(['20180101', '20180103', '20180105']), 'EndDate': pd.to_datetime(['20180101', '20180104', '20180105']), 'Event': ["Aliens're attacking", "The Sun is out", "No Gravity anymore"]})

x, y = np.where((price.Time.values[:, None] >= event.StartDate.values) & (price.Time.values[:, None] <= event.EndDate.values))

df = pd.concat([price.Time.iloc[x].reset_index(drop=True), event['Event'].iloc[y].reset_index(drop=True)], axis=1)
print(df)
````

  |      Time | Price|
0 |2018-01-01 |   100|
1 |2018-01-02 |   101|
2 |2018-01-03 |   99|
3 |2018-01-04 |   100|
4 |2018-01-05 |   102|


   StartDate    EndDate                Event
0 2018-01-01 2018-01-01  Aliens're attacking
1 2018-01-02 2018-01-04       The Sun is out
2 2018-01-04 2018-01-05   No Gravity anymore

        Time                Event
0 2018-01-01  Aliens're attacking
1 2018-01-03       The Sun is out
2 2018-01-04       The Sun is out
3 2018-01-05   No Gravity anymore
