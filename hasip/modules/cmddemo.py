#from ...hasip_base.switch import Switch


# @TODO:
# should be ==>
#   class Cmddemo(Switch)
#   class Cmddemo(Switch, Dimmer, ... )
# ^^ whatever this module should do... (ensures that standard methods are implemented!)
#

class Cmddemo(object):

  # ################################################################################
  # initialization of module and optional load of config files
  # ################################################################################
  def __init__(self, working_queue, back_queue):
    #
    # "cmddemo|port|command or action"
    #
    self.queue_identifier = 'cmddemo'   # this is the 'module address'  
    self.working_queue = working_queue  # worker queue to receive jobs 
    self.back_queue = back_queue        # queue to communicate back to main thread
    self.ports = [                      # internal port names
      { 
        'id'      : 0,
        'type'    : 'switch',
        'status'  : 'on'
      }, { 
        'id'      : 1,
        'type'    : 'switch',
        'status'  : 'unknown'
      }, {}, {}, {} ] # defining internal ports here (...)


  # ################################################################################
  # main thread of this module file which runs in background and constanly
  # checks working queue for new tasks. 
  # ################################################################################
  def worker(self):
    while True:
      _action = "status"  # this should be gatherd from "working queue"
      _port   = 0         # ...

      options = {
        "status"    : self.status,
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
  #
  # @arguments:  port
  # @return:     -
  # ################################################################################
  def status(self, port):
     print "Cmddemo :: status(" + str(port) + ") => " + self.ports[port]['status']

  # ################################################################################
  # sets the port provided by @argument to on
  #
  # @arguments:  port
  # @return:     -
  # ################################################################################
  def set_on(self, port):
    self.ports[port]['status'] = 'on'
    print "Cmddemo :: set_on(" + str(port) + ")"

  # ################################################################################
  # sets the port provided by @agrument to off
  #
  # @arguments:  port
  # @return:     -
  # ################################################################################
  def set_off(self, port):
    self.ports[port]['status'] = 'on'
    print "Cmddemo :: set_off(" + str(port) + ")"



#
# main for testing
#
#if __name__ == '__main__':
#  h = Cmddemo("queue_Object", "back_queue")
#  h.set_on(0)
#  h.status(0)
#  h.worker()
