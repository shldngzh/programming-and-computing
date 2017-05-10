# Stata 13

## load dates from Excel to stata
Loading dates to stata might be a mess, given how they handle formats and the difference "1900 system" vs "1960 system".
However, using ```c string``` is a good
### step 1 set up the string formatted date in Excel
An example as below.
```Excel
B2 = text(A2, "mmddyy")
```
