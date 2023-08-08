#!/usr/bin/env python
import hal, time, os
import sys
import linuxcnc
h = hal.component("X-axis-auto-scale")
h.newpin("in", hal.HAL_BIT, hal.HAL_IN)
h.newpin("MachineIsON", hal.HAL_BIT, hal.HAL_IN)
h.newpin("MachineON", hal.HAL_BIT, hal.HAL_OUT)
h.newpin("MachineOFF", hal.HAL_BIT, hal.HAL_OUT)
h.ready()

PowerFlag = False


inifilePath = os.environ['HOME'] +"/linuxcnc/configs/Plasma/Plasma++.ini"
inifile = linuxcnc.ini(inifilePath)
SCALE_PORTAL = inifile.find("JOINT_0", "SCALE_PORTAL") or "unknown"
SCALE_TUBE = inifile.find("JOINT_0", "SCALE_TUBE") or "unknown"


while 1:
	time.sleep(0.25)
	if PowerFlag != h['in']:
		MachineOFF = True
		time.sleep(0.25)
		MachineOFF = False
		if h['in']:
			os.system("halcmd setp stepgen.0.position-scale {}".format(SCALE_TUBE))
			time.sleep(1)
			MachineON = True
			time.sleep(0.5)
			MachineON = False
		else:
			os.system("halcmd setp stepgen.0.position-scale {}".format(SCALE_PORTAL))
			time.sleep(1)
			MachineON = True
			time.sleep(0.5)
			MachineON = False
     
	PowerFlag = h['in']
