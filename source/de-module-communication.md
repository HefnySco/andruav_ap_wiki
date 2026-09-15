# Communication Module

The **Communication Module** (`de_comm`, binary `de_comm`) is the UDP-based broker that lives on the drone or companion computer. It coordinates between the MAVLink module, camera modules, custom plugins, and the cloud Communication Server.

## What it does

- Runs as a local broker on the companion computer.
- Connects plugins (MAVLink, camera, custom) via UDP.
- Maintains an encrypted WebSocket uplink to the DroneEngage Communication Server.
- Routes messages between local modules and the cloud.
- Implements the DroneEngage/Andruav message protocol over UDP and WebSocket.

## When to use it

Every DroneEngage vehicle needs this module. It is the glue between the flight controller interface and the cloud.

## Quick links

- [Communication configuration](de-config-comm.md)
- [Custom plugins overview](technicals/de_common/de-custom-plugins)
- [DataBus protocol](de-dev-databus.md)
- [Plugin development](de-dev-plugin)

## For developers

- **Repository**: `droneengage_communication`
- **Language**: C++17
- **Build**: CMake 3.10+, Boost 1.74+, `build.sh`.
- **Architecture**: plugin-broker pattern.
  - **Plugin side**: `CModule`, `CUDPClient`, `CFacade_Base`.
  - **Broker side**: `CUavosModulesManager`, `CUDPCommunicator`, `CMessageBuffer`.
- **Configuration file**: `de_comm.config.module.json`.
- **Package output**: `build/de-communicator-pro-*.deb`, installs to `$HOME/drone_engage/de_comm/`.

See [Communication technicals](technicals/communication/de-comm-technicals.md) for the plugin-broker architecture, message protocol, and build details.
