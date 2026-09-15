# MAVLink Module

The **MAVLink Module** (`de_mavlink`, binary `de_ardupilot`) is the bridge between your flight controller and the rest of the DroneEngage system. It runs on the companion computer (for example, a Raspberry Pi) and talks to ArduPilot or PX4 over MAVLink.

## What it does

- Reads telemetry from the flight controller (GPS, attitude, battery, modes, etc.).
- Forwards telemetry to the Communication Module over UDP.
- Receives commands from the WebClient (via the Communication Module) and translates them into MAVLink messages.
- Supports advanced features such as follow-me, swarm, geo-fencing, RC override, and UDP telemetry proxy.
- Runs as a C++ plugin to the Communication broker.

## Supported vehicles and firmware

- **Firmware**: ArduPilot, PX4.
- **Vehicle types**: quadcopter, plane, rover, boat, helicopter, submarine, VTOL, and more.

## Quick links

- [MAVLink configuration](de-config-mavlink.md)
- [Telemetry optimization](webclient-udp-telemetry)
- [Geo-fencing](de-geo-fencing)
- [Swarm](de-swarm)
- [TX Block / RC override](de-tx-block)
- [TX Freeze](de-tx-freeze)

## For developers

- **Repository**: `droneengage_mavlink`
- **Language**: C++17
- **Build**: CMake 3.1+, `build.sh` / `build_release.sh`.
- **Key components**:
  - `fcb_facade.cpp/hpp` — high-level FCB API.
  - `fcb_main.cpp/hpp` — main logic, RC, modes.
  - `fcb_andruav_message_parser.cpp/hpp` — parses commands from DE Comm.
  - `mavlink_sdk/` — reusable MAVLink SDK with serial, UDP, and TCP ports.
- **Configuration file**: `de_mavlink.config.module.json`.
- **Package output**: `build/packages/de-mavlink-plugin-*.deb`, installs to `/home/$USER/drone_engage/de_mavlink/`.

See [MAVLink technicals](technicals/mavlink/de-mavlink-technicals.md) for architecture, configuration internals, and message handling.
