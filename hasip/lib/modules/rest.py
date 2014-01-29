from lib.base.modules import *
from bottle import route, run
from lib.base.general import ConfigItemReader, ConfigBaseReader
import time
import logging
import threading

class Rest(Basemodule):

  # ################################################################################
  # initialization of module and optional load of config files
  # ################################################################################
  def __init__(self, instance_queue, global_queue):

    self.logger = logging.getLogger('Hasip.rest')
    self.queue_identifier = 'rest'        # this is the 'module address'  
    self.instance_queue = instance_queue  # worker queue to receive jobs 
    self.global_queue = global_queue      # queue to communicate back to main thread
    self.items  = ConfigItemReader()      # config item reader
    self.config = ConfigBaseReader().get_values() # base config reader
    self.reply_cache={}                   # cache dictionary for catching replies to status requests of modules
 
    # ################################################################################
    # This method is for controlling all modules that are based on the switch template.
    # Only actions that are supported by the target module can be taken.
    # Takes the variables 'modname' and 'action' from the URL call and creates
    # a queue message out of it and sends it to the respective module. 
    # In case the "get_status" action has been called the method waits for an answer of
    # the asked module and returns the payload from the "opt_args" part of the answer.
    #
    # Note: To get a match for the answer the replying module need fill out the "module_from"
    #       parameter with its own name including port!!!!  e.g. gpio1
    #
    # @return:     command confirmation or payload of "opt_args" from response in cas of "get_status".
    # ################################################################################

   
    @route('/module/<module>/<action>')
    def rest_switch_modules(module, action):     # ########################################
      mod_list = self.items.get_items_dict()     # getting module list from item file
      if module in mod_list.keys():              # checking existence of requested module
        rcpt = mod_list[module][0]               # setting receiving module from item file
        mid = mod_list[module][1]                # setting module id from item file
        msg = {                                  # creating queue message
          'module_from_port':  0,                # ########################################
          'module_from':    'rest',
          'module_rcpt':    rcpt,
          'module_addr':    mid,
          'cmd':            action,
          'opt_args':       ''
        }                                                   # #################################################################
        self.global_queue.put(msg)                          # sending message to global queue
        if action == 'get_status':                          # checking if requested action was "get_status"
          esc = 0
          self.logger.debug("Waiting for module answer")
          while not (rcpt + str(mid) in self.reply_cache.keys()): # waiting until target module answer appears in worker queue
            time.sleep(0.05)                               # small break
            esc = esc+1
            if esc == 20:
              self.logger.error('No answer from module ' + str(rcpt) + ' received!')
              return 'Error: No status from module ' + str(module) + ' received!'
          self.logger.debug("Module answer received")       #
          val = self.reply_cache[rcpt + str(mid)]           # storing answer from target
          del self.reply_cache[rcpt + str(mid)]             # removing answer from reply_cache
          return module + " is " + val                      # returning module status
        elif action == 'set_on' or action == 'set_off':     # checking if if action was "set_on" or "set_off"
          return "Done"                                     # Placeholder for frontend. Command confirmation.
        else:                                               #
          return "Action not supported"                     # No supported command has been used
      return "No module named " + module                    # Module was not in the item file
                                                            # #################################################################

    

  # ################################################################################
  # main thread of this module file which runs in background and constanly
  # checks working queue for new tasks. 
  # ################################################################################
  def worker(self):
    
    # ##############################################################################
    # Starting rest webserver in own thread otherwise it will block the 
    # whole application
    # ##############################################################################

    t = threading.Thread(target=lambda: run(host=str(self.config['rest']['rest_service_ip']), 
      port=self.config['rest']['rest_service_port'], 
      debug=self.config['rest']['debug']))

    t.daemon = True
    t.start()
     
    while True:
      instance_queue_element = self.instance_queue.get(True)
      _senderport = instance_queue_element.get("module_from_port")
      _sender	  = instance_queue_element.get("module_from")
      _port       = instance_queue_element.get("module_addr")
      _action     = instance_queue_element.get("cmd")
      _optargs    = instance_queue_element.get("opt_args")

      self.reply_cache[_sender+str(_senderport)] = _optargs 
     
  # ################################################################################
  #
  # "private" methods from here on...
  #
  # ################################################################################


  

  


