.. _de-dev-mavlink-sdk-api:

==============
API Reference
==============

This section provides detailed API documentation for the MAVLink SDK components.

CMavlinkSDK (Main Entry Point)
-------------------------------

The main entry point for the SDK. Provides connection management and controls the SDK lifecycle.

Access via singleton:

.. code-block:: cpp

   mavlinksdk::CMavlinkSDK& sdk = mavlinksdk::CMavlinkSDK::getInstance();

Methods
~~~~~~~

**getInstance()**

Get the singleton instance of the SDK.

.. code-block:: cpp

   static CMavlinkSDK& getInstance();

**connectUDP(ip, port)**

Configure UDP connection.

.. code-block:: cpp

   void connectUDP(const std::string& ip, const int& port);

Parameters:
- ``ip`` - IP address to bind to (e.g., "0.0.0.0" for all interfaces)
- ``port`` - UDP port number

**connectSerial(device, baudrate, dynamic)**

Configure serial connection.

.. code-block:: cpp

   void connectSerial(const std::string& device, const int& baudrate, const bool& dynamic);

Parameters:
- ``device`` - Serial device path (e.g., "/dev/ttyUSB0")
- ``baudrate`` - Baud rate (e.g., 57600, 115200)
- ``dynamic`` - Enable dynamic port detection

**connectTCP(ip, port)**

Configure TCP connection.

.. code-block:: cpp

   void connectTCP(const std::string& ip, const int& port);

Parameters:
- ``ip`` - IP address to connect to
- ``port`` - TCP port number

**start(event_handler)**

Start the SDK with an event handler.

.. code-block:: cpp

   void start(CMavlinkEvents* event_handler);

Parameters:
- ``event_handler`` - Pointer to your event handler instance

**stop()**

Stop the SDK and close connections.

.. code-block:: cpp

   void stop();

**sendMavlinkMessage(msg)**

Send a raw MAVLink message.

.. code-block:: cpp

   void sendMavlinkMessage(const mavlink_message_t& msg);

Parameters:
- ``msg`` - MAVLink message to send

CMavlinkCommand (Vehicle Control)
----------------------------------

High-level command interface for vehicle control.

Access via singleton:

.. code-block:: cpp

   mavlinksdk::CMavlinkCommand& cmd = mavlinksdk::CMavlinkCommand::getInstance();

Methods
~~~~~~~

**doArmDisarm(arm, force)**

Arm or disarm the vehicle.

.. code-block:: cpp

   void doArmDisarm(const bool& arm, const bool& force);

Parameters:
- ``arm`` - True to arm, false to disarm
- ``force`` - Force arm/disarm

**doSetMode(mode, custom_mode, custom_sub_mode)**

Change flight mode.

.. code-block:: cpp

   void doSetMode(const int& mode, const uint32_t& custom_mode = 0, const uint32_t& custom_sub_mode = 0);

Parameters:
- ``mode`` - Flight mode number
- ``custom_mode`` - Custom mode value (optional)
- ``custom_sub_mode`` - Custom sub-mode value (optional)

**takeOff(altitude)**

Initiate takeoff to specified altitude.

.. code-block:: cpp

   void takeOff(const float& altitude);

Parameters:
- ``altitude`` - Target altitude in meters

**gotoGuidedPoint(lat, lon, alt)**

Fly to GPS coordinate.

.. code-block:: cpp

   void gotoGuidedPoint(const double& lat, const double& lon, const double& alt);

Parameters:
- ``lat`` - Latitude in degrees
- ``lon`` - Longitude in degrees
- ``alt`` - Altitude in meters

**changeAltitude(altitude)**

Change target altitude.

.. code-block:: cpp

   void changeAltitude(const float& altitude);

Parameters:
- ``altitude`` - Target altitude in meters

**setHome(yaw, lat, lon, alt)**

Set home position.

.. code-block:: cpp

   void setHome(const float& yaw, const double& lat, const double& lon, const double& alt);

Parameters:
- ``yaw`` - Yaw angle in degrees
- ``lat`` - Latitude in degrees
- ``lon`` - Longitude in degrees
- ``alt`` - Altitude in meters

**setROI(lat, lon, alt)**

Set region of interest.

.. code-block:: cpp

   void setROI(const double& lat, const double& lon, const double& alt);

Parameters:
- ``lat`` - Latitude in degrees
- ``lon`` - Longitude in degrees
- ``alt`` - Altitude in meters

**resetROI()**

Clear region of interest.

.. code-block:: cpp

   void resetROI();

**setYawCondition(angle, rate, clockwise, relative)**

Control yaw.

.. code-block:: cpp

   void setYawCondition(const float& angle, const float& rate, const bool& clockwise, const bool& relative);

Parameters:
- ``angle`` - Target angle in degrees
- ``rate`` - Yaw rate in degrees/second
- ``clockwise`` - True for clockwise rotation
- ``relative`` - True for relative angle

**setNavigationSpeed(type, speed, throttle, relative)**

Set navigation speed.

.. code-block:: cpp

   void setNavigationSpeed(const int& type, const float& speed, const float& throttle, const bool& relative);

Parameters:
- ``type`` - Speed type
- ``speed`` - Speed value
- ``throttle`` - Throttle value
- ``relative`` - True for relative speed

**setServo(channel, pwm)**

Control servo output.

.. code-block:: cpp

   void setServo(const uint8_t& channel, const uint16_t& pwm);

Parameters:
- ``channel`` - Servo channel number
- ``pwm`` - PWM value

**sendRCChannels(channels, length)**

Send RC override.

.. code-block:: cpp

   void sendRCChannels(const uint16_t* channels, const uint8_t& length);

Parameters:
- ``channels`` - Array of RC channel values
- ``length`` - Number of channels

**releaseRCChannels()**

Release RC override.

.. code-block:: cpp

   void releaseRCChannels();

**requestMissionList()**

Request mission from vehicle.

.. code-block:: cpp

   void requestMissionList();

**writeMission(mission_map)**

Upload mission to vehicle.

.. code-block:: cpp

   void writeMission(const std::map<int, mavlink_mission_item_int_t>& mission_map);

Parameters:
- ``mission_map`` - Map of mission items

**clearWayPoints()**

Clear mission on vehicle.

.. code-block:: cpp

   void clearWayPoints();

**setCurrentMission(mission_number)**

Set active waypoint.

.. code-block:: cpp

   void setCurrentMission(const uint16_t& mission_number);

Parameters:
- ``mission_number`` - Mission item number

**readParameter(param_name)**

Read single parameter.

.. code-block:: cpp

   void readParameter(const std::string& param_name);

Parameters:
- ``param_name`` - Parameter name

**writeParameter(param_name, value)**

Write parameter.

.. code-block:: cpp

   void writeParameter(const std::string& param_name, const float& value);

Parameters:
- ``param_name`` - Parameter name
- ``value`` - Parameter value

**requestParametersList()**

Request all parameters.

.. code-block:: cpp

   void requestParametersList();

**cmdTerminateFlight()**

Emergency flight termination.

.. code-block:: cpp

   void cmdTerminateFlight();

**requestHomeLocation()**

Request home position.

.. code-block:: cpp

   void requestHomeLocation();

**sendNative(mavlink_message)**

Send raw MAVLink message.

.. code-block:: cpp

   void sendNative(const mavlink_message_t& mavlink_message);

Parameters:
- ``mavlink_message`` - MAVLink message to send

CVehicle (Vehicle State & Telemetry)
-------------------------------------

Central component for vehicle state and telemetry. Automatically parses incoming MAVLink messages and maintains cached telemetry data.

Access via singleton:

.. code-block:: cpp

   mavlinksdk::CVehicle& vehicle = mavlinksdk::CVehicle::getInstance();

State Detection Methods
~~~~~~~~~~~~~~~~~~~~~~

**isFCBConnected()**

Returns true if heartbeat received within last 3 seconds.

.. code-block:: cpp

   bool isFCBConnected();

**isArmed()**

Returns true if vehicle is armed.

.. code-block:: cpp

   bool isArmed();

**isFlying()**

Returns true if vehicle is in flight (armed + active state).

.. code-block:: cpp

   bool isFlying();

**isReadyToArm()**

Returns true if pre-arm checks passed.

.. code-block:: cpp

   bool isReadyToArm();

**isMotorEnabled()**

Returns true if motors are enabled and healthy.

.. code-block:: cpp

   bool isMotorEnabled();

**hasLidarAltitude()**

Returns true if downward-facing lidar is available.

.. code-block:: cpp

   bool hasLidarAltitude();

Telemetry Accessor Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SDK automatically parses and stores these MAVLink messages. Access them using the following methods:

**Position**

.. code-block:: cpp

   mavlink_global_position_int_t getMsgGlobalPositionInt();
   mavlink_local_position_ned_t getMsgLocalPositionNED();
   mavlink_gps_raw_int_t getMSGGPSRaw();
   mavlink_gps2_raw_t getMSGGPS2Raw();

**Attitude**

.. code-block:: cpp

   mavlink_attitude_t getMsgAttitude();

**Speed**

.. code-block:: cpp

   mavlink_vfr_hud_t getMsgVFRHud();

**Battery**

.. code-block:: cpp

   mavlink_sys_status_t getMsgSysStatus();
   mavlink_battery_status_t getMsgBatteryStatus();
   mavlink_battery2_t getMsgBattery2Status();

**System**

.. code-block:: cpp

   mavlink_heartbeat_t getMsgHeartBeat();
   mavlink_home_position_t getMsgHomePosition();
   mavlink_system_time_t getSystemTime();

**Navigation**

.. code-block:: cpp

   mavlink_nav_controller_output_t getMsgNavController();

**RC and Servos**

.. code-block:: cpp

   mavlink_rc_channels_t getRCChannels();
   mavlink_servo_output_raw_t getServoOutputRaw();

**Sensors**

.. code-block:: cpp

   mavlink_radio_status_t getRadioStatus();
   mavlink_ekf_status_report_t getEkf_status_report();
   mavlink_vibration_t getVibration();
   distance_sensor_t getDistanceSensor(const int& direction);
   mavlink_wind_t getMsgWind();
   mavlink_terrain_report_t getTerrainReport();

**Traffic**

.. code-block:: cpp

   mavlink_adsb_vehicle_t getADSBVechile();

**High Latency**

.. code-block:: cpp

   mavlink_high_latency_t getHighLatency();
   mavlink_high_latency2_t getHighLatency2();
   int getHighLatencyMode();

**Flight Info**

.. code-block:: cpp

   mavlink_flight_information_t getFlightInformation();

System ID Filtering
~~~~~~~~~~~~~~~~~~~

**restrictMessageToSysID(sysid)**

Only accept messages from specific system ID.

.. code-block:: cpp

   void restrictMessageToSysID(const int& sysid);

**restrictMessageToCompID(compid)**

Only accept messages from specific component ID.

.. code-block:: cpp

   void restrictMessageToCompID(const int& compid);

**getSysId()**

Get current system ID of connected vehicle.

.. code-block:: cpp

   int getSysId();

**getCompId()**

Get current component ID of connected vehicle.

.. code-block:: cpp

   int getCompId();

CMavlinkEvents (Callbacks)
---------------------------

Abstract callback interface. Inherit from this class and override methods to receive event notifications.

Connection Events
~~~~~~~~~~~~~~~~

**OnConnected(connected)**

Connection state changed.

.. code-block:: cpp

   virtual void OnConnected(const bool& connected) = 0;

**OnHeartBeat_First(heartbeat)**

First heartbeat received.

.. code-block:: cpp

   virtual void OnHeartBeat_First(const mavlink_heartbeat_t& heartbeat) = 0;

**OnHeartBeat_Resumed(heartbeat)**

Heartbeat resumed after timeout.

.. code-block:: cpp

   virtual void OnHeartBeat_Resumed(const mavlink_heartbeat_t& heartbeat) = 0;

**OnBoardRestarted()**

Flight controller restarted.

.. code-block:: cpp

   virtual void OnBoardRestarted() = 0;

Vehicle State Events
~~~~~~~~~~~~~~~~~~~~

**OnArmed(armed, ready_to_arm)**

Arm state changed.

.. code-block:: cpp

   virtual void OnArmed(const bool& armed, const bool& ready_to_arm) = 0;

**OnFlying(isFlying)**

Flying state changed.

.. code-block:: cpp

   virtual void OnFlying(const bool& isFlying) = 0;

**OnModeChanges(custom_mode, firmware_type, autopilot)**

Flight mode changed.

.. code-block:: cpp

   virtual void OnModeChanges(const uint32_t& custom_mode, const int& firmware_type, 
                              const MAV_AUTOPILOT& autopilot) = 0;

**OnStatusText(severity, status)**

Status message received.

.. code-block:: cpp

   virtual void OnStatusText(const std::uint8_t& severity, const std::string& status) = 0;

**OnACK(cmd, result, result_msg)**

Command acknowledgment received.

.. code-block:: cpp

   virtual void OnACK(const int& cmd, const int& result, const std::string& result_msg) = 0;

Telemetry Events
~~~~~~~~~~~~~~~~

**OnHomePositionUpdated(home_position)**

Home position updated.

.. code-block:: cpp

   virtual void OnHomePositionUpdated(const mavlink_home_position_t& home_position) = 0;

**OnServoOutputRaw(servo_output_raw)**

Servo output changed.

.. code-block:: cpp

   virtual void OnServoOutputRaw(const mavlink_servo_output_raw_t& servo_output_raw) = 0;

**OnEKFStatusReportChanged(ekf_status_report)**

EKF status changed.

.. code-block:: cpp

   virtual void OnEKFStatusReportChanged(const mavlink_ekf_status_report_t& ekf_status_report) = 0;

**OnVibrationChanged(vibration)**

Vibration data updated.

.. code-block:: cpp

   virtual void OnVibrationChanged(const mavlink_vibration_t& vibration) = 0;

**OnDistanceSensorChanged(distance_sensor)**

Distance sensor updated.

.. code-block:: cpp

   virtual void OnDistanceSensorChanged(const distance_sensor_t& distance_sensor) = 0;

**OnADSBVechileReceived(adsb_vehicle)**

ADS-B traffic received.

.. code-block:: cpp

   virtual void OnADSBVechileReceived(const mavlink_adsb_vehicle_t& adsb_vehicle) = 0;

**OnHighLatencyModeChanged(latency_mode)**

High latency mode changed.

.. code-block:: cpp

   virtual void OnHighLatencyModeChanged(const int& latency_mode) = 0;

**OnHighLatencyMessageReceived(latency_mode)**

High latency message received.

.. code-block:: cpp

   virtual void OnHighLatencyMessageReceived(const int& latency_mode) = 0;

Mission Events
~~~~~~~~~~~~~~

**OnWaypointReached(seq)**

Waypoint reached.

.. code-block:: cpp

   virtual void OnWaypointReached(const uint16_t& seq) = 0;

**OnWayPointReceived(mission_item_int)**

Mission item downloaded.

.. code-block:: cpp

   virtual void OnWayPointReceived(const mavlink_mission_item_int_t& mission_item_int) = 0;

**OnWayPointsLoadingCompleted()**

Mission download complete.

.. code-block:: cpp

   virtual void OnWayPointsLoadingCompleted() = 0;

**OnMissionACK(result, mission_type, result_msg)**

Mission acknowledgment.

.. code-block:: cpp

   virtual void OnMissionACK(const int& result, const int& mission_type, 
                             const std::string& result_msg) = 0;

**OnMissionSaveFinished(result, mission_type, result_msg)**

Mission upload complete.

.. code-block:: cpp

   virtual void OnMissionSaveFinished(const int& result, const int& mission_type, 
                                      const std::string& result_msg) = 0;

**OnMissionCurrentChanged(mission_current)**

Active waypoint changed.

.. code-block:: cpp

   virtual void OnMissionCurrentChanged(const uint16_t& mission_current) = 0;

Parameter Events
~~~~~~~~~~~~~~~~

**OnParamReceived(param_name, param_message, changed, first_iteration)**

Parameter received.

.. code-block:: cpp

   virtual void OnParamReceived(const std::string& param_name, 
                                 const mavlink_param_value_t& param_message,
                                 const bool& changed, 
                                 const bool& first_iteration) = 0;

**OnParamReceivedCompleted()**

All parameters received.

.. code-block:: cpp

   virtual void OnParamReceivedCompleted() = 0;

Raw Message Event
~~~~~~~~~~~~~~~~~

**OnMessageReceived(mavlink_message)**

Any MAVLink message received.

.. code-block:: cpp

   virtual void OnMessageReceived(const mavlink_message_t& mavlink_message) = 0;
