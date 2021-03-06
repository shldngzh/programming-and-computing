# Stata 13

<!-- TOC depthFrom:2 -->

- [load dates from Excel to Stata](#load-dates-from-excel-to-stata)
    - [step 1: set up the string formatted date in Excel](#step-1-set-up-the-string-formatted-date-in-excel)
    - [step 2: load & re-format date in Stata](#step-2-load--re-format-date-in-stata)
- [save multiple graphs to avoid overwriting](#save-multiple-graphs-to-avoid-overwriting)

<!-- /TOC -->

## 1. load dates from Excel to Stata
Loading dates to stata might be a mess, given how they handle formats and the difference "1900 system" vs "1960 system".
However, using `string` is a good start. 
An example as below to load convert dates (daily) in Excel to Stata (monthly) for time series analysis later.

### 1.1. step 1: set up the string formatted date in Excel
```VBA
B2 = text(A2, "mmddyy")
```

### 1.2. step 2: load & re-format date in Stata
```Stata
gen asofmonth = mofd(date(asofdate, "MDY"))
format asofmonth %tm

tsset asofmonth, monthly
```

## 2. save multiple graphs to avoid overwriting
```Stata
tsline var1, title("y1") name("y1")
tsline var2, title("y2") name("y2")
```
