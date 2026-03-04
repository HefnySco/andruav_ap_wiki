# Custom Plugin Development

Writing Custom Plugins allows you to create modules that can handle hardware components such as GPIO or sensors, or perform data processing like image analysis from camera modules. Once you write and integrate these modules using the DataBus library, you can access them from remote units and the DroneEngage Web Client.

## Architecture Overview

The DroneEngage DataBus framework follows a layered architecture that enables seamless communication between custom modules and the main DroneEngage system:

```
+---------------------+
|  Your Application   |
|  (C++/Python/Node)  |
+----------+----------+
           |
           v
+---------------------+
|  DataBus Library    |
|  (Module + Facade)  |
+----------+----------+
           |
           v
+---------------------+
|  UDP Client         |
|  (Chunking/Assembly)|
+----------+----------+
           |
           v
+---------------------+
|  de_comm            |
|  Communicator       |
|  (Port 60000)       |
+---------------------+
```

### Key Components

- **CModule**: Singleton module manager for registration and message handling
- **FacadeBase**: Simplified API for response generation  
- **Message Parser**: Handles JSON/binary message processing and command dispatch
- **UDP Client**: Low-level network communication with automatic chunking

## Core Features

All language implementations provide:

- **Module Registration** - Register your module with the DroneEngage communicator
- **JSON Messaging** - Send and receive structured JSON messages
- **Binary Data Support** - Transmit images, files, and other binary data
- **Message Chunking** - Automatic splitting and reassembly of large messages
- **Message Filtering** - Subscribe to specific message types
- **Thread-Safe Operations** - Concurrent message handling
- **Periodic ID Broadcasting** - Automatic module identification
- **High-Level Facade API** - Simplified interface for common operations

## Quick Start

Choose your preferred language and follow the corresponding guide:

- [C++ Implementation](./de-custom-plugins-cpp.md)
- [Node.js Implementation](./de-custom-plugins-nodejs.md)
- [Python Implementation](./de-custom-plugins-python.md)

## Use Cases

- **Hardware Integration** - GPIO, sensors, actuators
- **Data Processing** - Image processing, telemetry analysis  
- **Custom Telemetry** - Send custom sensor data
- **MAVLink Integration** - Process MAVLink messages
- **Remote Control** - Implement custom control logic
- **Monitoring** - Real-time system monitoring
- **Logging** - Custom data logging modules

## Technical Requirements

### Network Configuration

- Default de_comm port: 60000
- Default module listen ports: 61111-61234
- UDP packet size: 8192 bytes (configurable)
- Message filtering supported via MESSAGE_FILTER arrays

### Language Standards

- **C++**: C++17 standard, camelCase variables, PascalCase classes
- **Python**: Snake_case, type hints in newer code, threading.Lock() for singleton safety
- **Node.js**: camelCase, async/await support, EventEmitter pattern

## See Also

- [General plugin development guide](./de-dev-plugin.md)
- [Available built-in plugins](./de-plugins.md)
- [Complete developer documentation](./de-dev.md)
