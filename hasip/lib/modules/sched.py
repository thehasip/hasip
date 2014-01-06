from lib.base.modules import *
import threading
import time
from apscheduler.scheduler import Scheduler
import logging

class Sched():

  # ################################################################################
  # initialization of module and optional load of config files
  # ################################################################################
  def __init__(self, instance_queue, global_queue):
    #
    # "sched|port|command or action"
    #
    self.logger = logging.getLogger('Hasip.sched')
    self.sched = Scheduler()
    self.sched.start()
    self.queue_identifier = 'sched'       # this is the 'module address'  
    self.instance_queue = instance_queue  # worker queue to receive jobs 
    self.global_queue = global_queue      # queue to communicate back to main thread
    
    
    # @TODO loading jobs from persistent store and create them in the scheduler


  # ################################################################################
  # main thread of this module file which runs in background and constanly
  # checks working queue for new tasks. 
  # ################################################################################
  def worker(self):
    while True:
      if not self.instance_queue.empty():
        instance_queue_element = self.instance_queue.get()

        _action = instance_queue_element.get("cmd")
        _opt_args   = instance_queue_element.get("opt_args")

        options = {
          "create"   : self.create,
          "delete"  : self.delete
        }
        options[_action](_opt_args)

  # ################################################################################
  #
  # "private" methods from here on...
  #
  # ################################################################################

  def create(opt_args)
    # @TODO
    print "Function to put jobs in the running scheduler job queue and store them persistent"
    pass

  def delete(opt_args)
    # @TODO
    print "Function to delete running and persistent jobs"
    pass

