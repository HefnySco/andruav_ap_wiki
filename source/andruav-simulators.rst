.. _andruav-simulators:


=============================
Andruav Simulation using SITL
=============================

You do not need to have a real drone to test Andruav cabapilities. Actually it is recommended to use `SITL <https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html>`_ simulation to test Andruav before actually flying long range with your drone. 

If you want more real action then maybe you can try `Webots SITL <https://ardupilot.org/dev/docs/sitl-with-webots.html>`_ to have a real taste of how using Andruav really feels.

.. youtube:: https://www.youtube.com/watch?v=c5CJaRH9Pig



Connecting to SITL
==================

Andruav connects tp SITL or Webots-SITL in the same way. The easiest way is set Andruav-Drone mobile FCB screen to connect using UDP. You need to specify the listening port.
In SITL simulator make sure that it sends UDP packets to mobile IP address on the specified port.

.. image:: ./images/s_fcb1.jpg
   :height: 400px
   :align: center
   :alt: FCB Screen for Drone Mobile

 
.. code-block:: bash
    
    $ ~/ardupilot/Tools/autotest/sim_vehicle.py -j4 -v ArduCopter -M  --out=udpout:127.0.0.1:14550 --out=udpout:192.168.1.100:10100

The above example sends UDP packets to 127.0.0.1 port 14550 as well as 192.168.1.100 port 10100. So you can use a separate Mission Planner or QGC *not connected to Andruav* to test the drone in parallel.


.. tip::
    give static IP to your mobile so it you do not need to change IP address each time.


Once Andruav is connected to FCB board it should give you an indication and the FCB button turns green.


|pic1|  and   |pic2|

.. |pic1| image:: ./images/s_fcb2.jpg
   :width: 35 %
   :alt: FCB Screen

.. |pic2| image:: ./images/s_fcb3.jpg
   :width: 35 %
   :alt: FCB Screen





