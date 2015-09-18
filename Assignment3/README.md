# Assignment 3
###### A * path finding algorithms in python
## Heuristic Chosen
###### Euclidian
I choose the euclidian heuristic which is a more direct way to estimate the distance from your current position to the goal

Base Equation: a^2 + b^2 = c^2 (pythagorean theorem) then take square root of c^2 and c is the estimation to the goal

###### My Equation: 
```
product = pow(childNode.location[0], 2) + pow( (columns-1) - childNode.location[1], 2 ) //product is c^2 from aboove
ans = math.sqrt(product)  //ans is just c
childNode.heuristic = ans * 10 //multiply by 10 to get cost estimate from goal
```

###### Why Euclidian?

I figured that because euclidian is a straightline estimate and we can use diagonal moves euclidian would be an interesting change to the heuristic. The fact that it gives a direct estimate also made me believe that it would give a better result. It did give me slightly different answers which you will see in the section below. I was a little unsure as to whether I should multiply c from above by 10 or 14 above to due to what i described in the first sentence, but i did mess around with it and left it at 10.

### Results
#### Format
Node --> [7, 0] is the start, so it is in the bottom left. if you are looking at a matrix it is the cell in the 8th row in the 1st column

#### World1.txt
###### Manhattan
```
user@cu-cs-vm:~/Documents/IntroToAI/Guegan_aStarSearch$ python aStar.py World2.txt m

Evaluating solution for: World1.txt

Solution Found!!!
----------------------------------------------------------
Cost of Path: 156
# of Nodes evaluated: 86
Starting from the end: [0, 9], [0, 8], [0, 7], [0, 6], [1, 5], [1, 4], [2, 3], [2, 2], [3, 1], [4, 1], [5, 1], [6, 1], [7, 0]
```

###### Euclidian
```
user@cu-cs-vm:~/Documents/IntroToAI/Guegan_aStarSearch$ python aStar.py World1.txt e

Evaluating solution for: World1.txt

Solution Found!!!
----------------------------------------------------------
Cost of Path: 130
# of Nodes evaluated: 105
Starting from the end: [0, 9], [0, 8], [1, 7], [2, 7], [3, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [7, 1], [7, 0]
```

#### World2.txt
###### Manhattan
```
user@cu-cs-vm:~/Documents/IntroToAI/Guegan_aStarSearch$ python aStar.py World2.txt m

Evaluating solution for: World2.txt

Solution Found!!!
----------------------------------------------------------
Cost of Path: 142
# of Nodes evaluated: 68
Starting from the end: [0, 9], [0, 8], [0, 7], [0, 6], [0, 5], [1, 4], [2, 4], [3, 4], [4, 4], [5, 3], [6, 3], [7, 2], [7, 1], [7, 0]
```

###### Euclidian
```
user@cu-cs-vm:~/Documents/IntroToAI/Guegan_aStarSearch$ python aStar.py World2.txt e

Evaluating solution for: World2.txt

Solution Found!!!
----------------------------------------------------------
Cost of Path: 142
# of Nodes evaluated: 125
Starting from the end: [0, 9], [0, 8], [0, 7], [0, 6], [0, 5], [1, 4], [2, 4], [3, 4], [4, 3], [5, 3], [6, 3], [7, 2], [7, 1], [7, 0]
```

#### Summary
Euclidian seemed to evaluate more nodes in both cases, but outperformed manhattan in finding low cost in World1.txt. I believe the fact that it evaulated more nodes to be because I multiplied c in the euclidian equation above by 10 rather than 14 which had changes in nodes evaluated when I tested it locally

