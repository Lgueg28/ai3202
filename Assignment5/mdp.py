import sys
import math
import numpy as np
import copy
	
def traverseMarkov(maze, e):
	
	rows = len(maze)
	columns = len(maze[0])
	utilityMatrix = np.zeros((rows,columns))
	openNodes = []
	
	#initialize utility matrix
	for i in range(0, rows):
		for j in range(columns-1, -1, -1):
			if (maze[i][j] == 0):
				utilityMatrix[i][j] = 0
				openNodes.append([i, j]) 
			elif (maze[i][j] == 1):
				utilityMatrix[i][j] = -1
				openNodes.append([i, j])
			elif (maze[i][j] == 2):
				utilityMatrix[i][j] = 0
			elif (maze[i][j] == 3):
				utilityMatrix[i][j] = -2
				openNodes.append([i, j])
			elif (maze[i][j] == 4):
				utilityMatrix[i][j] = 1
				openNodes.append([i, j])
			elif (maze[i][j] == 50):
				utilityMatrix[i][j] = 50
		
	ret = iterateMarkov(utilityMatrix, e, openNodes, rows, columns)
	printMatrixPath(ret[0], ret[1])	

def iterateMarkov(utilityMatrix, e, openNodes, rows, columns):		
	resultMatrix = copy.deepcopy(utilityMatrix)
	movesMatrix = np.full([rows, columns], 'n',  dtype=str)
	endIter = float(e) * ((1-.9)/.9)
	cont = True
	 
	#MDP Iterator
	while (cont):
		maxChange = 0
		for node in openNodes:
			originalValue = utilityMatrix[node[0]][node[1]]
			
			#these if statements check if we are at the edge of the map
			leftVal = 0
			if (node[1] != 0):
				leftVal = utilityMatrix[node[0]][node[1]-1]
			left2Val = 0
			if (node[1] != 0 and node[1] != 2):
				left2Val = utilityMatrix[node[0]][node[1]-2]	 
			rightVal = 0
			if (node[1] != (columns-1)):
				rightVal = utilityMatrix[node[0]][node[1]+1]
			right2Val = 0
			if (node[1] != (columns-1) and node[1] != (columns-2)):
				right2Val = utilityMatrix[node[0]][node[1]+2]
			upVal = 0
			if (node[0] != 0):
				upVal = utilityMatrix[node[0]-1][node[1]]
			downVal = 0
			if (node[0] != (rows-1)):
				downVal = utilityMatrix[node[0]+1][node[1]]
			
			#Evaluate left, right, up, down moves
			left = (.8 * leftVal) + (.1 * left2Val) + (.1 * originalValue)  
			right = (.8 *  rightVal) + (.1 * right2Val) + (.1 * originalValue)
			up = (.8 * upVal) + (.1 * leftVal) + (.1 * rightVal)
			down = (.8 * downVal) + (.1 * leftVal) + (.1 * rightVal)
			
			d = {"l": left, "r": right, "u": up, "d": down}  
			movesMatrix[node[0]][node[1]] = max(d, key=d.get) 
			#compute new utility
			result = resultMatrix[node[0]][node[1]] + (.9 * max(left, right, up, down))
			
			#check if there is a new max change
			if (abs(result-originalValue) > maxChange):
				maxChange = abs(result-originalValue) 
			utilityMatrix[node[0]][node[1]] = result
		
		#terminating condition of while
		if (maxChange < endIter):
			cont = False

	return [utilityMatrix, movesMatrix]

def printMatrixPath(matrix, moves):
	print "Maze with  Utilities"
	print "-------------------------"
	for x in range(0, len(matrix)):
		for y in range(0, len(matrix[0])):
			print("{:6}".format("{0:.2f}".format(matrix[x][y])) + " "),
		print ""
	row = len(matrix) - 1
	column = 0
	print ""
	print "Path Through Maze:"
	print "---------------------"
	while (True):
		print "Node: [" + str(row) + ", " + str(column) + "] " + "Utility: " + "{0:.2f}".format(matrix[row][column])	
		if (row == 0 and column == (len(matrix[0])-1)):
			break
		if (moves[row][column] == 'u'):
			row = row - 1			
		if (moves[row][column] == 'r'):
			column = column + 1
		if (moves[row][column] == 'l'):
			column = column - 1
		if (moves[row][column] == 'd'):
			row = row + 1

def main():
	
	print ""
	print "Evaluating solution for: " + sys.argv[1]
	print ""
	#read the matrix specified on the command line
	with open(sys.argv[1]) as f:
		inputMaze = [[int(x) for x in line.split()] for line in f]
	#make sure there are two args to function
	if (len(sys.argv) != 3): 
		print "Program should have two inputs (txt file representing world and epsilon) Ex. mdp.py WorldN.txt .5"
	#print sys.argv[2]
	traverseMarkov(inputMaze, sys.argv[2])

if __name__ == "__main__":
	main()
