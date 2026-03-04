# de_mavlink Configuration File

A file called **de_mavlink.config.module.json** exists in **/home/pi/drone_engage/de_mavlink/**
This file is written in JSON format. However, you can still add comments to the file.
To those who do not know JSON just consider it a text file that you need to edit only few lines in it.

## Accessing the Configuration File

Login to your Raspberry-PI board using ssh.

```bash
ssh pi@raspberry_pi_ip_address
```

and go to the file

```bash
cd /home/pi/drone_engage/de_mavlink/
ls
```

and open the file 

```bash
nano de_mavlink.config.module.json
```

## Fields Meaning

**module_id**
- Just a name for your module
- Example: "FCB_CTRL"

**s2s_udp_target_ip**
- Points to de_comm listening IP
- Example: "127.0.0.1"

**s2s_udp_target_port**
- de_comm listening port
- Example: "60000"

**s2s_udp_listening_ip**
- This module's listening IP
- Example: "127.0.0.1"

**s2s_udp_listening_port**
- This module's listening port
- Example: "61003"

**s2s_udp_packet_size**
- UDP packet size
- Example: "8192"

**fcb_connection_uri**
- Connection to FCB board
- Example: See examples below

**default_optimization_level**
- Telemetry optimization 0-3
- Example: 2

**udp_proxy_enabled**
- Enable UDP telemetry
- Example: false

**udp_proxy_fixed_port**
- Fixed UDP port (optional)
- Example: 15412

**read_only_mode**
- Block all commands from WebClient
- Example: false

**logger_enabled**
- Enable logging to Logs folder
- Example: true

**logger_debug**
- Enable debug logging
- Example: false

**message_timeouts**
- MAVLink message rate control
- Example: See below

**event_fire_channel**
- Event fire channel
- Example: 16

**event_wait_channel**
- Event wait channel
- Example: 15

**rc_block_channel**
- RC block channel (1-8, -1=off)
- Example: -1

**mavlink_ids**
- MAVLink ID configuration
- Example: See below

**rc_channels**
- RC channel configuration
- Example: See below

**follow_me**
- Follow Me PID settings
- Example: See below

## Connection Examples

### Connecting via TCP:

```json
{
"fcb_connection_uri": 
{
"type": "tcp",
"ip": "127.0.0.1",
"port": 7600
}
}
```

### Connecting via UDP:

```json
{
"fcb_connection_uri": 
{
"type": "udp",
"ip": "0.0.0.0",
"port": 14551
}
}
```

This connection is straightforward using UDP. This is suitable when connecting DroneEngage to boards like [OBAL](https://github.com/HefnySco/OBAL) via OTG Ethernet.

### Connecting to a Serial Port:

#### Static Port:

```json
{
"fcb_connection_uri":
{
"type": "serial",
"port": "/dev/ttyUSB1",
"baudrate": 115200
}
}
```

#### Dynamic Port Search:

```json
{
"fcb_connection_uri":
{
"type": "serial",
"port": "/dev/ttyUSB",
"baudrate": 115200,
"dynamic": true
}
}
```

The **dynamic** field will make the module search for a valid mavlink port from /dev/ttyUSB0 to /dev/ttyUSB10. So even if you unplug and plug it again and the USB appeared on different address, the module will find it. This feature is developed to be able to detect mavlink port from Scan port.

**baudrate** has to match the baudrate defined in FCB. You can open GSC and configure mavlink parameters.

> **Important:** You need to connect TX of RPI to RX of the FCB and vice-versa.

> **Important:** If you want to use the OTG USB port make sure you run **rasp-config** and disable shell but keep serial port enabled.

## MAVLink IDs Configuration

```json
"mavlink_ids": {
    "de_mavlink_gcs_id": 255,
    "only_allow_ardupilot_compid": 0,
    "only_allow_ardupilot_sysid": 0
}
```

- **de_mavlink_gcs_id**: Local GCS system ID (255 = default, -1 = disable heartbeat)
- **only_allow_ardupilot_compid**: Only receive mavlinks from specified component ID (0 = no restriction)
- **only_allow_ardupilot_sysid**: Only receive mavlinks from specified system ID (0 = no restriction)

## RC Channels Configuration

Used for Gamepad control via Drone-Engage Web Client. Determine channels enabled, reverse, max & min PWM range.

```json
"rc_channels": {
    "rc_smart_channels": {
        "active": true,
        "rc_channel_enabled": [1, 1, 1, 1],
        "rc_channel_limits_max": [2000, 2000, 1750, 2000],
        "rc_channel_limits_min": [1000, 1000, 1300, 1000]
    },
    "rc_channel_enabled": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "rc_channel_reverse": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "rc_channel_limits_max": [1850, 2000, 1750, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],
    "rc_channel_limits_min": [1150, 1000, 1300, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
}
```

- **rc_smart_channels**: Optional but recommended settings for ROLL-PITCH-THR-YAW regardless of actual settings on ardupilot
- **rc_channel_enabled**: Array indicating which channels are active (1 = enabled, 0 = disabled)
- **rc_channel_reverse**: Array indicating which channels are reversed (1 = normal, -1 = reversed)
- **rc_channel_limits_max/min**: PWM limits for each channel

## Follow Me Configuration

PID and Expo settings for autonomous tracking functionality:

```json
"follow_me": {
    "PID_P_X": 1.0,
    "PID_P_Y": 1.0,
    "PID_I_X": 0.00,
    "PID_I_Y": 0.00,
    "expo_factor": 0.5,
    "deadband": 0.1,
    "rate_limit": 0.1
}
```

- **PID_P_X/Y**: Proportional gain for X/Y axis tracking (0.1-5.0)
- **PID_I_X/Y**: Integral gain for X/Y axis tracking (0.0-1.0)
- **expo_factor**: Exponential curve for response (0.0-1.0)
- **deadband**: Deadband threshold (0.0-0.5)
- **rate_limit**: Max rate change per second (0.05-0.2)

## Message Timeouts

The message_timeouts section controls the rate at which different MAVLink messages are sent in telemetry mode. Each message type has an array of four values representing different optimization levels (0-3), where 0 is maximum bandwidth and 3 is minimum bandwidth.

Example configuration:
```json
"message_timeouts": {
    "0": [0, 1000, 2000, 3000],      // HEARTBEAT
    "24": [0, 800, 1000, 2000],     // GPS_RAW_INT
    "30": [0, 250, 1000, 2000],     // ATTITUDE
    "33": [0, 250, 1000, 2000],     // GLOBAL_POSITION_INT
    "74": [0, 500, 1000, 2000]      // VFR_HUD
}
```

The array format is `[level_0, level_1, level_2, level_3]` where each value represents the timeout in milliseconds for that optimization level.
