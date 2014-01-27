import serial, io, time, logging, threading
from lib.base.modules import *
from lib.base.general import ConfigItemReader

class Cul(Basemodule):

  # ################################################################################
  # initialization of module and optional load of config files
  # ################################################################################
  def __init__(self, instance_queue, global_queue):

    self.logger = logging.getLogger('Hasip.cul')
    self.queue_identifier = 'cul'     # this is the 'module address'  
    self.instance_queue = instance_queue  # worker queue to receive jobs 
    self.global_queue = global_queue      # queue to communicate back to main thread
    self.items  = ConfigItemReader()      # config item reader

  # ##########################################################################
  # Uncomment this block below on a prepared pi --> wheezy - fhem installation
  # and uncomment the 3 lines in the functions below.
  # refer to cul.md for detailed description
  # ##########################################################################  

  #  self.serial = serial.Serial('/dev/ttyAMA0', 38400) # connects to the serial adapter created by the FHEM setup for CUL
  #  self.sio = io.TextIOWrapper(io.BufferedRWPair(self.serial, self.serial)) # creates read write buffer for data exchange with the serial connection
  #  data='X21'                           # Sends the "X21" command to the cul to receive radio messages
  #  self.sio.write(unicode(data+'\n'))   # write the command + address + escape sequence to buffer
  #  self.sio.flush()                     # get the data out *now*

    self.ports = [                        # internal port names
      { 
        'id'      : 0,
        'type'    : 'FS20',
        'address' : 'F1B1B00',
        'status'  : 'off'

      }] # defining internal ports here (...)

    self.tx_addr = [
      {
        'addr'    : 'F1B1BBA00',
        'module'  : 'Pumpe1',
        'action'  : 'set_off'
      }, {
        'addr'    : 'F1B1BBA11',
        'module'  : 'Pumpe1',
        'action'  : 'set_on'
      }]


  # ################################################################################
  # main thread of this module file which runs in background and constanly
  # checks working queue for new tasks. 
  # ################################################################################
  def worker(self):
    t = threading.Thread(target=lambda: self.listen())
    t.daemon = True
    t.start()


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
  #    self.sio.write(unicode(data+'\n'))   # write the command + address + escape sequence to buffer
  #    self.sio.flush()                     # get the data out *now*
  #    self.ports[port]['status']='on'       # set internal port status
      self.logger.debug("CUL Port (" + str(port) + ") set to on")
    else:
      self.logger.error('Port "'+ str(port) + '" doesn\'t exist!')

  def set_off(self,port,sender):
    if port != None:
      data=self.ports[port]['address']+'00' # get the FS20 address of module + FS20 command "off"
  #    self.sio.write(unicode(data+'\n'))   # write the command + address + escape sequence to buffer
  #    self.sio.flush()                     # get the data out *now*
  #    self.ports[port]['status']='off'       # set internal port status
      self.logger.debug("CUL Port (" + str(port) + ") set to off")
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

  def listen(self):
    print 'Dummy line'
   # while True:
   #   buffer = self.serial.readline()
   #   if buffer != '':
   #     self.logger.debug('Received message from cul: ' + str(buffer))
   #     tmp = buffer[:9]
   #     for dict in self.tx_addr:
   #       if dict['addr'] == tmp:
   #         self.send_msg(dict['module'],dict['action'])
      
  def send_msg(self, module, action):               # ########################################
    mod_list = self.items.get_items_dict() 
    if module in mod_list.keys():              # checking existence of requested module
      rcpt = mod_list[module][0]               # setting receiving module from item file
      mid = mod_list[module][1]                # setting module id from item file
      msg = {                                       # creating queue message
        'module_from':    'cul',                  # ########################################
        'module_rcpt':    rcpt,
        'module_addr':    mid,
        'cmd':            action,
        'opt_args':       ''
      }                                                 
      self.global_queue.put(msg)     




