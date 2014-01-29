import os, sys, glob, re, ConfigParser

# ################################################################################
#
# ################################################################################
class ConfigReader(object):
  def __init__(self, conf_dir, file_ext):
    self.cfg = ConfigParser.ConfigParser();

    # get current script path, join it with the relative path provided by
    # param conf_dir and save all files with the extension provided by param
    # file_ext within the instance variable files.
    self.files = glob.glob(
      os.path.join(
        os.path.join( os.getcwd() + "/" + conf_dir ),
        '*' + file_ext
      ) 
    )

# ################################################################################
#
# ################################################################################
class ConfigItemReader(ConfigReader):

  def __init__(self, item_conf_dir='config/items/'):
  
    super(ConfigItemReader, self).__init__(item_conf_dir, '.item')

    self.item_conf_dir = item_conf_dir
    self.items = {}

    # read all config files and create a hash from it
    for cfg_file in self.files:
      self.cfg.readfp(open(cfg_file))
      for cfg_section in self.cfg.sections():
        self.items.update(
          {
            cfg_section: [
              self.cfg.get(cfg_section, "module_name"),     # module
              self.cfg.getint(cfg_section, "module_addr"),  # module_id
              self.cfg.get(cfg_section, "type")             # type
            ]
          }
        )

  def get_items_dict(self):
    return self.items

  # return a uniq list with all used modules within the items.
  def modules_items(self):
    module_list = []

    for item in self.items:
      module_list.append(
        self.items[item][0]
      )
    
    return list(set(module_list))


# ################################################################################
# ConfigBaseReader reads the configuration file and creats a dictonary out of
# the configuration. See below example for how to access the values than.
#
# Usage:
#
# >>> config = ConfigBaseReader()
# >>> values = config.get_values()
# >>> print values['services']['start_webserver']
#
# ################################################################################
class ConfigBaseReader(ConfigReader):
  def __init__(self, conf_dir='config/'):

    super(ConfigBaseReader, self).__init__(conf_dir, '.config')

    self.config_options = {}
    self.cfg.readfp( open(self.files[0]) )

    true_false = re.compile('^([Tt]rue|[Ff]alse)$')   # regular expression:
                                                      # true|false (with or without capital letter)

    # (1) Get all sections in config file and process each one individually
    # (2) Create a tmporary dictonary
    # (3) Get all options within the current section and process each one individually
    # (4) For each options within the section we add it to the tmporary dictionarry
    #     if the value is a string with "true" or "false" we evaluate it to get a real 
    #     boolean value from the string.
    # (5) The temp directory is than added to the "main" dictionary

    for cfg_section in self.cfg.sections():                           # (1)
      tmp = {}                                                        # (2)
      for option in self.cfg.options(cfg_section):                    # (3)
        opt_val = self.cfg.get(cfg_section, option)
        if true_false.match( opt_val ):
          tmp.update({ option: eval( opt_val.capitalize() ) })        # (4)
        else:
          tmp.update({ option: opt_val })                             # (4)

      self.config_options.update({cfg_section: tmp})                  # (5)

  def get_values(self):
    return self.config_options


  def modules_services(self):
    """
    Returns a list of modules which are responsible for the provided services.
    Only modules which have the flag 'true' are returned.
    """

    service_list = []
    services = self.config_options['services']

    for service_key in services.keys():

      # config: 'start_api_rest'; module_tame = 'rest';
      if services[service_key] and service_key == 'start_api_rest':
        service_list.append('rest')
      # add additional services / module mappings here
      # ...

    return service_list


  def logfile_path(self):
    """
    Returns path to hasip logfile.

    Returns:
      - default value (log/hasip.log) if not set in configuration file
      - or value from configuration file
    """

    if 'logfile' in self.config_options['main'].keys():
      return self.config_options['main']['logfile']
    else:
      return 'log/hasip.log'


  def loglevel_console(self):
    """
    Returns loglevel for console logging.

    Returns:
      - default value (0) if not set in configuration file
      - or value from configuration file
    """

    if 'console_log_lvl' in self.config_options['main'].keys():
      return self.config_options['main']['console_log_lvl']
    else:
      return 0 # NOTSET

  def loglevel_file(self):
    """
    Returns loglevel for file logging.

    Returns:
      - default value (INFO) if not set in configuration file
      - or value from configuration file
    """

    if 'logfile_log_lvl' in self.config_options['main'].keys():
      return self.config_options['main']['logfile_log_lvl']
    else:
      return 'INFO'
