=====================
Scenarios & Use Cases
=====================

This page covers configuration examples, real-world deployments, and common applications for DroneEngage and Andruav.

.. youtube:: Lv9_dq8OgdY

|

.. toctree::
   :caption: Configuration Scenarios
   :titlesonly:
   :maxdepth: 1

   On-Board DroneEngage <de-drone-connection>
   Ground-DroneEngage (Air Unit) <de-drone-ground-config-unit>
   All-In-One Board (RPI as FCB + Companion) <de-all-in-one>
   Camera Naming & Video Pipelines <de-camera-names>
   Andruav + Mission Planner over 4G/5G, with Video <andruav-mp-4g5g>

.. toctree::
   :caption: Real-World Use Cases
   :titlesonly:
   :maxdepth: 1

   First Long Range Intercontinental Controlled Rover 2016 <../use-cases/de-usa-rover>
   DroneEngage Rover in France 2025 <../use-cases/de-france-rover>

|

On-Board DroneEngage
====================

This is the **default DroneEngage installation** (:doc:`de-drone-connection`), where DroneEngage runs on a Raspberry Pi or similar board installed directly on the drone.

Ground-DroneEngage (Air Unit)
=============================

This is a **very suitable configuration** (:doc:`de-drone-ground-config-unit`) for drones that already have telemetry and video links, allowing access via DroneEngage without modifying the onboard systems. It is also ideal when a powerful ground-based computer is needed for AI/ML processing.

All-In-One Board (RPI as FCB + Companion)
=========================================

This configuration uses a single Raspberry Pi 4 board to run both the flight controller (Ardupilot) and the companion computer (DroneEngage), leveraging CPU affinity for real-time performance. More about this configuration can be found in :doc:`de-all-in-one`.

Camera Naming & Video Pipelines
===============================

When multiple cameras are connected, the same camera may not always receive the same device path (e.g., ``/dev/videoX``) after a board restart or when a new camera is connected. This variability can make debugging frustrating and time-consuming.

To address this, DroneEngage creates `virtual camera devices <https://github.com/umlaeute/v4l2loopback>`_ (:doc:`de-camera-names`) using **v4l2loopback**, assigning custom names to each camera source for reliable identification.

Each time cameras are initialized, they may receive a different index (i.e., ``/dev/videoX``, where ``X`` changes across restarts or new connections). DroneEngage eliminates this uncertainty by using custom names, allowing the Camera, Tracker, and AI modules to access cameras by name rather than by device path.

Andruav + Mission Planner over 4G/5G, with Video
=================================================

For the mobile-only setup — two Android phones and Andruav instead of a
Raspberry Pi — see :doc:`andruav-mp-4g5g`. It covers linking the flight
controller, forwarding telemetry into Mission Planner over UDPCI, and
streaming live video, all over a standard 4G/5G or WiFi connection.

|

Common Applications
====================

- **Long-Range FPV** - Stream video over 4G while flying beyond visual line of sight
- **Remote Inspection** - Control drones at remote sites from a central location
- **Fleet Management** - Monitor and control multiple drones from one interface
- **Agricultural Surveys** - Coordinate swarm operations for large area coverage
- **Search & Rescue** - Real-time video and telemetry for emergency response

|

Real-World Use Cases
======================

- :doc:`First Long Range Intercontinental Controlled Rover 2016 <../use-cases/de-usa-rover>` — Andruav's 12,193 km telemetry demo, Cairo to Los Angeles.
- :doc:`DroneEngage Rover in France 2025 <../use-cases/de-france-rover>`
