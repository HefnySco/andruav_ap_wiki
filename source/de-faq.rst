.. _de-faq:

===============
DroneEngage FAQ
===============

.. image:: ./images/de.png
   :height: 160px
   :align: center
   :alt: DroneEngage icon

|

Find answers to common questions about using DroneEngage with Ardupilot. For additional terms, see :ref:`glossary`. Submit new questions via `GitHub Issues <https://github.com/DroneEngage/droneengage_communication/issues>`_.

General Questions
=================

**Q: What hardware do I need?**

A: A Raspberry Pi (Zero W, Zero 2 W, 3, 4, or 5) or Radxa board, a 4G/LTE modem, and an Ardupilot or PX4 flight controller. See :ref:`de-what-is` for full requirements.

**Q: Do I need an account?**

A: Yes, you need a DroneEngage account and Access Code from `cloud.ardupilot.org <https://cloud.ardupilot.org>`_. See :ref:`de-account-create` for details.

Installation & Updates
======================

**Q: How do I install DroneEngage?**

A: Follow the :ref:`de-getting-started-index` guide, or see the :ref:`de-install` page for detailed instructions.

**Q: Can I use a pre-built image?**

A: Yes, DroneEngage RPI images are available. See :ref:`de-software-installation_download` for download links.

WiFi & Network
==============

**Q: Does DroneEngage work without internet?**

A: DroneEngage requires internet connectivity (4G/LTE/5G) to connect to the cloud server. Local-only operation is not supported.

**Q: Can I use WiFi instead of 4G?**

A: Yes, WiFi works for local testing. For field operations, 4G/LTE is recommended for reliable connectivity.

Troubleshooting
===============

**Q: My unit won't connect to the server.**

A: Check your internet connection, verify your Access Code, and ensure the server URL is correct. See :doc:`de-config-comm` for communication module configuration.

**Q: Telemetry is not showing in the web client.**

A: Verify the MAVLink module is running and connected to the flight controller. Check :doc:`de-config-mavlink` for configuration details.

For more help, please submit your question via `GitHub Issues <https://github.com/DroneEngage/droneengage_communication/issues>`_.

