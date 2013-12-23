Logger
===================

General
-------

The logging module is the basic python logging class. The main logger/handlers are intialized
in the hasip.py with the 3 paramteters from the logging file.
```logfile``` indicates the location of the filename relative to the current working directory which should be "hasip-base"
```con_log_lvl``` sets the logging level of the messages that are displayed on the console
```file_log_lvl``` sets the logging level of the message that are logged into the logfile


Usage
---------

The main and the cmddemo module already have a logger running. One can use logging very simple in each module by including the python logging library and setting a logger name. Then a log message can
be created and the it will catched by the main logger that puts into the console and/or the logfile
depending on the set log levels.


    import logging
    class Module():
      def __init__():
        self.logger=logger.getLogger('Haspip.<Modulename>')
        self.logger.debug('DEBUG Message')
        self.logger.info('INFO Message')
        self.logger.warn('WARNING Message')
        self.logger.error('ERROR Message')
        self.logger.critical('CRITICAL Message')



