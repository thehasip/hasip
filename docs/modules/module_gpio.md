GPIO Module
===================

General
-------

The gpio module is used to control the GPIO pins of the raspberry pi directly. Please make sure that your connected circuit works correctly
and uses the correct pins in correct modes to avoid damage to you circuit or the pi.
The pi specific code lines are commented to test the module on a normal machine.
Please uncomment them before using the module on a pi.

The ports dictionary contains 16 IO ports which can be set to "IN" or "OUT" and "HIGH" or "LOW"
The internal port numbering starts at 0 and ends at 15 and are mapped to the physical pins.
You can change the mapping by editing the ports dictionary.
Please see references section for a link with the ports.

The gpio module inherits from the switch class. So it has the 3 basic switch classes (set_on, set_off, get_status) implemented.

If not already installed you can install the RPi.GPIO library manually. 
There is a link in the references section.


Port mappings

internal ID        physical port
	0		3
	1		5
	2		7
	3		8
	4		10
	5		11
	6		12
	7		13
	8		15
	9		16
	10		18
	11		19
	12		21
	13		22
	14		23
	15		24
	16		26

Usage
---------

Only the base actions for switch classes are available.
```set_on```     sets the switch on
```set_off```    sets the switch off
```get_status``` queries the status of the switch

Create an item in the item file with the respective port and "gpio" as module. And finished!
Use the rest module to switch the item off, on and to get the current status.
e.g.: http://localhost/module/Pumpe1/set_on

References
---------
http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/cheat_sheet/
https://pypi.python.org/pypi/RPi.GPIO

