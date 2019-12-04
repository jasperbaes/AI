# Binary Bayes - Jasper Baes

By feeding this program some binary training data, it will predict other cases (classification).

## Usage
1 = True <br>
0 = False

| Option 1 | Option 2 | Option 3 | Option 4 | Result |
| -------- | -------- | -------- | -------- | ------ |
| 1        | 0        | 0        | 0        | 1      |
| 1        | 0        | 1        | 0        | 1      |
| 0        | 1        | 0        | 1        | 1      |
| 0        | 0        | 0        | 1        | 0      |
| 1        | 1        | 1        | 0        | 0      |
| 1        | 0        | 1        | 1        | 0      |
| 1        | 0        | 0        | 1        | 0      |
| 0        | 1        | 0        | 0        | 0      |
| 0        | 1        | 1        | 1        | ???    |

This will predict the outcome of the last record

```
$ python3 run.py 
 0.021 vs 0.0027
 The chance of True is 7.69 times bigger then False 
 ========================================================
 TRUE  :  86.99%
 FALSE :  13.01%
```