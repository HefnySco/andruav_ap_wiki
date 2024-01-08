.. _de-install:

========================
DroneEngage Installation
========================


Preparing Raspberry
===================


If you want to install **Telemetry without Video** then you can use `RPI-Zero W <https://www.raspberrypi.com/products/raspberry-pi-zero-w/>`_.
If you want to install **Telemetry and Video streaming** then you can use `RPI-Zero W2 <https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/>`_ or and for multiple camera support please use `RPI-4 <https://www.raspberrypi.com/products/raspberry-pi-4-model-b/>`_.

The following steps assume that you know how to install a raspberry-pi and have a raspberry-pi board up and running and accessible using SSH.


.. important::
    You need to execute this script also to install **libcrypto_1.1**
    `install_libcrypto_1.1.sh <https://github.com/DroneEngage/DroneEngage_ScriptWiki/blob/main/helper_scripts/install_libcrypto_1.1.sh>`_


Download Binaries
=================


Binaries are available at `Binaries Download <https://cloud.ardupilot.org/downloads/>`_ and are ordered by date. 
There is a version for each application. i.e. de_comm may have a different version than de_mavlink as each one has its own fixed and updates.


.. code-block:: bash
    
    $ ssh pi@raspberrypi.local




.. code-block:: bash
    
    $ wget https://cloud.ardupilot.org/downloads/RPI/01__29Aug2022/Drone_Engage_29Aug_2022.zip
    $ wget https://cloud.ardupilot.org/downloads/RPI/01__29Aug2022/Drone_Camera_29Aug_2022.zip

* Please check https://cloud.ardupilot.org/downloads/RPI to download latest version.*

Now you can see two scripts:

* **install_droneengage.sh** for telemetry.
* **install_droneengage_camera.sh** for camera

make sure that these scripts are executable by running

.. code-block:: bash
    
    chmod a+x ./install_droneengage.sh
    chmod a+x ./install_droneengage_camera.sh

now execute scripts

.. code-block:: bash
    
    ./install_droneengage.sh
    ./install_droneengage_camera.sh


after they finish you will a folder called drone_engage


* **/home/pi/drone_engage/de_comm**   Communicator Module.
* **/home/pi/drone_engage/de_mavlink**  Mavlink Module that communicates with FCB.
* **/home/pi/drone_engage/de_camera**   Camera Module that streams video and records video and images.

each folder contains **config.module.json** that you need to edit.




DE_COMM Configuration File 
--------------------------

:ref:`de-config-comm`

You mainly need to enter two fields:

"userName"                  :"team@ardupilot.org", 
"accessCode"                :"1234",

use your own account and access code from registration.


DE_MAVLINK Configuration File 
-----------------------------

:ref:`de-config-mavlink`

you can enable wifi connection or serial connection form the settings:

.. code-block:: bash
    
    "fcb_connection_uri":
    {  
        "type": "udp",
        "ip": "0.0.0.0",
        "port":14445
    },
    // Using serial interface
    //"fcb_connection_uri":
    // {
    //   "type": "serial",
    //   "port": "/home/mhefny/ttyUSB23",
    //   "baudrate": 115200
    // },


The wifi can be used also to connect to SITL on your laptop by running that sends UDP to 14445 on your RaspberryPI IP.

.. code-block:: bash
    
    $ python3 ardupilot/Tools/autotest/sim_vehicle.py -j4 -v ArduCopter    -M --map --console --instance 50   --out=udpout:RPI-IP:14445

or 

.. code-block:: bash
    
    //"fcb_connection_uri":
    //{  "type": "udp",
    //   "ip": "0.0.0.0",
    //   "port":14445
    //},
    // Using serial interface
    "fcb_connection_uri":
    {
        "type": "serial",
        "port": "/home/mhefny/ttyAMA0",
        "baudrate": 115200
    },






.. important::
    Only one connection should be active and the other should be commented by "//" or remove it form the file.





DE_CAMERA Configuration File 
-----------------------------

you mainly need to define cameras. bedefault there is a camera defined on /dev/video0 and given name "AI1"

.. code-block:: json
    
    "one_session_per_camera"    : true,
    "camera_list": [
    {
      "name": "AI1", "device_num": 0
      "name": "AnotherCAM", "device_num": 1 // you can add additional cameras
    } // name should be unique across all cameras.
    ],


you can also choose to enumerate on video devices that exists in a given range. 
for example list all video devices from **/dev/video0** to **/dev/video10** :

.. code-block:: json
    
    "one_session_per_camera"    : true,
    "camera_start_index"        :0, 
    "camera_end_index"          :10,
    


You can comment the unwanted option by adding **//** at the beginning if its line.

Other parameters exists but they are not mandatory to change and you can just leave them as a start.


.. important::
    you need to enable legacy camera suppot on camera devices that you are using, and remember to reboot.
    **sudo raspi-config nonint do_legacy 0**





The following video describes installation procedures. It may differ from version to another, but the video includes the main steps.

.. youtube:: cvQgMcnM7NA








