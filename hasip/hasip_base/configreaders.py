import os, sys, glob, ConfigParser

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
              self.cfg.get(cfg_section, "module"),       # module
              self.cfg.getint(cfg_section, "module_id"), # module_id
              self.cfg.get(cfg_section, "type")          # type
            ]
          }
        )

  def get_items_dict(self):
    return self.items

# ################################################################################
#
# ################################################################################
class ConfigBaseReader(ConfigReader):
  def __init__(self):
    pass

#print ConfigItemReader().get_items_dict()
