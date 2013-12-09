class Basemodule(object):
  def __init__(self, working_queue, back_queue):
    raise NotImplementedError, "__init__(self, working_queue, back_queue)"

  def worker(self):
    raise NotImplementedError, "worker(self)"
