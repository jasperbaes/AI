# Naive Bayes - Jasper Baes

By feeding this program some training data, it can classify a new record. </br>
This method is relatively simple, but not the most accurate. Especially not with small training datasets. </br>
If no values are True for an option, we have a 'Zero Frequency'. If this occurs, the result is inaccurate.

## Example 1
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

## Example 2

| Age     | Income | Student | Credit Rating | Buys Computer |
| ------- | ------ | ------- | ------------- | ------------- |
| <=30    | high   | no      | fair          | no            |
| <=30    | high   | no      | excellent     | no            |
| 31...40 | high   | no      | fair          | yes           |
| >40     | medium | no      | fair          | yes           |
| >40     | low    | yes     | fair          | yes           |
| >40     | low    | yes     | excellent     | no            |
| 31...40 | low    | yes     | excellent     | yes           |
| <=30    | medium | no      | fair          | no            |
| <=30    | low    | yes     | fair          | yes           |
| >40     | medium | yes     | fair          | yes           |
| <=30    | medium | yes     | excellent     | yes           |
| 31...40 | medium | no      | excellent     | yes           |
| 31...40 | high   | yes     | fair          | yes           |
| >40     | medium | no      | excellent     | no            |
| <=30    | medium | yes     | fair          | ?             |

## Usage
```
$ python3 run.py 
 Prediction for ['<=30', 'medium', 1, 'fair']:
 0.0282 vs 0.0069
 True / Yes  :  19.55%
 False / No  :  80.45%
```