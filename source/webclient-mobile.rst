.. _webclient-mobile:

=======================
WebClient — Mobile View
=======================

.. youtube:: cO7825pTuAs

|

A phone-sized ground station that needs no install. Open
`cloud.ardupilot.org:8001/mobile <https://cloud.ardupilot.org:8001/mobile>`_
in any mobile browser, log in with your account and access code, and you
get live map, video, and flight controls sized for a phone screen — the
same account and units as the full :ref:`webclient-whatis`.

|

Map, Status & Flight Controls
==============================

.. image:: ./images/new_andruav_2026/webclient_mobile_andruav_connected.png
   :height: 500px
   :align: center
   :alt: Mobile WebClient connected, showing map, unit status bar, and flight mode buttons

- Status bar with unit selector, signal info, and a speech enable/disable toggle
- Live map with GPS, battery, DFM, altitude, speed, and waypoint readouts
- ARM / AUTO / BRAKE / LAND / GUIDED flight mode buttons
- FPV image viewer with Fit / Contain modes, rotation, and one-tap image save
- Camera dialog with GCS image size toggle and timed capture controls

|

Smart Telemetry — UDP Forwarding to Mission Planner
=====================================================

The same UDP proxy used on the full WebClient is one tap away here too,
useful when you're setting up a Mission Planner link from your phone
instead of a laptop.

.. image:: ./images/new_andruav_2026/webclient_mobile_andruav_telemetry.png
   :height: 500px
   :align: center
   :alt: Smart Telemetry panel showing IP, port, and rate for the UDP proxy

Tap the Smart Telemetry icon, enable it, and copy the IP/port it gives you
into Mission Planner's UDPCI connection. Full detail, including rate
levels, in :ref:`webclient-udp-telemetry`.

|

See it in a full setup: :doc:`scenarios/andruav-mp-4g5g` walks through
pairing this with Andruav over 4G/5G, end to end.
