.. _de-dev-mavlink-sdk-intro:

====================
Introduction
====================

The MAVLink SDK is a lightweight, standalone C++17 library for communicating with ArduPilot-based autopilots. It provides a clean, event-driven API for connecting to drones via UDP, TCP, or Serial interfaces.

This SDK can be used independently of the full DroneEngage system, making it ideal for developers who want to integrate MAVLink communication into their own C++ projects.

Features
--------

**Multiple Connection Types**

- UDP support for SITL, MAVProxy, and network connections
- TCP support for MAVLink routers and proxies
- Serial port support for direct flight controller connections

**Event-Driven Architecture**

- Callback-based notifications for vehicle state changes
- Automatic detection of connection, arm/disarm, mode changes
- Real-time telemetry updates through callbacks

**Vehicle State Management**

- Automatic parsing and storage of MAVLink messages
- Cached telemetry data for easy access
- State detection (armed, flying, ready to arm, motor enabled)
- System ID filtering for multi-vehicle scenarios

**Mission Management**

- Upload waypoint missions to the vehicle
- Download and monitor mission progress
- Clear missions and set active waypoints
- Mission acknowledgment tracking

**Parameter Management**

- Read individual parameters
- Write parameter values
- Request complete parameter list
- Parameter change notifications

**Command Interface**

- High-level API for common drone operations
- Arm/disarm control
- Flight mode changes
- Takeoff and guided navigation
- Altitude control
- Home position and ROI setting
- Yaw control
- Servo and RC channel control
- Emergency flight termination

**Modern C++ Design**

- C++17 standard with smart pointers and RAII patterns
- Singleton pattern for easy access to SDK components
- Thread-safe singleton instances
- Clean, intuitive API

**Autopilot Compatibility**

- ArduPilot support (Copter, Plane, Rover)
- PX4 support
- Automatic handling of firmware differences
- High-latency satellite link support

Project Structure
-----------------

The SDK is organized as follows::

    mavlink_sdk/
    ├── src/
    │   ├── mavlink_sdk.h/cpp        # Main SDK entry point
    │   ├── vehicle.h/cpp            # Vehicle state and telemetry
    │   ├── mavlink_command.h/cpp    # Command API for vehicle control
    │   ├── mavlink_events.h         # Event callback interface
    │   ├── mavlink_waypoint_manager.h/cpp    # Mission management
    │   ├── mavlink_parameter_manager.h/cpp   # Parameter management
    │   ├── mavlink_communicator.h/cpp        # Message routing
    │   ├── mavlink_helper.h/cpp     # Utility functions
    │   ├── generic_port.h           # Abstract port interface
    │   ├── udp_port.h/cpp           # UDP communication
    │   ├── tcp_client_port.h/cpp    # TCP communication
    │   ├── serial_port.h/cpp        # Serial communication
    │   └── helpers/
    │       ├── colors.h             # Console color definitions
    │       └── utils.h              # Utility helpers
    ├── CMakeLists.txt               # CMake build configuration
    └── build.sh                     # Build script

Key Components
--------------

**CMavlinkSDK**

Main entry point for the SDK. Provides connection management (UDP, TCP, Serial) and controls the SDK lifecycle (start/stop).

**CVehicle**

Central component for vehicle state and telemetry. Automatically parses incoming MAVLink messages, maintains cached telemetry data, and triggers callbacks on state changes.

**CMavlinkCommand**

High-level command interface for vehicle control. Provides methods for arming, mode changes, navigation, mission management, and parameter operations.

**CMavlinkEvents**

Abstract callback interface that you inherit from to receive event notifications. Override methods to handle connection events, vehicle state changes, telemetry updates, mission events, and parameter changes.

**CMavlinkWaypointManager**

Handles mission/waypoint operations. Uploads, downloads, and monitors waypoint missions.

**CMavlinkParameterManager**

Manages autopilot parameters. Reads, writes, and tracks parameter values.

**Port Classes**

Abstract communication layer with implementations for UDP, TCP, and Serial connections.

Requirements
------------

- **C++17** compatible compiler (GCC 7+ or Clang 5+)
- **CMake** 3.1.0 or higher
- **MAVLink C library** (c_library_v2) - should be placed at ``../c_library_v2`` relative to the SDK

License
-------

This SDK is provided under the BSD-3-Clause license, consistent with the MAVLink project licensing.

Related Projects
----------------

- `MAVLink <https://mavlink.io/>`_ - MAVLink protocol
- `ArduPilot <https://ardupilot.org/>`_ - ArduPilot autopilot
- `PX4 <https://px4.io/>`_ - PX4 autopilot
