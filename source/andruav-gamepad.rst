.. _andruav-gamepad:



========================
Navigation Using GamePad
========================



.. image:: ./images/xbox_web.png
   :align: center
   :alt: XBox Wired Gamepad

|

:ref:`webclient-whatis` allows you to connect XBOX-360 gamepad directly to your webbrowser. 
You do not need to run GCS applications such as `Mission Planner <https://ardupilot.org/planner/>`_ to connect your joystick anymore.

|

Features
========

1. Gamepad can control one vehicle at a time. And you can switch control between multiple vehicles.
2. Channel reverse and scale is set from Andruav-Drone settings. This is a very important feature, as if you are going to use GamePad for different drones and vehicle you will need to reverse some channels and change rate of some channels based one the vehicle your control. This is handled automatically by storing RX settings in each Andruav Drone App mobile through **RC Settings** screen.


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

.. image:: ./images/rx_web_onscreen.png
   :width: 50 %
   :alt: Adjust Channels

|


4. You need to use a wired XBOX Gamepad not the wireless one. Other Gamepads can work, however you need to make sure channels are mapped correctly.


.. image:: ./images/xbox-wired.png
   :align: center
   :alt: XBox Wired Gamepad


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

This mode is activated automatically from :ref:`webclient-whatis` when switching to **Guided Mode** in copter vehicle. It is equivelant to fly-by-wire in ArduPlane.

|

.. tip::
   You can use :ref:`andruav-simulators` for safely testing this feature.

   
