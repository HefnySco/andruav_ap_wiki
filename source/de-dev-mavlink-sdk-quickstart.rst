.. _de-dev-mavlink-sdk-quickstart:

==================
Quick Start Guide
==================

This guide will help you get started with the MAVLink SDK in just a few minutes.

Step 1: Include Headers
----------------------

Include the necessary SDK headers in your application:

.. code-block:: cpp

   #include "mavlink_sdk.h"
   #include "mavlink_command.h"
   #include "vehicle.h"

Step 2: Create Event Handler
----------------------------

Inherit from ``mavlinksdk::CMavlinkEvents`` and override the callbacks you need:

.. code-block:: cpp

   class MyDroneHandler : public mavlinksdk::CMavlinkEvents
   {
   public:
       void OnConnected(const bool& connected) override
       {
           std::cout << "Connection status: " << connected << std::endl;
       }

       void OnHeartBeat_First(const mavlink_heartbeat_t& heartbeat) override
       {
           std::cout << "First heartbeat received!" << std::endl;
       }

       void OnArmed(const bool& armed, const bool& ready_to_arm) override
       {
           std::cout << "Armed: " << armed << ", Ready: " << ready_to_arm << std::endl;
       }

       void OnModeChanges(const uint32_t& custom_mode, const int& firmware_type, 
                          const MAV_AUTOPILOT& autopilot) override
       {
           std::cout << "Mode changed to: " << custom_mode << std::endl;
       }

       void OnMessageReceived(const mavlink_message_t& mavlink_message) override
       {
           // Handle raw MAVLink messages if needed
       }
   };

Step 3: Initialize and Connect
------------------------------

Create your main application to initialize the SDK and connect to a vehicle:

.. code-block:: cpp

   int main()
   {
       MyDroneHandler handler;
       
       // Get SDK instance
       mavlinksdk::CMavlinkSDK& sdk = mavlinksdk::CMavlinkSDK::getInstance();
       
       // Connect via UDP (e.g., to SITL or MAVProxy)
       sdk.connectUDP("0.0.0.0", 14550);
       
       // Or connect via Serial
       // sdk.connectSerial("/dev/ttyUSB0", 57600, false);
       
       // Or connect via TCP
       // sdk.connectTCP("127.0.0.1", 5760);
       
       // Start the SDK with your event handler
       sdk.start(&handler);
       
       // Your application loop here...
       
       // Cleanup
       sdk.stop();
       return 0;
   }

Connection Types
----------------

**UDP Connection**

Connect to SITL or MAVProxy:

.. code-block:: cpp

   sdk.connectUDP("0.0.0.0", 14550);

**Serial Connection**

Connect to a flight controller via USB or telemetry radio:

.. code-block:: cpp

   // Linux - Pixhawk via USB
   sdk.connectSerial("/dev/ttyACM0", 115200, false);
   
   // Or with dynamic port detection
   sdk.connectSerial("/dev/ttyACM0", 115200, true);
   
   // Telemetry radio at 57600 baud
   sdk.connectSerial("/dev/ttyUSB0", 57600, false);

**TCP Connection**

Connect to a MAVLink router or proxy:

.. code-block:: cpp

   sdk.connectTCP("192.168.1.100", 5760);

Next Steps
----------

- :doc:`API Reference <de-dev-mavlink-sdk-api>` - Learn about all available methods
- :doc:`Code Examples <de-dev-mavlink-sdk-examples>` - See complete application examples
- :doc:`Integration Guide <de-dev-mavlink-sdk-integration>` - Integrate the SDK into your project

Common Callbacks
----------------

Here are the most commonly used callbacks you might want to implement:

**Connection Events**

- ``OnConnected(connected)`` - Connection state changed
- ``OnHeartBeat_First(heartbeat)`` - First heartbeat received
- ``OnHeartBeat_Resumed(heartbeat)`` - Heartbeat resumed after timeout

**Vehicle State Events**

- ``OnArmed(armed, ready_to_arm)`` - Arm state changed
- ``OnFlying(isFlying)`` - Flying state changed
- ``OnModeChanges(custom_mode, firmware_type, autopilot)`` - Flight mode changed
- ``OnStatusText(severity, status)`` - Status message received
- ``OnACK(cmd, result, result_msg)`` - Command acknowledgment received

**Telemetry Events**

- ``OnHomePositionUpdated(home_position)`` - Home position updated
- ``OnServoOutputRaw(servo_output_raw)`` - Servo output changed
- ``OnEKFStatusReportChanged(ekf_status_report)`` - EKF status changed
- ``OnVibrationChanged(vibration)`` - Vibration data updated

**Mission Events**

- ``OnWaypointReached(seq)`` - Waypoint reached
- ``OnWayPointsLoadingCompleted()`` - Mission download complete
- ``OnMissionSaveFinished(result, mission_type, result_msg)`` - Mission upload complete

**Parameter Events**

- ``OnParamReceived(param_name, param_message, changed, first_iteration)`` - Parameter received
- ``OnParamReceivedCompleted()`` - All parameters received
