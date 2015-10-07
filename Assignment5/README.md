# Assignment 5 - Markov Maze Navigation
## Usage
```
> python mdp.py <yourWorld.txt> <epsilon value>
```

## My Solution (epsilon 0.5)
### My Path
```
Node: [7, 0] Utility: 3.34
Node: [7, 1] Utility: 3.70
Node: [7, 2] Utility: 4.11
Node: [7, 3] Utility: 4.61
Node: [6, 3] Utility: 5.30
Node: [5, 3] Utility: 6.69
Node: [4, 4] Utility: 10.46
Node: [3, 4] Utility: 13.49
Node: [2, 4] Utility: 17.45
Node: [1, 4] Utility: 20.55
Node: [0, 5] Utility: 27.70
Node: [0, 6] Utility: 30.62
Node: [0, 7] Utility: 35.15
Node: [0, 8] Utility: 39.56
Node: [0, 9] Utility: 50.00
```

### My Utility Matrix
```
15.80   17.53   19.46   21.61   23.85   27.70   30.62   35.15   39.56   50.00   
0.00    0.00    14.98   17.76   20.55   19.80   0.00    25.31   0.00    36.00   
11.43   12.69   14.09   15.62   17.45   13.82   0.00    20.23   22.08   27.91   
0.00    10.14   0.00    0.00    13.49   10.36   13.26   16.76   0.00    20.09   
6.22    7.86    0.00    8.28    10.46   0.00    9.62    11.94   11.14   15.47   
4.84    4.09    0.00    6.69    8.13    0.00    7.76    9.29    0.00    11.14   
3.60    1.27    0.00    5.30    5.33    0.00    6.15    6.24    0.00    0.00    
3.34    3.70    4.11    4.61    4.68    4.76    5.34    5.41    4.81    4.33    
```

#### Effect of Varying Epsilon
#Solution for 0.5:
My Epsilon Value for my solution listed above was 0.5 (See Above)

#Solution for epsilon 2:
Same epsilon == 0.5 solution, but there were slightly different utilities
```
Node: [7, 0] Utility: 3.33
Node: [7, 1] Utility: 3.70
Node: [7, 2] Utility: 4.10
Node: [7, 3] Utility: 4.60
Node: [6, 3] Utility: 5.30
Node: [5, 3] Utility: 6.69
Node: [4, 4] Utility: 10.46
Node: [3, 4] Utility: 13.49
Node: [2, 4] Utility: 17.45
Node: [1, 4] Utility: 20.55
Node: [0, 5] Utility: 27.70
Node: [0, 6] Utility: 30.62
Node: [0, 7] Utility: 35.15
Node: [0, 8] Utility: 39.56
Node: [0, 9] Utility: 50.00
```

#Solution for epsilon 10:
Same as epsilon == 0.5, but slightly different utilities
```
Node: [7, 0] Utility: 3.28
Node: [7, 1] Utility: 3.66
Node: [7, 2] Utility: 4.06
Node: [7, 3] Utility: 4.57
Node: [6, 3] Utility: 5.27
Node: [5, 3] Utility: 6.66
Node: [4, 4] Utility: 10.42
Node: [3, 4] Utility: 13.46
Node: [2, 4] Utility: 17.41
Node: [1, 4] Utility: 20.53
Node: [0, 5] Utility: 27.70
Node: [0, 6] Utility: 30.62
Node: [0, 7] Utility: 35.15
Node: [0, 8] Utility: 39.56
Node: [0, 9] Utility: 50.00
```

#Solution for epsilon 100:
Same as epsilon == 0.5, but slightly different utilities
```
Node: [7, 0] Utility: 2.16
Node: [7, 1] Utility: 2.51
Node: [7, 2] Utility: 2.90
Node: [7, 3] Utility: 3.41
Node: [6, 3] Utility: 4.11
Node: [5, 3] Utility: 5.23
Node: [4, 4] Utility: 8.52
Node: [3, 4] Utility: 11.38
Node: [2, 4] Utility: 14.69
Node: [1, 4] Utility: 18.04
Node: [0, 5] Utility: 26.00
Node: [0, 6] Utility: 29.39
Node: [0, 7] Utility: 34.39
Node: [0, 8] Utility: 39.24
Node: [0, 9] Utility: 50.00
```


