#!/usr/bin/python
import os

grid = []
p_Pos = [1, 1]	# Player position
lp_Pos = [1, 1]	# Last player position
gridH = 10
gridL = 10

messageLog = []

spacer = '=' * 40

# Can move?
cm_N = False
cm_E = False
cm_S = False
cm_W = False

class move:
	def moveNorth():
		if cm_N:
			p_Pos[0] -= 1
		else:
			messageLog.append('Cant move north')
	def moveEast():
		if cm_E:
			p_Pos[1] += 1
		else:
			messageLog.append('Cant move east')
	def moveSouth():
		if cm_S:
			p_Pos[0] += 1
		else:
			messageLog.append('Cant move south')
	def moveWest():
		if cm_W:
			p_Pos[1] -= 1
		else:
			messageLog.append('Cant move west')

	def canMove():
		global cm_N
		global cm_E
		global cm_S
		global cm_W

		if grid[p_Pos[0] - 1][p_Pos[1]] != 'w':	#check north
			cm_N = True
		else:
			cm_N = False

		if grid[p_Pos[0]][p_Pos[1] + 1] != 'w':	#check east
			cm_E = True
		else:
			cm_E = False

		if grid[p_Pos[0] + 1][p_Pos[1]] != 'w': #check south
			cm_S = True
		else:
			cm_S = False

		if grid[p_Pos[0]][p_Pos[1] - 1] != 'w': #check west
			cm_W = True
		else:
			cm_W = False

	def updateMap():
		grid[lp_Pos[0]][lp_Pos[1]] = '0'
		grid[p_Pos[0]][p_Pos[1]] = 'P'


def initGrid(height, length):
	for i in range(height):
		grid.append(['0'])
		for j in range(length - 1):
			grid[i].append('0')
	
	# Initialize the player's position
	grid[p_Pos[0]][p_Pos[1]] = 'P'

	# Initizlize walls
	for i in range(height):
		grid[i][0] = 'w'
		grid[i][length - 1] = 'w'
		for j in range(length - 1):
			if i == 0 or i == (length - 1):
				grid[i][j] = 'w'

def help():
	print('This is some example help text.')

def printMap():
	for row in grid:
		for tile in row:
			if tile == '0':
				print('  ', end = '')
			elif tile == 'w':
				print('██', end = '')
			elif tile == 'P':
				print('@ ', end = '')
		print()

def updateLastPos():
	global lp_Pos
	lp_Pos.pop()
	lp_Pos.pop()
	lp_Pos.append(p_Pos[0])
	lp_Pos.append(p_Pos[1])
	pass

def main_loop():
	while True:
		print(spacer)
		printMap()

		move.canMove()

		for message in messageLog:
			print(message)

		print(spacer)
		#print(p_Pos)
		#print(lp_Pos)
		#print(cm_N, cm_E, cm_S, cm_W)
		P = input('Command: ').upper()
		print(spacer)

		updateLastPos()

		if P == 'N':
			os.system('clear')
			move.moveNorth()
			move.updateMap()
		elif P == 'E':
			os.system('clear')
			move.moveEast()
			move.updateMap()
		elif P == 'S':
			os.system('clear')
			move.moveSouth()
			move.updateMap()
		elif P == 'W':
			os.system('clear')
			move.moveWest()
			move.updateMap()
		elif P == 'HELP' or P == '?':
			os.system('clear')
			help()
		elif P == 'EXIT':
			exit()
		else:
			os.system('clear')
			messageLog.append('invalid move, please input another direction')

def init():
	initGrid(gridH, gridL)
	os.system('clear')
	main_loop()

init()