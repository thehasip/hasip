Cul Module
===================

General
-------

Currently the cul can be only used when running the rasperian image wheezy from fhem available on the busware.de page as there are some kernel 
modifications necessary to run it.
http://files.busware.de/RPi/README.raspbian
The cul then will be set up the FHEM installation and the serial port /dev/ttyAMA0 will be created which is used in this module for the basic communication of the module. This is not the clean method but it works.

The cul module provides basic communication with FS20 components via the COC module from Busware.de that can be attached to the raspberry pi.
The cul will be mainly controlled by the rest module. Therefore it has the 3 switch classes "set_on", "set_off" and "get_status" implemented.
You can use the cul module as every other module that is attached to queue system. Just define an item in the item file and select the cul as module. The module address need to be set in the cul module first. In the ports dictionary define a new port with the respective FS20 address.
Keep in mind that the address is not in the decimal system. The decimal module address need to be calculated first by using the table below.

Like in GPIO module the pi specific code is commented to test it on a "normal" machine. Please do not forget to uncomment it before using.


Calculating the module address:
e.g. house code = 12341234 and the group and module code is 11 11
Then the address of the FS20 module would be 1B1B00.
 1x quad 	2x quad 	3x quad 	4x quad
11 = 0x0 	12 = 0x1 	13 = 0x2 	14 = 0x3
21 = 0x4 	22 = 0x5 	23 = 0x6 	24 = 0x7
31 = 0x8 	32 = 0x9 	33 = 0xA 	34 = 0xB
41 = 0xC 	42 = 0xD 	43 = 0xE 	44 = 0xF 



To run the module the ```pyserial``` library needs to be installed first.
Use the commands below to install pyserial on your host.

$sudo pip install pyserial              # recommended


Usage
---------

Currently only the base actions for switch classes are available.
```set_on```     sends the on command (01) to the FS20 module address
```set_off```    sends the on command (00) to the FS20 module address
```get_status``` queries the status of the switch which is stored in the ports dictionary

Define a port in the ports dictionary in the cul.py and calculate the address of the module you want to control.
DO NOT FORGET to add the "F" in front of the module address. It is necessary for the coc to send it as an FS20 message.
Then create an item in the item file with the created port and "cul" as module. And finished!
Use the rest module to switch the item off, on and to get the current status.
http://pi_IP/module/item/operation


References
---------
http://busware.de/tiki-index.php?page=COC
http://www.fhemwiki.de/wiki/FS20_Allgemein
http://fhz4linux.info/tiki-index.php?page=FS20%20Protocol
http://pyserial.sourceforge.net/





