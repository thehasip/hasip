from lib.base.modules import *
import RPi.GPIO
import time

class Gpio(Basemodule, Switch):

  # ################################################################################
  # initialization of module and optional load of config files
  # ################################################################################
  def __init__(self, instance_queue, global_queue):
    #
    # "gpio|port|command or action"
    #
    #self.GPIO = RPi.GPIO
    #self.GPIO.setmode(self.GPIO.BOARD)
    self.queue_identifier = 'gpio'       # this is the 'module address'  
    self.instance_queue = instance_queue  # worker queue to receive jobs 
    self.global_queue = global_queue      # queue to communicate back to main thread
    self.ports = [                        # internal port names
      { 
        'id'      : 0,
        'status'  : 'off',
        'pin'     : 3,
        'mode'    : 'out'
      }, { 
        'id'      : 1,
        'status'  : 'off',
        'pin'     : 5,
        'mode'    : 'out'
      }, {
        'id'      : 2,
        'status'  : 'off',
        'pin'     : 7,
        'mode'    : 'out'
      }, {
        'id'      : 3,
        'status'  : 'off',
        'pin'     : 8,
        'mode'    : 'out'
      }, {} ] # defining internal ports here (...)


  # ################################################################################
  # main thread of this module file which runs in background and constanly
  # checks working queue for new tasks. 
  # ################################################################################
  def worker(self):
    while True:
      if not self.instance_queue.empty():
        instance_queue_element = self.instance_queue.get()

        _action = instance_queue_element.get("cmd")
        _port   = instance_queue_element.get("module_id")

        options = {
          "get_status"    : self.get_status,
          "set_on"    : self.set_on,
          "set_off"   : self.set_off
        }
        options[_action](_port)

  # ################################################################################
  #
  # "private" methods from here on...
  #
  # ################################################################################

  # ################################################################################
  # shows status of port provided by argument
  #e
  # @arguments:  port
  # @return:     -
  # ################################################################################
  def get_status(self, port):
     print "GPIO :: status(" + str(port) + ") => " + self.ports[port]['status']
     pass

  # ################################################################################
  # sets the port provided by @argument to on
  #
  # @arguments:  port
  # @return:     -
  # ################################################################################
  def set_on(self, port):
    self.ports[port]['status'] = 'on'
    if self.ports[port]['mode'] == 'out':
#      self.GPIO.setup(self.ports[port]['pin'], self.GPIO.OUT)
#     self.GPIO.output(self.ports[port]['pin'], self.GPIO.HIGH)
      print 'Hello'
    if self.ports[port]['mode'] == 'in':
#      self.GPIO.setup(self.ports[port]['pin'], self.GPIO.IN)
       print 'Hello'
    print "GPIO :: set_on(" + str(port) + ")"

  # ################################################################################
  # sets the port provided by @agrument to off
  #
  # @arguments:  port
  # @return:     -
  # ################################################################################
  def set_off(self, port):
    self.ports[port]['status'] = 'off'
    if self.ports[port]['mode'] == 'out':
 #     self.GPIO.setup(self.ports[port]['pin'], self.GPIO.OUT)
 #     self.GPIO.output(self.ports[port]['pin'], self.GPIO.LOW)
      print 'Hello'
    if self.ports[port]['mode'] == 'in':
 #     self.GPIO.setup(self.ports[port]['pin'], self.GPIO.IN)
      print 'Hello'
    print "GPIO :: set_off(" + str(port) + ")"



#
# main for testing
#
#if __name__ == '__main__':
#  import Queue
#  q = Queue.Queue()
#  h = Gpio(q,q)
#  h.set_on(0)
#  h.get_status(0)
#  time.sleep(10)
#  h.set_off(0)
#  h.get_status(0)
#  h.worker()
