from lib.base.modules import *
import threading
import time, os
from apscheduler.scheduler import Scheduler
#from apscheduler.jobstores.shelve_store import ShelveJobStore
import logging
from lib.base.general import ConfigBaseReader, ConfigItemReader

def test(asd):
  print asd

class Sched(Basemodule):

  # ################################################################################
  # initialization of module and optional load of config files
  # ################################################################################
  def __init__(self, instance_queue, global_queue):
    #
    # "sched|port|command or action"
    #

    self.logger = logging.getLogger('Hasip.sched')
    self.sched = Scheduler()
    self.items  = ConfigItemReader()
    self.mod_list = self.items.get_items_dict()     # getting module list from item file
    self.queue_identifier = 'sched'       # this is the 'module address'  
    self.instance_queue = instance_queue  # worker queue to receive jobs 
    self.global_queue = global_queue      # queue to communicate back to main thread

    self.sched.start()

    self.jobs  = ConfigBaseReader('config/jobs/').get_values()
    sched_params={}
    for section in self.jobs:
      for item in self.jobs[section]:
        if self.jobs[section][item] != '':
          sched_params.update({item : self.jobs[section][item]})
        else:
          sched_params.update({item : None})
 
      
      self.sched.add_cron_job(self.send_msg,
        year   = sched_params['year'], 
        month  = sched_params['month'],
        day    = sched_params['day'],
        week   = sched_params['week'],
        day_of_week = sched_params['day_of_week'],
        hour   = sched_params['hour'],
        minute = sched_params['minute'],
        second = sched_params['second'],
        args=(sched_params['module'],sched_params['action']))

    
    self.logger.debug(self.sched.print_jobs())

  # @TODO loading jobs from persistent store and create them in the scheduler


  # ################################################################################
  # main thread of this module file which runs in background and constanly
  # checks working queue for new tasks. 
  # ################################################################################

  def worker(self):
    while True:
      instance_queue_element = self.instance_queue.get(True)

      _senderport = instance_queue_element.get("module_from_port")
      _sender	  = instance_queue_element.get("module_from")
      _port       = instance_queue_element.get("module_addr")
      _action     = instance_queue_element.get("cmd")
      _optargs    = instance_queue_element.get("opt_args")
      
      options = {
        "create"   : self.create,
        "delete"  : self.delete
      }
      options[_action](_sender, _senderport, _port, _optargs)

  # ################################################################################
  #
  # "private" methods from here on...
  #
  # ################################################################################

  def create(self, sender, senderport, port, optargs):
    # @TODO
    print "Function to put jobs in the running scheduler job queue and store them persistent"
    pass

  def delete(self, sender, senderport, port, optargs):
    # @TODO
    print "Function to delete running and persistent jobs"
    pass
  
  def send_msg(self, module, action):               # ########################################
    if module in self.mod_list.keys():              # checking existence of requested module
      rcpt = self.mod_list[module][0]               # setting receiving module from item file
      mid = self.mod_list[module][1]                # setting module id from item file
      msg = {                                       # creating queue message
        'module_from_port': 0,                      # ########################################
        'module_from':    'sched',
        'module_rcpt':    rcpt,
        'module_addr':    mid,
        'cmd':            action,
        'opt_args':       ''
      }                                                 
      self.global_queue.put(msg)


