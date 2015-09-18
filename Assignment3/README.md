# Assignment 3
###### A * path finding algorithms in python
## Heuristic Chosen
###### Euclidian
I choose the euclidian heuristic which is a more direct way to estimate the distance from your current position to the goal

Base Equation: a^2 + b^2 = c^2 (pythagorean theorem) then take square root of c^2 and c is the estimation from the goal

My Equation: 
'''
product = pow(childNode.location[0], 2) + pow( (columns-1) - childNode.location[1], 2 )
ans = math.sqrt(product)
childNode.heuristic = ans * 10
'''




