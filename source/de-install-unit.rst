.. _de-install-unit:

========================
DroneEngage Installation
========================

Choose your preferred installation method below. The **Ready-Made Image** is recommended for most users.

|

.. toctree::
   :titlesonly:
   :maxdepth: 1
   
   Installing from Binaries </de-software-installation_binaries>

|

Hardware Requirements
=====================

DroneEngage supports various Raspberry Pi models. Choose based on your needs:

.. list-table::
   :widths: 30 35 35
   :header-rows: 1

   * - Use Case
     - Recommended Board
     - Notes
   * - **Telemetry Only**
     - `RPI-Zero W <https://www.raspberrypi.com/products/raspberry-pi-zero-w/>`_
     - Lightest option, no video
   * - **Telemetry + Single Camera**
     - `RPI-Zero 2 W <https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/>`_
     - Best balance of size/performance
   * - **Multi-Camera Setup**
     - `RPI-4 <https://www.raspberrypi.com/products/raspberry-pi-4-model-b/>`_
     - Most powerful, multiple cameras

|

Installation Methods
====================

Ready-Made Image (Recommended)
------------------------------

The easiest way to get started. Pre-built images include all modules and configurations.

- Download from `cloud.ardupilot.org/downloads/RPI_Full_Images <https://cloud.ardupilot.org/downloads/RPI_Full_Images/droneengage_rpi/>`_
- Available for RPI-Zero 2 W and RPI-4
- Includes telemetry, camera, and all dependencies

.. youtube:: WEE4tTnNDwQ

See :ref:`de-software-installation_download` for detailed instructions.

|

Installing from Binaries
------------------------

For users who prefer manual installation or need custom configurations.

- Requires Raspberry Pi OS with SSH access
- Download binaries from `cloud.ardupilot.org/downloads/RPI <https://cloud.ardupilot.org/downloads/RPI/>`_

.. youtube:: cvQgMcnM7NA

.. tip::
   For Bullseye, enable "Legacy Camera Support" via ``raspi-config``.

See :ref:`de-software-installation_binaries` for detailed instructions.







