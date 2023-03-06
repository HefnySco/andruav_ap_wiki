.. _what-is-drone-engage:

======================
What is Drone-Engage ?
======================

Drone-Engage is a distibuted system that allows monitoring & controlling drones via Internet. 
Drone-Engage does a lot of every cool things, including:

* a metered telemetry connection from your drone to a website and 
* (optionally) forwarding telemetry to/from your ground station such as Mission Planner or QGroundControl
* easy streaming of video and/or pictures from one or more cameras connected to the companion computer in the vehicle
* ability to record video or pictures on the drone or on your computer via the web interface.
* An easy to use web based ground control station interface that can be accessed via the internet from literally anywhere
* Ability to manage a fleet of many drones using the same interface
* An advanced geo-fencing capability that supersedes the flight controller 
* Synchronized missions - where multiple vehicles co-ordinate with each other
* The ability to remotely fly your drone via the internet using a controller connected to your ground station

In a nutshell Drone-Engage is:

* Ardupilot or PX4 companion software that runs on a companion computer in your Drone (Plane, Multi-Roter, Copter, Rover, Sub)
* A website that can be used as a groundstation to control multiple drones
* A drone camera streaming platform for your drone(s)
* A remote controller that allows you to control your drone over the internet

Basic requirements for Drone-Engage to work are:
* A Raspberry PI directly connected to your autopilot on the vehicle
* A 4G or LTE connection to the internet via the Raspberry PI
* A login/access code for Drone-Engage on ArduPilot Cloud (cloud.ardupilot.org)
* [optional] One or more cameras directly connected to the Raspberry PI
* [optional] An X-box controller connected to your PC 

Drone-Engage objective is to provide a Linux-based alternative for `Andruav <https://play.google.com/store/apps/details?id=arudpilot.andruav&hl=en&gl=US>`_ Android mobiles.


.. youtube:: F9b4dXLRLjg

Now you can use Raspberry-pi boards to run Drone-Engage companion computer software and enjoy tiny size of RPI-Zero, and the multi-camera capabilities or RPI-4.

.. image:: ./images/setup1.png
        :align: center
        :alt: Drone-Engage on RPI-Zero connected to OBAL board.


.. tip::

      Download Drone-Engage apps from `here <https://drive.google.com/drive/folders/1wMIw5VSW4CdIxMXIFMeq0AyuZBDIfFaH?usp=sharing>`_



Drone-Engage uses on-board Raspberry-Pi Zero connected to `Ardupilot <https://ardupilot.org/>`_ flight control board "FCB" to provide unlimited range telemetry and control. 

.. image:: ./images/rpizeroweight.jpeg
        :align: center
        :alt: Drone-Engage on RPI-Zero

This example is only 42 grams or 1.48 oz and 
is everything you need to take full control on your drone anywhere anytime.


If you want to make use of video streaming then you can use Raspberry-Pi Zero 2. It is only 52.2gm or 1.84oz.
including camera and OTG cable. A Zero 2 is enough for one camera, but if you want more than one camera you will need a more powerful PI.

.. image:: ./images/IMG_20220402_160422.jpg
        :align: center
        :alt: Drone-Engage on RPI-Zero-2 with camera









