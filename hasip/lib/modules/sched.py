from lib.base.modules import *
import threading
import time, os
#from apscheduler.scheduler import Scheduler
#from apscheduler.jobstores.shelve_store import ShelveJobStore
import logging
from lib.base.general import ConfigBaseReader



class Sched(Basemodule):

  # ################################################################################
  # initialization of module and optional load of config files
  # ################################################################################
  def __init__(self, instance_queue, global_queue):
    #
    # "sched|port|command or action"
    #

    self.path = os.path.join(os.path.join( os.getcwd() + "/tmp/dbfile"))
    self.logger = logging.getLogger('Hasip.sched')
    self.logger.debug(self.path)
    #self.sched = Scheduler()
    #self.sched.add_jobstore(ShelveJobStore(self.path), 'default')
    
    self.queue_identifier = 'sched'       # this is the 'module address'  
    self.instance_queue = instance_queue  # worker queue to receive jobs 
    self.global_queue = global_queue      # queue to communicate back to main thread



    #self.jobs  = ConfigBaseReader('config/jobs/').get_values()
    #sched_params={}
    #for section in self.jobs:
    #  for item in self.jobs[section]:
    #    if self.jobs[section][item] != '':
    #      sched_params.update({item : self.jobs[section][item]})
    #    else:
    #      sched_params.update({item : None})
    #    #self.logger.debug(sched_params)
    #
    #  self.sched.add_cron_job(lambda: self.send_msg(sched_params['module'],sched_params['action']),
    #    year   = sched_params['year'], 
    #    month  = sched_params['month'],
    #    day    = sched_params['day'],
    #    week   = sched_params['week'],
    #    day_of_week = sched_params['day_of_week'],
    #    hour   = sched_params['hour'],
    #    minute = sched_params['minute'],
    #    second = sched_params['second'])


    #self.sched.add_cron_job(self.test,second='1,10,20')
    #self.sched.add_cron_job(test,second='5,15,25')
    #self.sched.start()
    #self.logger.debug(self.sched.print_jobs())

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

  def create(self, opt_args):
    # @TODO
    print "Function to put jobs in the running scheduler job queue and store them persistent"
    pass

  def delete(self, opt_args):
    # @TODO
    print "Function to delete running and persistent jobs"
    pass
  
  def send_msg(self, module, action):
    self.logger.debug(module + ' & ' + action)


