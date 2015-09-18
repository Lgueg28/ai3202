import sys
import math

#class that stores global arrays
class nodesList: 
	def __init__(self):
		self.openNodes = []
		self.closedNodes = []
		self.nodesEvaluated = [[0, 0]]

#class that constructs maze nodes as we iterate through maze
class mazeNode:
	def __init__(self): 
		self.location = [0, 0]
		self.distanceToStart = 0
		self.heuristic = 0
		self.f = 0
		self.parent = None
	
def traverseManhattan(maze):
	rows = len(maze)
	columns = len(maze[0])
	nodes = nodesList()
	startNode = mazeNode()
	startNode.location = [rows - 1, 0]

	nodes.openNodes.append(startNode)

	(boolean, ret) = getAdajcentCells(nodes, maze, startNode, rows, columns)

	#delete start node from openNodes
	if startNode in nodes.openNodes:
		nodes.openNodes.remove(startNode)
		nodes.closedNodes.append(startNode)
	
	#evaluate rest of the nodes, find min of open and evaluate adajcent nodes
	while ( (not boolean) and ( len(nodes.openNodes) != 0) ):
		minIndex = -1
		minVal = 1000000000
		for i in range(0, len(nodes.openNodes)):
			#new min if comparison passes
			if (nodes.openNodes[i].f <= minVal):
				minVal = nodes.openNodes[i].f
				minIndex = i
		
		#close min node
		tempNode = nodes.openNodes[minIndex]
		if tempNode in nodes.openNodes:
			nodes.openNodes.remove(tempNode)
			nodes.closedNodes.append(tempNode)		
		
		#get min nodes nieghbors
		(boolean, ret) = getAdajcentCells(nodes, maze, tempNode, rows, columns) 	
	
	#see if we have a solution
	if (boolean):
		print ""
		print "Solution Found!!!"
		print "----------------------------------------------------------"
		print "Cost of Path: " + str(ret.distanceToStart)
		print "# of Nodes evaluated: " + str( len(nodes.nodesEvaluated) )
		sys.stdout.write("Starting from the end: " + str(ret.location))
		tempParent = ret.parent
		while ( tempParent != None ):
			sys.stdout.write(", ")
			sys.stdout.write(str(tempParent.location))
			tempParent = tempParent.parent
		print ""
		print ""
	else:
		print ""
		print "Solution Not Found!!!!!"
		print ""

def getAdajcentCells(nodes, maze, parentNode, rows, columns):
	for i in range(-1, 2):
		for j in range (-1, 2):
			#dont evaluate self
			if ( j != 0 or i != 0):
				#check if node is within our bounds
				if ( (0 <= parentNode.location[0] + i < rows) and (0 <= parentNode.location[1] + j < columns ) ):
					#check if node has not been evaluated, if not add to evaluated location array
					if [parentNode.location[0] + i, parentNode.location[1] + j] not in nodes.nodesEvaluated:
						nodes.nodesEvaluated.append([parentNode.location[0] + i, parentNode.location[1]])
					#check if node is not a wall
					if ( maze[parentNode.location[0] + i][parentNode.location[1] + j] != 2 ):
						
						#check if node is closed
						for closedNode in nodes.closedNodes:
							if (closedNode.location == [parentNode.location[0] + i, parentNode.location[1] + j] ):
								continue
						
						#check if node is open
						foundOpenNode = False
						for openNode in nodes.openNodes:
							if (openNode.location == [parentNode.location[0] + i, parentNode.location[1] + j] ):
								foundOpenNode = True
								#if shorter path to node update the openNode's info
								if ( openNode.parent.distanceToStart > parentNode.distanceToStart ):
									openNode.parent = parentNode
									if ( i != 0 and j != 0):
                        			                                distance = 14
                	                        		        else:
        	                                              			distance = 10
									if ( maze[openNode.location[0]][openNode.location[1]] == 1 ):
                		        	                        	openNode.distanceToStart = parentNode.distanceToStart + distance + 10
        	                	        	                else:
                                                       				openNode.distanceToStart = parentNode.distanceToStart + distance
									openNode.f = openNode.distanceToStart + openNode.heuristic
									break	

						#if open do not add again
						if (foundOpenNode):
							continue
						
						#if valid and not closed or open create new node 
						childNode = mazeNode()
						#set location array
						childNode.location = [parentNode.location[0] + i, parentNode.location[1] + j]
						#set parent pointer
						childNode.parent = parentNode
						#check if diagonal
						if ( i != 0 and j != 0):
							distance = 14
						else:
							distance = 10
						#check if Mountain
						if ( maze[childNode.location[0]][childNode.location[1]] == 1 ):
							childNode.distanceToStart = parentNode.distanceToStart + distance + 10
						else:
							childNode.distanceToStart = parentNode.distanceToStart + distance
						#Heuristic Cases (manhattan or euclidian)
						if (sys.argv[2] == "m"): 	
							childNode.heuristic = ( childNode.location[0] + ( (columns-1) - childNode.location[1] ) ) * 10
						elif (sys.argv[2] == "e"):
							product = pow(childNode.location[0], 2) + pow( (columns-1) - childNode.location[1], 2 )
							ans = math.sqrt(product) 
							childNode.heuristic = ans * 10
						#Calculate F (G + H)
						childNode.f = childNode.distanceToStart + childNode.heuristic
						#terminating case based on our graph layouts
						if (childNode.location == [0, columns - 1] ):
							return (True, childNode)
						#Append child node to open nodes
						nodes.openNodes.append(childNode)
	#target node not found
	return (False, None)

def main():
	
	print ""
	print "Evaluating solution for: " + sys.argv[1]

	#read the matrix specified on the command line
	with open(sys.argv[1]) as f:
		inputMaze = [[int(x) for x in line.split()] for line in f]
	#make sure there are two args to function
	if (len(sys.argv) < 3): 
		print "Program should have two inputs (txt file and heuristic flag) Ex. aStar.py WorldN.txt (m or e)"
	#check for valid heuristic flag
	elif (sys.argv[2] == "m" or sys.argv[2] == "e"):
		traverseManhattan(inputMaze)

if __name__ == "__main__":
	main()
