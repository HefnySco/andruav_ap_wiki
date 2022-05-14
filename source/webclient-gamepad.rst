.. _webclient-gamepad:



========================
Navigation Using GamePad
========================


.. youtube:: https://www.youtube.com/watch?v=-qh248Hnn-M

|

:ref:`webclient-whatis` allows you to connect XBOX-360 gamepad directly to your webbrowser. 
You do not need to run GCS applications such as `Mission Planner <https://ardupilot.org/planner/>`_ to connect your joystick anymore.

|

Features
========

1. Gamepad can control one vehicle at a time. And you can switch control between multiple vehicles.
2. Channel Settings:

On Drone Engage
---------------
Channel reverse and scale is set by editing **config.module.json** file. This is a very important feature, as if you are going to use GamePad for different drones and vehicle you will need to reverse some channels and change rate of some channels based one the vehicle your control. This is handled automatically by storing RX settings in each **Ardupilot-Module** configuration file.

.. code-block:: JAVASCRIPT

   "rc_channels":
   {
      "rc_channel_enabled": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      "rc_channel_reverse": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      "rc_channel_limits_max": [1850,2000,1750,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000],
      "rc_channel_limits_min": [1150,1000,1300,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000]
   }
   
.. note::

    Although xml does not allow adding comments in c-style using "//" but **config.module.json** accepts this syntax.


On Andruav
----------

Channel reverse and scale is set from Andruav-Drone settings. This is a very important feature, as if you are going to use GamePad for different drones and vehicle you will need to reverse some channels and change rate of some channels based one the vehicle your control. This is handled automatically by storing RX settings in each Andruav Drone App mobile through **RC Settings** screen.


|pic1|  and   |pic2|

.. |pic1| image:: ./images/rc_settings.png
   :width: 35 %
   :alt: How to enter to RC Settings

.. |pic2| image:: ./images/rc_screen.png
   :width: 35 %
   :alt: Adjust Channels

3. You can change flight modes from GamePad buttons by long pressing "red - yellow - blue - green" buttons.

+------------+------------+-----------+
| VEHICLE    | COLOR      | MODE      |
+------------+------------+-----------+
| Copter     | blue       | Guided    |
+------------+------------+-----------+
| Copter     | green      | Land      |
+------------+------------+-----------+
| Copter     | red        | Break     |
+------------+------------+-----------+
| Copter     | yellow     | RTL       |
+------------+------------+-----------+

.. image:: ./images/rx_web_onscreen2.png
   :width: 50 %
   :alt: Adjust Channels

|


4. You need to use a wired XBOX Gamepad not the wireless one. Other Gamepads can work, however you need to make sure channels are mapped correctly.


.. image:: ./images/xbox-wired.png
   :align: center
   :alt: XBox Wired Gamepad


5. Smart RCMAP can be enabled on :ref:`what-is-drone-engage` only. This feature allows using Gamepad without maping channels. The system will automatically map it using RCMap infrom from ardupilot. 
However you can set maximum and minimum ranges from **config.module.json**



.. youtube:: https://www.youtube.com/watch?v=MeYIKJpHngM


|
   The above video shows actual controlling of a Rover via Drone-Engage. There is a delay and this is because data is transmitted from WebClient to Server, and then to Drone-Engage communicator module, then to Drone-Engage Mavlink module and finally to Ardupilot.
   There is lot of transmission and re-transmission here. But in open area this should be acceptable.

|
.. note::

    Connecting joystick to Mission Planner and control your drone via :ref:`webclient-webplugin` is possible but not recommended as this method is more efficient.
|


Running in Linux
================

For Windows you can just plug you xbox-360 gamepad directly and it will be detected by Windows with no extra settings. In linux you need to run a simple script before the browser is able to detect gamepad.

You need to create .sh file and run it.

.. code-block:: bash

    #!/bin/bash
    sudo killall xboxdrv
    sudo xboxdrv --detach-kernel-driver

|

Taking & Releasing Control
==========================

To activate control to GamePad press **RX** button for the vehicle you want to control. **RX** button should be **RX-ON**.

.. image:: ./images/menu_rx_off.png
   :align: center
   :alt: Take Remote

To release control press the same button **RX** or press **TX-Rel** button. **RX** button should be **RX-Off**.

.. image:: ./images/menu_rx_on.png
   :align: center
   :alt: Release Remote

|

DJI-Style Remote
================

`DJI  <https://www.dji.com/phantom>`_ is known of its ease of flying among many other features. What is targetted here is that changing throttle stick function so that pushing stick up will lead to climbing while pusshing it down will lead to decreasing altitude. Andruav make use on Ardupilot remote control features to achieve similar capabilities.

This mode is activated automatically from :ref:`webclient-whatis` when switching to **Guided Mode** in copter vehicle. 

|

.. tip::
   You can use :ref:`andruav-simulators` for safely testing this feature.

   
