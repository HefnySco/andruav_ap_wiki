.. _de-config-mavlink:

=============================
de_mavlink Configuration File
=============================

A file called **de_mavlink.config.module.json** exists in **/home/pi/drone_engage/de_mavlink/**
This file is written in :term:`JSON` format. However, you can still add comments to the file.
To those who do not know :term:`JSON` just consider it a text file that you need to edit only few lines in it.


login to your Raspberry-PI board using ssh.

.. code-block:: bash

   ssh pi@raspberry_pi_ip_address
|

and go to the file

.. code-block:: bash

   cd /home/pi/drone_engage/de_mavlink/
   ls
  
|

and open the file 

.. code-block:: bash

   nano de_mavlink.config.module.json

|

Fields Meaning
==============


.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - Field Name
     - Description
     - Example
   * - "module_id"
     - Just a name for your module. 
     - "C1" , "COMM_MAIN" ...etc.
   * - "s2s_udp_target_ip" (**)
     - points to de_comm **"s2s_udp_listening_ip"** in :ref:`de-config-comm`. 
     - "127.0.0.1" if all modules on the same board else the comm board IP e.g. "192.168.1.147".
   * - "s2s_udp_target_port" (**)
     - ip port used by communicate ** "s2s_udp_listening_port"** in :ref:`de-config-comm`.
     - default: "60000".
   * - "s2s_udp_listening_ip" (**)
     - Listen ip for the de_comm module to communicate with other modules. 
     - "127.0.0.1" if :term:`Comm Module` on the same board else "0.0.0.0".
   * - "s2s_udp_listening_port" (**)
     - ip port used to communicate with :term:`Comm Module`. 
     - default: "60003".
   * - "fcbConnectionURI" (M)
     - This is the connection to the flight control :term:`FCB` board. 
     - 
   * - "default_optimization_level"
     - Telemetry bandwidth optimization. 0 means no optimization and 3 is the make optimization check :ref:`de-telemetry`.
     - any value from 0 to 3
   * - "udp_proxy_enabled" (*)
     - This is to enable the udp telemetry. By default it is disabled.
     - true, Default(false)
   * - "udp_proxy_fixed_port" (*)
     - Specify a fixed port for UDO cpnnection or you can change it from WebClient. Communication Server can ignore this value based on its settings.
     - 
   * - "ignore_loading_parameters" (*)
     - This enable and disable loading vehicle parameters and expose it to web client. You need to enable this if you want to use R/C gamepad :ref:`webclient-gamepad`.
     - true, Default(false)
   * - "read_only_mode" (*)
     - This is used to prevent any type of commands from WebClient. WebClient will be used for monitoring only. When this is true nothing can control the drone even from udp telemetry.
     - true, Default(false) 
   * - "logger_enabled" (*)
     - enabling it will create a log file for each run in a folder called Logs
     - false
   * - "message_timeouts" (*)
     - This is used to determine message rates for mavlink telemetry.
     - see :ref:`webclient-udp-telemetry`

`(*)` You can keep default value.  

`(**)` You **SHOULD** keep the default value unless you know what you do.

`(M)` You need to change it based on your account.



Connecting via UDP:

 .. code-block:: json

    {
    "fcb_connection_uri": 
    {
    "type": "udp",
    "ip": "0.0.0.0",
    "port":14551
    },
    }

This connection is straight forward using UDP. This is suitable when connecting DroneEngage to boards like `OBAL <https://github.com/HefnySco/OBAL>`_ via OTG Ethernet.


Connecting to a Serial Port:

.. code-block:: json

    {
    "fcbConnectionURI":
     {
     "type": "serial",
     "port": "/dev/My_DE_PORT",
     "baudrate": 115200
     }
    }
Remember you can easly `create alias <https://unix.stackexchange.com/questions/66901/how-to-bind-usb-device-under-a-static-name>`_ for your USB to appear such as My_DE_PORT using 

.. code-block:: json

    {
    "fcb_connection_uri":
     {
     "type": "serial",
     "port": "/dev/ttyUSB",
     "baudrate": 115200,
     "dynamic": true
    },
    }

The **dynamic** field will make the module search for a valid mavlink port from /dev/ttyUSB0 to /dev/ttyUSB10. 
So Even if you unplug and plugged it again and the usb appeared on different address the module will find it.
This feature is developed to be able to detect mavlink port from SCan port. 

**baudrate** has to match the baudrate defined in :term:`FCB`. You can open :term:`GSC` and configure mavlink parameters.

.. important::
    You need to connect TX of RPI o RX of the :term:`FCB` and vice-versa.

|

.. important::
    If you want to use the OTG USB port make sure you run **rasp-config** and disable shell but keep serial port enabled.

|

