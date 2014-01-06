Rest Module
===================

General
-------

The rest module provides a webinterface to control other modules via URL calls. The module is loaded like other non standard modules, to be attached
to the main queue as it needs to exchange messages.
The module comes with single thread webserver that can be configured 
in the rest section of the base config file. 

```rest_service_ip``` specifies the ip the service should run on. You can also use localhost instead of the ip address. But then it only works locally ;)
```rest_service_port``` specifies the port the rest service should run on. Default should be 80.
```debug``` Don know the exact impact. But should stay on False.

To run the module the ```bottle``` library needs to be installed first.
Use one of the commands below to install bottle on your host.

$sudo pip install bottle              # recommended
$sudo easy_install bottle             # alternative without pip
$sudo apt-get install python-bottle   # works for debian, ubuntu, ...


Usage
---------

Currently only the base actions for switch classes are available.
```set_on```     sets the switch on
```set_off```    sets the switch off
```get_status``` queries the status of the switch

The rest module has no ports and no private methods as the only thing it does is to capture the answer of a status request. The correlate the answer of the status request to the original web request the  module name and the port of the target module need to be in the ```module_from``` part of message. 
e.g.: the answer of the GPIO module on port 3 need to have "gpio3" in the module_from part of the message. See the gpio module for further details.

The target modules can be controlled by using this URL once the main is started.
http://localhost/module/module/action
whereby "module" is the name used in the config item file and "action"
one of the three actions mentioned above.
e.g.: http://localhost/module/Pumpe1/set_on



