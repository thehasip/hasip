####################################
# importing standard libraries
####################################
import logging, time, os, re
from lib.base.general import ConfigBaseReader

####################################
#5 loglevels are available. All messages from the modules can be either displayed on the
#command line or also logged into the log file. The log level can be specified in the config file.
#debug, info, warn, error, critical
####################################
class Log():

  config_hasip = ConfigBaseReader()
  
  def __init__(self, fname = config_hasip.logfile_path(),
                     clvl  = config_hasip.loglevel_console(),
                     flvl  = config_hasip.loglevel_file()):

    self.clvl = eval('logging.'+clvl)
    self.flvl = eval('logging.'+flvl)

    # absolut / relative
    if re.match('^/', fname):
      self.path = fname
    else:
      self.path = os.path.join(os.getcwd(), fname)

    self.logger = logging.getLogger('Hasip')
    self.loglvl = self.logger.setLevel(logging.DEBUG)
    self.fhandler = logging.FileHandler(self.path)
    self.fhandler.setLevel(self.flvl)
    self.chandler = logging.StreamHandler()
    self.chandler.setLevel(self.clvl)
    self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    self.fhandler.setFormatter(self.formatter)
    self.chandler.setFormatter(self.formatter)

    self.logger.addHandler(self.fhandler)
    self.logger.addHandler(self.chandler)

    self.logger.debug('Logger initialized')

    
####################################
#Block for testing log messages
####################################
    #self.logger.debug('DEBUG Testmessage')
    #self.logger.info('INFO Testmessage')
    #self.logger.warn('WARNING Testmessage')
    #self.logger.error('ERROR Testmessage')
    #self.logger.critical('CRITICAL Testmessage')


