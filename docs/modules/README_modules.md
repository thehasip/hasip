Available default modules
========================

- **cmddemo**: Refer to: [module_cmddemo](docs/modules/module_cmddemo.md)
- **cul**: Refer to: [module_cul](docs/modules/module_cul.md)
- **gpio**: Refer to: [module_gpio](docs/modules/module_gpio.md)
- **rest**: Refer to: [module_gpio](docs/modules/module_rest.md)
- **sched**: Refer to: [module_sched](docs/modules/module_sched.md)

Installation of modules
=======================

- To installing additional modules place them within the `hasip/modules/` directory.
- Include the module within the `hasip/modules/__init__.py` file to make it available within the main application.

Development of new Modules
==========================

General information
-------------------

New modules should be placed within the `hasip/modules/` directory. To automatically load the module within the project ensure that you include the module within the `hasip/modules/__init__.py` file.

Example of the `hasip/modules/__init__.py` file:

    # add new modules here:
    from lib.modules.foobarbaz import Foobarbaz

Structure of a module file
--------------------------

Every module file should be a class which inherit it's functionallity from at least the `Basemodule` class. This class specifies the default methods to start the module as a background thread. If your module is intended to provides access via the internal messaging queue to other modules or the application you also have to inherit from one of the other classes listed within `hasip/lib/modules` directory. For example if you want to implement a toggeling of a specific port you have to use the `Switch` class.

Here is a short example of how a module should look like:

    from lib.base.modules import *
    
    class Foobarbaz(Basemodule):
      def __init__(self, instance_queue, global_queue):
        pass

      def worker(self):
        pass

Naming convention for new modules
---------------------------------

- Allowed values: Characters from a-z and A-Z
- Class name has to start with a capital letter
- Integer or special characters are forbidden (e.g. 0-9, $, !, -, ...)
- Capital letters are only allowed at the beginning of the class and not within the class name itself
- The class has to be stored within a file which has the same name as the class itself.

Example for **forbidden** class names: `myFooClass`, `My_Fooclass`, `My42foo`, ...
Example for **allowed** class names: `Foobar`, `Watchdog`, `Foobaz`, ...

General information about modules
=================================

Modules are initialized within the main application when they are used for the first time within an [item](docs/items/README_items.md) file.
