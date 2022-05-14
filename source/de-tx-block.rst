.. _de-tx-block:

========================
Drone-Engage RC Blocking
========================


Assume you are in the field with your TX in your hands. Your drone is flying using Andruav. Your friend is using :ref:`de-web-client` and controls your drone from else where.
For any reason you need to take control of your drone. And you need to prevent remote access to your drone.  
You need to be able to control your drone from your TX directly to save it from a crash -for example-. 
Here comes the value of **RC-Block** where you can define a channel on yout TX. Once this channel is actived Andruav stops executing any command from any GCS and redirect your TX signal to FCB board and you take for control of your drone.

This mechanism ensures that the pilot in the field with TX has full control over a remote pilot to ensure better security as safety.
 
The idea is easy you need to define a channel in yout TX in the field to be used as a switch for entering Block-Mode.


How to Use
==========

The channel is defined in **config.module.json** in field **"rc_block_channel"**. When this field is larger than 1800 pwm blocking mode is activated.
You can still deactivate blocking mde by switching channel to value lower than 1800.


.. code-block:: JAVASCRIPT

   // should be a channel from 1 to 8. when High all commands from GCS will be ignored including RC-Override.
   "rc_block_channel": 6,


|

.. youtube:: https://www.youtube.com/watch?v=hL0x1kCPyX4

|

.. tip::

    You can block and un-block many times during flying.

