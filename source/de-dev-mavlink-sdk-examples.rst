.. _de-dev-mavlink-sdk-examples:

=============
Code Examples
=============

This section provides complete application examples using the MAVLink SDK.

Complete Application Example
-----------------------------

Here's a complete application that connects to a vehicle, monitors telemetry, and performs basic operations:

.. code-block:: cpp

   #include <iostream>
   #include <thread>
   #include <chrono>
   #include "mavlink_sdk.h"
   #include "mavlink_command.h"
   #include "vehicle.h"

   class DroneController : public mavlinksdk::CMavlinkEvents
   {
   private:
       bool m_connected = false;
       bool m_armed = false;

   public:
       void OnConnected(const bool& connected) override
       {
           m_connected = connected;
           std::cout << "Connected: " << connected << std::endl;
       }

       void OnHeartBeat_First(const mavlink_heartbeat_t& heartbeat) override
       {
           std::cout << "Vehicle detected! Type: " << (int)heartbeat.type << std::endl;
           
           // Request parameters after connection
           mavlinksdk::CMavlinkCommand::getInstance().requestParametersList();
       }

       void OnArmed(const bool& armed, const bool& ready_to_arm) override
       {
           m_armed = armed;
           std::cout << "Armed: " << armed << ", Ready: " << ready_to_arm << std::endl;
       }

       void OnModeChanges(const uint32_t& custom_mode, const int& firmware_type,
                          const MAV_AUTOPILOT& autopilot) override
       {
           std::cout << "Mode: " << custom_mode << std::endl;
       }

       void OnStatusText(const std::uint8_t& severity, const std::string& status) override
       {
           std::cout << "Status [" << (int)severity << "]: " << status << std::endl;
       }

       void OnACK(const int& cmd, const int& result, const std::string& result_msg) override
       {
           std::cout << "ACK for CMD " << cmd << ": " << result_msg << std::endl;
       }

       bool isConnected() const { return m_connected; }
       bool isArmed() const { return m_armed; }
   };

   int main()
   {
       DroneController controller;
       mavlinksdk::CMavlinkSDK& sdk = mavlinksdk::CMavlinkSDK::getInstance();
       mavlinksdk::CMavlinkCommand& cmd = mavlinksdk::CMavlinkCommand::getInstance();
       mavlinksdk::CVehicle& vehicle = mavlinksdk::CVehicle::getInstance();

       // Connect to SITL
       sdk.connectUDP("0.0.0.0", 14550);
       sdk.start(&controller);

       // Wait for connection
       while (!controller.isConnected())
       {
           std::this_thread::sleep_for(std::chrono::milliseconds(100));
       }

       // Wait for vehicle to be ready
       std::this_thread::sleep_for(std::chrono::seconds(2));

       // Example: Set mode to GUIDED (mode 4 for ArduCopter)
       cmd.doSetMode(4);

       std::this_thread::sleep_for(std::chrono::seconds(1));

       // Example: Arm the vehicle
       cmd.doArmDisarm(true, false);

       // Main loop - print telemetry
       for (int i = 0; i < 100; ++i)
       {
           if (vehicle.isFCBConnected())
           {
               auto pos = vehicle.getMsgGlobalPositionInt();
               auto att = vehicle.getMsgAttitude();
               
               std::cout << "Position: " 
                         << pos.lat / 1e7 << ", " 
                         << pos.lon / 1e7 << ", "
                         << pos.relative_alt / 1000.0 << "m" << std::endl;
               
               std::cout << "Attitude: Roll=" << att.roll * 57.3 
                         << " Pitch=" << att.pitch * 57.3 
                         << " Yaw=" << att.yaw * 57.3 << std::endl;
           }
           std::this_thread::sleep_for(std::chrono::milliseconds(500));
       }

       // Cleanup
       sdk.stop();
       return 0;
   }

Telemetry Monitoring Example
-----------------------------

Example of monitoring various telemetry data:

.. code-block:: cpp

   void printTelemetry()
   {
       mavlinksdk::CVehicle& vehicle = mavlinksdk::CVehicle::getInstance();
       
       if (!vehicle.isFCBConnected()) {
           std::cout << "Vehicle disconnected!" << std::endl;
           return;
       }
       
       // Position
       auto gps = vehicle.getMsgGlobalPositionInt();
       std::cout << "Position: " 
                 << gps.lat / 1e7 << ", " 
                 << gps.lon / 1e7 << std::endl;
       std::cout << "Altitude (rel): " << gps.relative_alt / 1000.0 << " m" << std::endl;
       
       // Attitude
       auto att = vehicle.getMsgAttitude();
       std::cout << "Roll: " << att.roll * 57.3 << "°" << std::endl;
       std::cout << "Pitch: " << att.pitch * 57.3 << "°" << std::endl;
       std::cout << "Yaw: " << att.yaw * 57.3 << "°" << std::endl;
       
       // Speed
       auto hud = vehicle.getMsgVFRHud();
       std::cout << "Groundspeed: " << hud.groundspeed << " m/s" << std::endl;
       std::cout << "Airspeed: " << hud.airspeed << " m/s" << std::endl;
       std::cout << "Throttle: " << hud.throttle << "%" << std::endl;
       
       // Battery
       auto sys = vehicle.getMsgSysStatus();
       std::cout << "Battery: " << sys.voltage_battery / 1000.0 << " V" << std::endl;
       std::cout << "Current: " << sys.current_battery / 100.0 << " A" << std::endl;
       std::cout << "Remaining: " << (int)sys.battery_remaining << "%" << std::endl;
       
       // GPS Quality
       auto gps_raw = vehicle.getMSGGPSRaw();
       std::cout << "GPS Fix: " << (int)gps_raw.fix_type << std::endl;
       std::cout << "Satellites: " << (int)gps_raw.satellites_visible << std::endl;
       
       // Status
       std::cout << "Armed: " << vehicle.isArmed() << std::endl;
       std::cout << "Flying: " << vehicle.isFlying() << std::endl;
       std::cout << "Ready to Arm: " << vehicle.isReadyToArm() << std::endl;
       
       // Home
       auto home = vehicle.getMsgHomePosition();
       std::cout << "Home: " << home.latitude / 1e7 << ", " 
                 << home.longitude / 1e7 << std::endl;
       
       // Navigation
       auto nav = vehicle.getMsgNavController();
       std::cout << "WP Distance: " << nav.wp_dist << " m" << std::endl;
       std::cout << "Alt Error: " << nav.alt_error << " m" << std::endl;
       
       // Lidar altitude (if available)
       if (vehicle.hasLidarAltitude()) {
           auto lidar = vehicle.getLidarAltitude();
           std::cout << "Lidar Alt: " << lidar.current_distance / 100.0 << " m" << std::endl;
       }
   }

System ID Filtering Example
---------------------------

Example of restricting messages to a specific vehicle:

.. code-block:: cpp

   mavlinksdk::CVehicle& vehicle = mavlinksdk::CVehicle::getInstance();

   // Only accept messages from system ID 1
   vehicle.restrictMessageToSysID(1);

   // Only accept messages from component ID 1 (autopilot)
   vehicle.restrictMessageToCompID(1);

   // Get current system/component ID of connected vehicle
   int sysid = vehicle.getSysId();
   int compid = vehicle.getCompId();

   std::cout << "Connected to System ID: " << sysid 
             << ", Component ID: " << compid << std::endl;

Distance Sensor Example
------------------------

Example of accessing distance sensor data:

.. code-block:: cpp

   mavlinksdk::CVehicle& vehicle = mavlinksdk::CVehicle::getInstance();

   // Get downward-facing lidar (altitude)
   auto lidar = vehicle.getLidarAltitude();
   std::cout << "Altitude: " << lidar.current_distance << " cm" << std::endl;

   // Get specific orientation
   auto front = vehicle.getDistanceSensor(MAV_SENSOR_ROTATION_NONE);        // Forward
   auto back = vehicle.getDistanceSensor(MAV_SENSOR_ROTATION_YAW_180);      // Backward
   auto down = vehicle.getDistanceSensor(MAV_SENSOR_ROTATION_PITCH_270);    // Down (lidar)

High Latency Mode Example
--------------------------

Example of handling high-latency satellite links:

.. code-block:: cpp

   mavlinksdk::CVehicle& vehicle = mavlinksdk::CVehicle::getInstance();

   int mode = vehicle.getHighLatencyMode();
   // 0 = Normal mode
   // MAVLINK_MSG_ID_HIGH_LATENCY = High latency v1
   // MAVLINK_MSG_ID_HIGH_LATENCY2 = High latency v2

   if (mode == MAVLINK_MSG_ID_HIGH_LATENCY2) {
       auto hl2 = vehicle.getHighLatency2();
       // Use high latency data
       std::cout << "High latency mode active" << std::endl;
   }

Guided Mode Position Tracking
------------------------------

Example of tracking guided mode position for altitude changes:

.. code-block:: cpp

   mavlinksdk::CVehicle& vehicle = mavlinksdk::CVehicle::getInstance();

   // Set current guided target (called internally when gotoGuidedPoint is used)
   vehicle.setGuidedPoint(latitude, longitude, relative_altitude);

   // Get position for altitude change commands
   LOCATION_3D pos = vehicle.getPositionforChangeAltitude();

Message Timestamps Example
---------------------------

Example of tracking when messages were last received:

.. code-block:: cpp

   mavlinksdk::CVehicle& vehicle = mavlinksdk::CVehicle::getInstance();

   // Get timestamp of last GPS message (microseconds)
   uint64_t gps_time = vehicle.getMessageTime(MAVLINK_MSG_ID_GLOBAL_POSITION_INT);

   // Check if message has been processed
   uint16_t flags = vehicle.getProcessedFlag(MAVLINK_MSG_ID_ATTITUDE);
   if (flags == MESSAGE_UNPROCESSED) {
       // New data available
       vehicle.setProcessedFlag(MAVLINK_MSG_ID_ATTITUDE, MESSAGE_PROCESSED);
   }

Connection Examples
------------------

**SITL (Software In The Loop)**

.. code-block:: cpp

   // Connect to ArduPilot SITL default port
   sdk.connectUDP("0.0.0.0", 14550);

**MAVProxy**

.. code-block:: cpp

   // Connect to MAVProxy output
   sdk.connectUDP("127.0.0.1", 14550);

**Pixhawk via USB**

.. code-block:: cpp

   // Linux
   sdk.connectSerial("/dev/ttyACM0", 115200, false);

   // Or with dynamic port detection
   sdk.connectSerial("/dev/ttyACM0", 115200, true);

**Telemetry Radio**

.. code-block:: cpp

   // 3DR Radio or similar at 57600 baud
   sdk.connectSerial("/dev/ttyUSB0", 57600, false);

**TCP Connection**

.. code-block:: cpp

   // Connect to MAVLink router or proxy
   sdk.connectTCP("192.168.1.100", 5760);

Thread Safety Notes
-------------------

- The SDK uses internal threading for message reception
- Callbacks are invoked from the communication thread
- Use appropriate synchronization when accessing shared data from callbacks
- The singleton instances are thread-safe for access
