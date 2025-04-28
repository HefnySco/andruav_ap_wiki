.. _de-install-unit:

========================
DroneEngage Installation
========================





.. toctree::
   :titlesonly:
   :maxdepth: 1
   
   Ready-Made Image (Recommended) </de-software-installation_download>
   Installing from Binaries </de-software-installation_binaries>
   
|

Hardware Requirements
=====================
Drone-Engage can be installed on a variety of Raspberry Pi models.  The choice of model depends on the desired functionality.
DroneEngage can run **Telemetry without Video** on simple boards like then you can use `RPI-Zero W <https://www.raspberrypi.com/products/raspberry-pi-zero-w/>`_ .
If you want to install **Telemetry and Video streaming** then you can use `RPI-Zero W2 <https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/>`_ or and for multiple camera support please use `RPI-4 <https://www.raspberrypi.com/products/raspberry-pi-4-model-b/>`_.

|

Ready-Made Image (Recommended)
========================
The recommended method for installing Drone-Engage is to use the **pre-built images** available for `download <https://cloud.ardupilot.org/downloads/RPI_Full_Images/droneengage_rpi/>`_ . 
These images are designed to be installed on a Raspberry Pi and come with all the necessary binaries and configurations pre-installed. 
This method is particularly useful for users who may not be familiar with the installation process or who prefer a more streamlined approach.
The pre-built images are available for both the **Raspberry Pi Zero W2** and the **Raspberry Pi 4**. These images include all the necessary software and configurations to get started with Drone-Engage quickly and easily.

Further information regarding image downloads can be found in the :ref:`de-software-installation_download` section.


Installing from Binaries
========================

System installation is straightforward, requiring a functional Raspberry Pi with SSH access.  Raspberry Pi OS can be downloaded from the `official website <https://www.raspberrypi.com/software/operating-systems/>`_. Drone-Engage software packages are available `here <https://cloud.ardupilot.org/downloads/RPI/>`_.

.. youtube:: cvQgMcnM7NA


.. tip::
   For Bullseye, enable "Legacy Camera Support" via `raspi-config`.


Further information regarding image downloads can be found in the :ref:`de-software-installation_binaries`.







