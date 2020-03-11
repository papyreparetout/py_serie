# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 22:18:44 2020

@author: pcjean
"""

import serial.tools.list_ports
ports = serial.tools.list_ports.comports(include_links=False)
#listport = [""]
nbport = 0
listport = []
for port, desc, hwid in sorted(ports):
    listport.append(port + " : "+ desc)
    nbport = nbport + 1
print(listport)