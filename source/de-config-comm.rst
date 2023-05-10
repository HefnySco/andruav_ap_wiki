.. _de-config-comm:

=============================================
de_comm config.module.json Configuration File
=============================================

A file called **de_comm.config.module.json** exists in **/home/pi/drone_engage/de_comm/**
This file is written in :term:`JSON` format. However, you can still add comments to the file.
To those who do not know :term:`JSON` just consider it a text file that you need to edit only few lines in it.


login to your Raspberry-PI board using ssh.

.. code-block:: bash

   ssh pi@raspberry_pi_ip_address
|

and go to the file

.. code-block:: bash

   cd /home/pi/drone_engage/de_comm/
   ls
  
|

and open the file 

.. code-block:: bash

   nano config.module.json

|

Fields Meaning
==============


.. list-table:: de_comm.config.module.json
   :widths: 25 25 50
   :header-rows: 1

   * - Heading Field Name
     - Heading Description
     - Heading Example
   * - "module_id"
     - just a name for your module. 
     - "C1" , "COMM_MAIN" ...etc.
   * - "s2s_udp_listening_ip" (**)
     - listen ip for the de_comm module to communicate with other modules. 
     - "127.0.0.1" if all modules on the same board else "0.0.0.0".
   * - "s2s_udp_listening_port" (**)
     - ip port used to communicate with other modules. 
     - default: "60000".
   * - "auth_ip" (**)
     - authentication server ip 
     - "andruav.com", "droneengage.com", or your local server ip.
   * - "auth_port" (**)
     - authentication server port. It is a number no "" 
     - default: 19408. Do not change unless you use a local server.
   * - "userName" (M)
     - just a name for your module. 
     - "C1" , "COMM_MAIN" ...etc.
   * - "accessCode" (M)
     - just a name for your module. 
     - "C1" , "COMM_MAIN" ...etc.
   * - "unitID" (M)
     - a readable name for your drone that will be displayed. 
     - "drone1", "D1-Copter" ...etc.
   * - "groupID" (**)
     - "1" 
     - s
   * - "unitDescription" (M)
     - a brief single line description of vehicle.
     - "My X8 Drone" ...etc.
   * - "logger_enabled" (*)
     - enabling it will create a log file for each run in a folder called Logs
     - false

         

`(*)` You can keep default value.  

`(**)` You **SHOULD** keep the default value unless you know what you do.

`(M)` You need to change it based on your account.


**Note:**  **userName** and **accessCode** can be generated from :ref:`de-account-create`.
