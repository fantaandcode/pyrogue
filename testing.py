#!/usr/bin/python
import time

p_Pos = [1, 1]	# Player position
lp_Pos = [1, 1]	# Last player position

def updateLastPos():
	#global lp_Pos
	lp = p_Pos
	lp_Pos = lp
	pass

def main_loop():
	while True:
		updateLastPos()
		lp_Pos = p_Pos
		p_Pos[0] += 1

		print('Old ' + str(lp_Pos))
		print('New ' + str(p_Pos))

		time.sleep(1)



main_loop()