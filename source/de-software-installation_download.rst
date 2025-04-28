.. _de-software-installation_download:


===========================================
Drone Engage RPI-WZero2 / RPI-4 Ready Image
===========================================


You can download a ready-made image from here:

Download Image from `Here <https://cloud.ardupilot.org/downloads/RPI_Full_Images/droneengage_rpi/rpi_wzero_2_drone_engage_w_camera.xz>`_ .

Please remember to change the password to your own WIFI password by editing /etc/wpa_supplicant/wpa_supplicant.conf
as in the below images.


sudo nano ./etc/wpa_supplicant/wpa_supplicant.conf

username/password:  **pi/raspberry**


.. image:: ./images/wpa_path.png
   :align: center
   :alt: wpa_supplicant file path

|


.. image:: ./images/wpa_file.png
   :align: center
   :alt: wpa_supplicant file


change SSID and password to your own WIFI and password by editing it on your laptop before running the ROM on the RPI.



Also please update your account by editing file de_comm.config.module.json

.. image:: ./images/de_comm_config.png
   :align: center
   :alt: de_comm.config.module.json


|

you can stop and restart DroneEngage Services  using the following commands:

.. code-block:: bash

      ~/home/pi/stop_droneengage_services.sh

      ~/home/pi/restart_droneengage_services.sh

.. important::

     services will start automatically when you restart RPI board. Stopping services does not disable them.






