#!/usr/bin/env python
import hal, time, os
import sys
import linuxcnc
h = hal.component("TubeWAIT")
h.newpin("tube", hal.HAL_BIT, hal.HAL_IN)
h.newpin("machine-status", hal.HAL_BIT, hal.HAL_IN)
h.newpin("prog-run", hal.HAL_BIT, hal.HAL_IN)
h.ready()
clampFlag = False
unclampFlag = False
#setp Chuck.clamp true


while 1:
	time.sleep(0.1)
	if h['machine-status'] and not  h['prog-run']: 
		if h['tube']:
			os.system("halcmd loadusr TUBE_MOVE.py")
			time.sleep(0.6)
      
    
      
