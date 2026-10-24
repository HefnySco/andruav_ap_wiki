.. _de-dev-mavlink-sdk:

===========================
MAVLink SDK Library
===========================

A lightweight, standalone C++17 MAVLink SDK for communicating with ArduPilot-based autopilots. This SDK provides a clean, event-driven API for connecting to drones via UDP, TCP, or Serial interfaces.

The MAVLink SDK can be used as a standalone library in your own C++ projects, independent of the full DroneEngage system.

.. toctree::
   :titlesonly:
   :maxdepth: 1

   Introduction <de-dev-mavlink-sdk-intro>
   Building the SDK <de-dev-mavlink-sdk-building>
   Quick Start Guide <de-dev-mavlink-sdk-quickstart>
   API Reference <de-dev-mavlink-sdk-api>
   Code Examples <de-dev-mavlink-sdk-examples>
   Integration Guide <de-dev-mavlink-sdk-integration>

Overview
--------

The MAVLink SDK provides:

- **Multiple Connection Types**: UDP, TCP, and Serial port support
- **Event-Driven Architecture**: Callback-based notifications for vehicle state changes
- **Vehicle State Management**: Automatic parsing and storage of MAVLink messages
- **Mission Management**: Upload, download, and monitor waypoint missions
- **Parameter Management**: Read and write autopilot parameters
- **Command Interface**: High-level API for common drone operations
- **C++17**: Modern C++ with smart pointers and RAII patterns
- **Singleton Pattern**: Easy access to SDK components
- **ArduPilot & PX4 Support**: Compatible with both autopilot firmwares

Documentation Sections
----------------------

- :doc:`Introduction <de-dev-mavlink-sdk-intro>` - SDK overview, features, and project structure
- :doc:`Building the SDK <de-dev-mavlink-sdk-building>` - Build instructions and requirements
- :doc:`Quick Start Guide <de-dev-mavlink-sdk-quickstart>` - Get started with your first application
- :doc:`API Reference <de-dev-mavlink-sdk-api>` - Detailed API documentation
- :doc:`Code Examples <de-dev-mavlink-sdk-examples>` - Complete application examples
- :doc:`Integration Guide <de-dev-mavlink-sdk-integration>` - CMake integration and linking

Source Code
-----------

The MAVLink SDK source code is available at:

`droneengage_mavlink <https://github.com/DroneEngage/droneengage_mavlink>`_ - MAVLink interface with standalone SDK

The SDK is located in the ``mavlink_sdk/`` subdirectory of the repository.
