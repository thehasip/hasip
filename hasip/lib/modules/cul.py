import serial, io, time, logging
from lib.base.modules import *

class Cul(Basemodule):

  # ################################################################################
  # initialization of module and optional load of config files
  # ################################################################################
  def __init__(self, instance_queue, global_queue):

    self.logger = logging.getLogger('Hasip.cul')
    self.queue_identifier = 'cul'     # this is the 'module address'  
    self.instance_queue = instance_queue  # worker queue to receive jobs 
    self.global_queue = global_queue      # queue to communicate back to main thread

  # ##########################################################################
  # Uncomment this block below on a prepared pi --> wheezy - fhem installation
  # and uncomment the 3 lines in the functions below.
  # refer to cul.md for detailed description
  # ##########################################################################  

  #  self.serial = serial.Serial('/dev/ttyAMA0', 38400, timeout=1) # connects to the serial adapter created by the FHEM setup for CUL
  #  self.serial.open() # opens the serial connection
  #  self.sio = io.TextIOWrapper(io.BufferedRWPair(self.serial, self.serial)) # creates read write buffer for data exchange with the serial connection

    self.ports = [                        # internal port names
      { 
        'id'      : 0,
        'type'    : 'FS20',
        'address' : 'F1B1B00',
        'status'  : 'off'

      }] # defining internal ports here (...)


  # ################################################################################
  # main thread of this module file which runs in background and constanly
  # checks working queue for new tasks. 
  # ################################################################################
  def worker(self):
    while True:

        instance_queue_element = self.instance_queue.get(True)

        _action = instance_queue_element.get("cmd")
        _port   = instance_queue_element.get("module_addr")
        _sender = instance_queue_element.get("module_from")

        options = {
          "set_on"    : self.set_on,
          "set_off"   : self.set_off,
          "get_status": self.get_status
        }
        options[_action](_port,_sender)

  # ################################################################################
  #
  # "private" methods from here on...
  #
  # ################################################################################

  def set_on(self,port,sender):
    if port != None:
      data=self.ports[port]['address']+'01' # get the FS20 address of module + FS20 command "on"
#      self.sio.write(unicode(data+'\n'))   # write the command + address + escape sequence to buffer
#      self.sio.flush()                     # get the data out *now*
#      buffer = self.sio.readline()         # catching answer from cul module if available. Not used atm.
      self.ports[port]['status']='on'       # set internal port status
      self.logger.debug('Sent message ' + data + ' to CUL')
    else:
      self.logger.error('Port "'+ str(port) + '" doesn\'t exist!')

  def set_off(self,port,sender):
    if port != None:
      data=self.ports[port]['address']+'00' # get the FS20 address of module + FS20 command "off"
#      self.sio.write(unicode(data+'\n'))   # write the command + address + escape sequence to buffer
#      self.sio.flush()                     # get the data out *now*
#      buffer = self.sio.readline()         # catching answer from cul module if available. Not used atm.
      self.ports[port]['status']='off'       # set internal port status
      self.logger.debug('Sent message ' + data + ' to CUL')
    else:
      self.logger.error('Port "'+ str(port) + '" doesn\'t exist!')

  def get_status(self, port, sender):
    if port != None and sender != None:
      args=str(self.ports[port]['status'])
      queue_msg = {
        'module_from':  self.queue_identifier + str(port),
        'module_rcpt':  sender,
        'module_addr':    0,
        'cmd':          'reply',
        'opt_args':     args
      }
      self.global_queue.put(queue_msg)
    else:
      self.logger.error('Port "'+ str(port) + '" or sender "' + str(sender) + '" doesn\'t exist!')

