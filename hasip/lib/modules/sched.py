from lib.base.modules import *
import threading
import time
from apscheduler.scheduler import Scheduler


class Sched():

  # ################################################################################
  # initialization of module and optional load of config files
  # ################################################################################
  def __init__(self, instance_queue, global_queue):
    #
    # "sched|port|command or action"
    #

    self.sched = Scheduler()
    self.sched.start()
    self.queue_identifier = 'sched'       # this is the 'module address'  
    self.instance_queue = instance_queue  # worker queue to receive jobs 
    self.global_queue = global_queue      # queue to communicate back to main thread
    self.ports = [                        # internal port names
      { 
        'id'      : 0,
        'status'  : 'on'
      }, { 
        'id'      : 1,
        'type'    : 'pump',
        'status'  : 'off'
      }, {}, {}, {} ] # defining internal ports here (...)

    
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
          "set_off"   : self.set_off,
          "pumptest"  : self.pumptest
        }
        options[_action](_port)

  # ################################################################################
  #
  # "private" methods from here on...
  #
  # ################################################################################

  
  # ################################################################################
  # sets the port provided by @agrument to off
  #
  # @arguments:  port
  # @return:     -
  # ################################################################################
  def set_off(self, port):
    self.ports[port]['status'] = 'off'
    self.sched.stop()
    print "Scheduler :: set_off(" + str(port) + ")"

  # ################################################################################
  # Testing method to switch pump off and on for Demonstration purpose
  # sets a interval scheduler that switches off the GPIO pin 3 off and on via the
  # GPIO module. Pump should be attached to that port.
  # @arguments:  port
  # @return:     -
  # ################################################################################
  def pumptest(self, port):
    print "Pumptest started"
    
    queue_msg_start = {
        'module':       'gpio',
        'module_id':    0,
        'cmd':          'set_on',
        'opt_args':     ''
    }
    queue_msg_stop = {
        'module':       'gpio',
        'module_id':    0,
        'cmd':          'set_off',
        'opt_args':     ''
    }

    start = self.global_queue.put(queue_msg_start)
    stop = self.global_queue.put(queue_msg_stop)
    self.sched.add_interval_job(lambda: start, minutes=0.2)
    self.sched.add_interval_job(lambda: stop, minutes=0.05)
    print "Pumptest stopped"

#
# main for testing
#
#if __name__ == '__main__':
#  import Queue
#  q = Queue.Queue()
#  h = Sched(q,q)
#  h.pumptest(0)
#  
# h.worker()
