#!/usr/bin/env python

import time
import Queue
import threading

from modules.cmddemo import Cmddemo
from hasip_base.configreaders import ConfigItemReader, ConfigBaseReader

class Hasip(object):
  # - load config
  #     |- bindings
  #     |- items
  #     |- mappings ( where is which item available )
  # - start: "hassip_messaging_bus"
  # - start: "scheduled_tasker"
  # - init logging (including level; and provide to all instances)
  # - command line args; demonize process; 
  def __init__(object):
    print "Main::__init__()"

  #
  # "run" is the main thread.
  # here we start all background threads for our modules:
  # => Where do we know which modules to load?
  # => Config Files (items)
  # Bellow is an example for static loading of the CMDModule
  def run(self):
    print "Main::run()"
    job_number = 0


    # loading all modules which are used in the config files
    # @TODO:
    #   * load each module which is mentioned within the config file (see: items config file) (idea: loop?)
    #   * create one queue for each model. name sugestion like: "$modelname_queue"
    #   * start thread for each module and provide two queues:
    #       - first queue:    Communication from MAIN   => to => MODULE. 
    #       - second queue:   Communication from MODULE => to => MAIN.    (can be the same for all modules, this queue is processed HERE) 


    # Example with "cmddemo"

    # init queues
    back_queue    = Queue.Queue()
    cmddemo_queue = Queue.Queue()

    # create object
    cmddemo = Cmddemo(cmddemo_queue, back_queue)

    # start "module" as thread in background
    t = threading.Thread(target=cmddemo.worker)
    t.daemon = True
    t.start()

    while 1:
      print "Main::run() # in loop now!"

      # So what are we doing here?
      #
      # - Checking "back_queue" for new jobs within this method.
      #   this is mainly shifting arround answers we get from threads to queues of other threads
      #
      #

      #if q.empty(): # wenn leer schicken wir mal ein paar jobs rein. :)
      #  print "Main::run() # queue is empty!"
      #  for i in range(0,3): # adding 4 jobs to working queue
      #    job_number += 1
      #    print "Main::run() # adding job to queue, no.: " + str(job_number)
      #    time.sleep(0.1)
      #    q.put(job_number)

      time.sleep(3)

#
# This starts the hole stuff ;)
#
if __name__ == '__main__':
  m = Hasip()
  m.run()
