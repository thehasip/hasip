Queue Communication
===================

General
-------

The communication between the modules is working via queues. During the initialization of the main instance multiple queues objects where created. The first one is a `global_queue` and the second one is a `instance_queue` which exclusively belongs to one module only.

When a module is initialized both queue objects where passed as reference.

- The `global_queue` is used as a communication channel back to the main thread (e.g. send results, request data from other modules, ...)
- The `instance_queue` is used to send jobs to each module (e.g. "switch on port 1", ...)

On the following chart you can see the concept behind this system:

![queue chart](../raw/master/docs/static_files/queue.chart.png)

Protocol
--------

The communication between the different modules is managed by putting a dictonary into the queue.

A single message has at least the following keys in the message dictonary:

    queue_msg = {
        'module_from':  (String,lowercase),
        'module_rcpt':  (String,lowercase),
        'module_addr':  (Integer),
        'cmd':          (String),
        'opt_args':     (String, Dict, ... )
    }

Here is an example message to get the **status** of port **1** on the **cmddemo** module:

    queue_msg = {
        'module_from':  '',
        'module_rcpt':  'cmddemo',
        'module_addr':  1, 
        'cmd':          'status',
        'opt_args':     ''
    }