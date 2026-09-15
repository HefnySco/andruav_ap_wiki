Developer Guide
===============

This section provides technical documentation for developers who want to build DroneEngage from source, create custom plugins, or understand the internal architecture.

.. toctree::
   :titlesonly:
   :maxdepth: 1

   Building & Setup <de-dev-building-code>
   Raspberry Pi Deployment <technicals/rpi-scripts/rpi-bookworm-scripts>
   Architecture <de-dev-architecture>
   Extending DroneEngage <de-dev-extending>
   Creating Custom Plugins <de-dev-plugin>
   SWARM Logic <de-dev-swarm>
   Web Client Technicals <technicals/webclient/de-web-technicals>
   Communication Module Technicals <technicals/communication/de-comm-technicals>
   Server Technicals <technicals/server/de-server-technicals>
   MAVLink Module Technicals <technicals/mavlink/de-mavlink-technicals>

Overview
--------

DroneEngage is built with a modular architecture:

- **de_comm** - Communication module (connects to cloud server)
- **de_mavlink** - MAVLink module (connects to flight controller)
- **de_camera** - Camera module (video streaming and recording)
- **Plugins** - Custom modules for GPIO, SDR, tracking, etc.

All modules communicate via the **DataBus** using UDP sockets, allowing them to run on the same device or distributed across multiple devices.

Building & Setup
----------------

- :doc:`Building from Source <de-dev-building-code>`

Raspberry Pi Deployment
-----------------------

- `Camera Manager Wrapper <https://github.com/DroneEngage/DroneEngage_ScriptWiki/blob/master/rpi_image_scripts/bookworm/wrapper/README.md>`_ - C++ wrapper for managing DroneEngage camera and tracking modules on Raspberry Pi
- :doc:`Raspberry Pi Bookworm Scripts <technicals/rpi-scripts/rpi-bookworm-scripts>` - Overview of helper scripts for managing DroneEngage services, networking, cameras, simulators, and maintenance on Raspberry Pi OS

Architecture
------------

- :doc:`Communication Protocol <de-dev-andruav-communication-protocol>`
- :doc:`DataBus (Inter-Module Communication) <de-dev-databus>`

Extending DroneEngage
---------------------

- :doc:`Creating Custom Plugins <de-dev-plugin>`
- :doc:`Custom Plugin Development <technicals/de_common/de-custom-plugins>`
- :doc:`C++ Plugin Development <technicals/de_common/de-custom-plugins-cpp>`
- :doc:`Node.js Plugin Development <technicals/de_common/de-custom-plugins-nodejs>`
- :doc:`Python Plugin Development <technicals/de_common/de-custom-plugins-python>`
- :doc:`SWARM Logic <de-dev-swarm>`
- :doc:`Communication Module Config <de-config-comm>`
- :doc:`MAVLink Module Config <de-config-mavlink>`

Web Client Technicals
---------------------

- :doc:`Web Client Overview <technicals/webclient/de-web-technicals>`
- :doc:`Authentication System <technicals/webclient/de-web-technicals-authentication>`
- :doc:`Configuration Management <technicals/webclient/de-web-technicals-configuration>`
- :doc:`Server Communication <technicals/webclient/de-web-technicals-servercomm>`
- :doc:`Site Configuration <technicals/webclient/de-web-technicals-siteconfig>`
- :doc:`Unit Management <technicals/webclient/de-web-technicals-unit>`
- :doc:`WebRTC Video Streaming <technicals/webclient/de-web-technicals-webrtc>`
- :doc:`Mission Planning Base <technicals/webclient/de-web-technicals-moduleplanning>`

Communication Module Technicals
-------------------------------

- :doc:`Communication Module Overview <technicals/communication/de-comm-technicals>`
- :doc:`Andruav Authenticator <technicals/communication/de-comm-technicals-authenticator>`
- :doc:`Andruav Communication Server <technicals/communication/de-comm-technicals-commserver>`
- :doc:`Andruav Facade <technicals/communication/de-comm-technicals-facade>`
- :doc:`Andruav Message Parser <technicals/communication/de-comm-technicals-parser>`
- :doc:`Configuration File Management <technicals/communication/de-comm-technicals-configfile>`

Server Technicals
-----------------

- :doc:`Server Technicals Overview <technicals/server/de-server-technicals>`
- :doc:`Authentication Server Internals <technicals/server/de-server-technicals-authentication>`
- :doc:`Communication Server Internals <technicals/server/de-server-technicals-communication>`
- :doc:`Authentication ↔ Communication Flow <technicals/server/de-server-technicals-auth-comm-flow>`
- :doc:`Mesh Communication Server Relay <technicals/server/de-server-technicals-mesh-relay>`

MAVLink Module Technicals
-------------------------

- :doc:`MAVLink Module Overview <technicals/mavlink/de-mavlink-technicals>`
- :doc:`Flight Control Board Connection <technicals/mavlink/de-mavlink-technicals-fcbconnection>`
- :doc:`Configuration File System <technicals/mavlink/de-mavlink-technicals-configfile>`
- :doc:`Rate Limiting Effects <technicals/mavlink/de-mavlink-technicals-ratelimit>`
- :doc:`Joystick Channels Guided Mode <technicals/mavlink/de-mavlink-technicals-joystick>`
- :doc:`RC Sub Actions <technicals/mavlink/de-mavlink-technicals-rcsubactions>`

Source Code Repositories
------------------------

- `droneengage_communication <https://github.com/DroneEngage/droneengage_communication>`_ - Main communication module
- `droneengage_mavlink <https://github.com/DroneEngage/droneengage_mavlink>`_ - MAVLink interface
- `droneengage_camera <https://github.com/DroneEngage/droneengage_camera>`_ - Camera streaming
- `droneengage_databus <https://github.com/DroneEngage/droneengage_databus>`_ - Plugin development library
- `droneengage_webclient_react <https://github.com/DroneEngage/droneengage_webclient_react>`_ - Web client
