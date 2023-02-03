.. _de-software-installation:


=====================
Software Installation
=====================

Installing the system is fairly straight forward. You need to start with a `Raspberry-PI board that is up and running <https://www.raspberrypi.com/software/operating-systems/>`_ with ssh connection.
Different versions of software can be found `here <https://cloud.ardupilot.org/downloads/>`_ 



|
.. youtube:: cvQgMcnM7NA
|





Steps
=====

Make sure you have a Raspberry-PI board with `Raspberry PI OS Lite (Legacy) <https://downloads.raspberrypi.org/raspios_oldstable_lite_armhf/images/raspios_oldstable_lite_armhf-2022-01-28/2022-01-28-raspios-buster-armhf-lite.zip>`_ installed on it.
This is important to have access to camera if you choose to run Camera Module. In case of using Bullseye-64 then enable Legacy Camera using raspi-config.


Open `Drone-Engage WebSite <https://www.droneengage.com>`_ and select `"Download Application" <https://cloud.ardupilot.org/downloads>`_ .
|
Download the appropriate binary for your board and version.
|
Copy files to youe home folder in the board.
|

Copy downloaded file to your raspberry using the following command:

.. code-block:: bash

   scp ./latest.zip  pi@raspberry_pi_ip_address:.
|


login to your raspberry-pi board using the following commands:
    
.. code-block:: bash

   ssh pi@raspberry_pi_ip_address

|
.. tip::
    Now you can download the files directly into Raspberry-PI using from `here <https://cloud.ardupilot.org/downloads/RPI/>`_ .

|

Unzip your file. It will extract a folder and a file script.


.. code-block:: bash

   chmod +x ./install_droneengage.sh

Now you need to start the installation process.

.. code-block:: bash

   ./install_droneengage.sh

The above command will extract folder **drone_engage** that contains two applications. **de_comm** that is responsible for communicating with 
Drone Engage server via Internet, and **de_mavlink** that is responsible for communicating with your flight controller "FC" board.
It will also ensure that these applications will be autorun so whenever you power up the board these applications will start.

|

Configuring Apps
================

You need to edit two text files to register simple information required to run apps properly. You do not need to go through all
settings right now. 

Update your account in file **./drone_engage/de_comm/config.module.json** you need to enter your email & :term:`Access Code`.
You may also name your vehicle.

.. code-block:: bash

   nano ./drone_engage/de_comm/config.module.json 
|



Update your connection to Flight Controller in file **./drone_engage/de_mavlink/config.module.json**. You can choose a UDP connection to your board if you are using a Linux FCB
such as `OBAL <https://ardupilot.org/copter/docs/common-obal-overview.html>`_ or you can use serial connection using TX&RX pins.

for more information about this file :ref:`de-config-comm` 

|


.. code-block:: bash

   nano ./drone_engage/de_mavlink/config.module.json 
|


for more information about this file :ref:`de-config-mavlink`    




   


