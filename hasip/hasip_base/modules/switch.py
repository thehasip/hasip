class Switch(object):

  def set_on(self, port):
    raise NotImplementedError, "set_on(self, port)"

  def set_off(self, port):
    raise NotImplementedError, "set_off(self, port)"

  def get_status(self, port):
    raise NotImplementedError, "get_status(self, port)"
