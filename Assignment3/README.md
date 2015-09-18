# Assignment 3
###### A * path finding algorithms in python
## Heuristic Chosen
###### Euclidian
I choose the euclidian heuristic which is a more direct way to estimate the distance from your current position to the goal

Base Equation: a^2 + b^2 = c^2 (pythagorean theorem) then take square root of c^2 and c is the estimation from the goal

###### My Equation: 
```
product = pow(childNode.location[0], 2) + pow( (columns-1) - childNode.location[1], 2 ) //product is c^2 from aboove
ans = math.sqrt(product)  //ans is just c
childNode.heuristic = ans * 10 //multiply by 10 to get cost estimate from goal
```

###### Why Euclidian?

I figured that because euclidian is a straightline estimate and we can use diagonal moves euclidian would be an interesting change to the heuristic. The fact that it gives a direct estimate also made me believe that it would give a better result. It did give me slightly different answers which you will see in the section below. I was a little unsure as to whether I should multiply c from above by 10 or 14 above to due to what i described in the first sentence, but i did mess around with it and left it at 10.




