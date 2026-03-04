# Developer Guide

This section provides technical documentation for developers who want to build DroneEngage from source, create custom plugins, or understand the internal architecture.


## Overview

DroneEngage is built with a modular architecture:

- **de_comm** - Communication module (connects to cloud server)
- **de_mavlink** - MAVLink module (connects to flight controller)
- **de_camera** - Camera module (video streaming and recording)
- **Plugins** - Custom modules for GPIO, SDR, tracking, etc.

All modules communicate via the **DataBus** using UDP sockets, allowing them to run on the same device or distributed across multiple devices.

## Building & Setup

- [Building from Source](de-dev-building-code.md)

## Architecture

- [Communication Protocol](de-dev-andruav-communication-protocol.md)
- [DataBus (Inter-Module Communication)](de-dev-databus.md)

## Extending DroneEngage

- [Creating Custom Plugins](de-dev-plugin.md)
- [Custom Plugin Development](de-custom-plugins.md)
- [C++ Plugin Development](de-custom-plugins-cpp.md)
- [Node.js Plugin Development](de-custom-plugins-nodejs.md)
- [Python Plugin Development](de-custom-plugins-python.md)
- [SWARM Logic](de-dev-swarm.md)
- [Communication Module Config](de-config-comm.md)
- [MAVLink Module Config](de-config-mavlink.md)

## Web Client Technicals

- [Web Client Overview](technicals/webclient/de-web-technicals.md)
- [Authentication System](technicals/webclient/de-web-technicals-authentication.md)
- [Configuration Management](technicals/webclient/de-web-technicals-configuration.md)
- [Server Communication](technicals/webclient/de-web-technicals-servercomm.md)
- [Site Configuration](technicals/webclient/de-web-technicals-siteconfig.md)
- [Unit Management](technicals/webclient/de-web-technicals-unit.md)
- [WebRTC Video Streaming](technicals/webclient/de-web-technicals-webrtc.md)
- [Mission Planning Base](technicals/webclient/de-web-technicals-moduleplanning.md)

## Communication Module Technicals

- [Communication Module Overview](technicals/communication/de-comm-technicals.md)
- [Andruav Authenticator](technicals/communication/de-comm-technicals-authenticator.md)
- [Andruav Communication Server](technicals/communication/de-comm-technicals-commserver.md)
- [Andruav Facade](technicals/communication/de-comm-technicals-facade.md)
- [Andruav Message Parser](technicals/communication/de-comm-technicals-parser.md)
- [Configuration File Management](technicals/communication/de-comm-technicals-configfile.md)

## MAVLink Module Technicals

- [MAVLink Module Overview](technicals/mavlink/de-mavlink-technicals.md)
- [Flight Control Board Connection](technicals/mavlink/de-mavlink-technicals-fcbconnection.md)
- [Configuration File System](technicals/mavlink/de-mavlink-technicals-configfile.md)
- [Rate Limiting Effects](technicals/mavlink/de-mavlink-technicals-ratelimit.md)
- [Joystick Channels Guided Mode](technicals/mavlink/de-mavlink-technicals-joystick.md)
- [RC Sub Actions](technicals/mavlink/de-mavlink-technicals-rcsubactions.md)


## Source Code Repositories

- [droneengage_communication](https://github.com/DroneEngage/droneengage_communication) - Main communication module
- [droneengage_mavlink](https://github.com/DroneEngage/droneengage_mavlink) - MAVLink interface
- [droneengage_camera](https://github.com/DroneEngage/droneengage_camera) - Camera streaming
- [droneengage_databus](https://github.com/DroneEngage/droneengage_databus) - Plugin development library
- [droneengage_webclient_react](https://github.com/DroneEngage/droneengage_webclient_react) - Web client
