# Binary Naive Bayes - Jasper Baes

By feeding this program some binary training data, it can classify a new record. </br>
This method is relatively simple, but not the most accurate. Especially not with small training datasets. </br>
If no values are True for an option, we have a 'Zero Frequency'. If this occurs, the result is inaccurate.

## Example
1 = True  = Yes <br>
0 = False = No

| Adult | Employed | Relationship | Women | Alcoholic |
| ----- | -------- | ------------ | ----- | --------- |
| 1     | 0        | 0            | 0     | 1         |
| 1     | 0        | 1            | 0     | 1         |
| 0     | 1        | 0            | 1     | 1         |
| 0     | 0        | 0            | 1     | 0         |
| 1     | 1        | 1            | 0     | 0         |
| 1     | 0        | 1            | 1     | 0         |
| 1     | 0        | 0            | 1     | 0         |
| 0     | 1        | 0            | 0     | 0         |
| 0     | 1        | 1            | 1     | ???       |

This will predict the outcome of the last record.

## Usage
```
$ python3 run.py 
 0.0046 vs 0.024
 The chance of False is 5.18 times bigger then True 
 TRUE  :  16.17%
 FALSE :  83.83%
```