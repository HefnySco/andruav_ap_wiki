.. _de-config-mavlink:

=============================
de_mavlink Configuration File
=============================

A file called **config.module.json** exists in **/home/pi/drone_engage/de_mavlink/**
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

   nano config.module.json

|

Fields Meaning
==============


.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - Heading Field Name
     - Heading Description
     - Heading Example
   * - "module_id"
     - just a name for your module. 
     - "C1" , "COMM_MAIN" ...etc.
   * - "module_key" (*)
     - unique identification for your module.
     - GUID number. you can change it or just leave it.
   * - "s2s_udp_target_ip" (**)
     - points to de_comm **"s2s_udp_listening_ip"** in :ref:`de-config-comm`. 
     - "127.0.0.1" if all modules on the same board else the comm board IP e.g. "192.168.1.147".
   * - "s2s_udp_target_port" (**)
     - ip port used by communicate ** "s2s_udp_listening_port"** in :ref:`de-config-comm`.
     - default: "60000".
   * - "s2s_udp_listening_ip" (**)
     - listen ip for the de_comm module to communicate with other modules. 
     - "127.0.0.1" if :term:`Comm Module` on the same board else "0.0.0.0".
   * - "s2s_udp_listening_port" (**)
     - ip port used to communicate with :term:`Comm Module`. 
     - default: "60003".
   * - "fcbConnectionURI" (M)
     - This is the connection to the flight control :term:`FCB` board. 
     - 
   


`(*)` You can keep default value.  

`(**)` You **SHOULD** keep the default value unless you know what you do.

`(M)` You need to change it based on your account.



.. code-block:: json

    {
    "fcbConnectionURI":
     {
     "type": "serial",
     "port": "/dev/serial0",
     "baudrate": 115200
     }
    }
    
**baudrate** has to match the baudrate defined in :term:`FCB`. You can open :term:`GSC` and configure mavlink parameters.

.. important::
    You need to connect TX of RPI o RX of the :term:`FCB` and vice-versa.

|

.. important::
    If you want to use the OTG USB port make sure you run **rasp-config** and disable shell but keep serial port enabled.

|

