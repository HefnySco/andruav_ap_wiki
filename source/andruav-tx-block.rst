.. _andruav-tx-block:

===================
Andruav RC Blocking
===================


Assume you are in the field with your TX in your hands. Your drone is flying using Andruav. Your friend is using :ref:`andruav-web-client` and controls your drone from else where.
For any reason you need to take control of your drone. And you need to prevent remote access to your drone.  
You need to be able to control your drone from your TX directly to save it from a crash -for example-. 
Here comes the value of **RC-Block** where you can define a channel on yout TX. Once this channel is actived Andruav stops executing any command from any GCS and redirect your TX signal to FCB board and you take for control of your drone.

This mechanism ensures that the pilot in the field with TX has full control over a remote pilot to ensure better security as safety.
 

.. image:: ./images/blocking.png
   :height: 400px
   :align: center
   :alt: XBox Wired Gamepad

How to Use
==========

#. From Andruav Drone Setting enable RC Block.
#. Choose a channel to activate from your TX.
#. Set minimum PWM value for this channel after which it is considered active.

|
.. youtube:: https://www.youtube.com/watch?v=hL0x1kCPyX4



|

.. tip::

    You can block and un-block Andruav as you wish.

