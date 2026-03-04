# Node.js Plugin Development

The Node.js implementation provides an event-driven, asynchronous interface to the DroneEngage DataBus. It's ideal for web-integrated solutions, real-time applications, and rapid prototyping.

## Features

- **Event-driven Architecture** - Built on Node.js EventEmitter
- **Async/Await Support** - Modern JavaScript patterns
- **NPM Package** - Easy installation and dependency management
- **Complete API Reference** - Comprehensive documentation
- **Cross-platform** - Works on Windows, macOS, and Linux
- **Real-time Communication** - Low-latency UDP messaging
- **Binary Data Support** - Handle images, files, and streams
- **Message Filtering** - Subscribe to specific message types

## Quick Start

### Installation

```bash
cd nodejs
npm install
```

### Basic Usage

```bash
node client.js --help               # Show comprehensive help
node client.js MyModule 60000 61234   # Run with all arguments  
node client.js MyModule              # Uses default ports
```

## Architecture

The Node.js library follows the same layered architecture as other implementations:

### Library Components

```
┌─────────────────────┐
│  Your Application   │
│  (client.js)        │
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│  CFacade_Base       │  ← High-level API
│  (de_facade_base.js)│
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│  CModule            │  ← Module management & routing
│  (de_module.js)     │  ← EventEmitter for async ops
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│  CUDPClient         │  ← UDP transport with chunking
│  (udpClient.js)     │  ← EventEmitter for data events
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│  de_comm            │  ← DroneEngage Communicator
│  (Port 60000)       │
└─────────────────────┘
```

### Key Classes

**CModule (EventEmitter)**
- Module registration and management
- Message routing and filtering
- Event emission for async operations

**CUDPClient (EventEmitter)**
- UDP communication with chunking
- Automatic message reassembly
- Periodic module identification

**CFacade_Base**
- Simplified API for response generation
- Command handling and validation
- Error handling and logging

**AndruavMessageParserBase**
- JSON and binary message parsing
- Command dispatch and routing
- Message validation and filtering

## Usage Examples

### Basic Module Setup

```javascript
const { CModule, CFacade_Base } = require('./de_module');
const { CUDPClient } = require('./udpClient');

class MyFacade extends CFacade_Base {
    handleCommand(request) {
        return {
            status: 'success',
            data: { message: 'Command processed' }
        };
    }
}

// Create module instance
const module = CModule.getInstance();
const facade = new MyFacade();

// Define module properties
module.defineModule('MyModule', '1.0.0', facade);

// Start communication
module.start();
```

### Event-driven Message Handling

```javascript
const module = CModule.getInstance();

// Listen for incoming messages
module.on('message', (message) => {
    console.log('Received:', message);
});

// Listen for connection events
module.on('connected', () => {
    console.log('Connected to DroneEngage communicator');
});

module.on('disconnected', () => {
    console.log('Disconnected from communicator');
});
```

### Binary Data Transmission

```javascript
const fs = require('fs');

// Read image file
const imageData = fs.readFileSync('image.jpg');

// Send binary data
module.sendBinaryData('target_module', imageData, {
    type: 'image',
    format: 'jpeg'
});
```

### Message Filtering

```javascript
// Filter messages by type
module.setMessageFilter(['telemetry', 'command']);

// Custom message handler
module.on('telemetry', (data) => {
    processTelemetryData(data);
});
```

## API Reference

### CModule Class

```javascript
class CModule extends EventEmitter {
    // Singleton access
    static getInstance();
    
    // Module management
    defineModule(name, version, facade);
    start();
    stop();
    
    // Messaging
    sendMessage(target, message);
    sendBinaryData(target, data, metadata);
    
    // Configuration
    setMessageFilter(filters);
    setJsonId(jsonId);
    
    // Events
    on('message', callback);
    on('connected', callback);
    on('disconnected', callback);
    on('error', callback);
}
```

### CUDPClient Class

```javascript
class CUDPClient extends EventEmitter {
    constructor(callback);
    
    // Network operations
    initialize(port);
    sendMessage(data);
    close();
    
    // Events
    on('data', callback);
    on('error', callback);
    on('listening', callback);
}
```

### CFacade_Base Class

```javascript
class CFacade_Base {
    // Abstract method to implement
    handleCommand(request);
    
    // Helper methods
    generateResponse(status, data);
    generateError(message, code);
    validateRequest(request);
}
```

## Package Configuration

### package.json

```json
{
  "name": "droneengage-databus-nodejs",
  "version": "1.0.0",
  "description": "Node.js client for DroneEngage DataBus",
  "main": "client.js",
  "dependencies": {},
  "engines": {
    "node": ">=12.0.0"
  },
  "scripts": {
    "start": "node client.js",
    "test": "node test.js"
  }
}
```

## Code Style

- **Variables**: camelCase (e.g., `moduleName`, `messageData`)
- **Classes**: PascalCase (e.g., `CModule`, `CUDPClient`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `DEFAULT_PORT`, `MAX_PACKET_SIZE`)
- **Files**: snake_case (e.g., `de_module.js`, `udp_client.js`)
- **Functions**: camelCase (e.g., `sendMessage`, `handleCommand`)

## Error Handling

Comprehensive error handling with proper event emission:

```javascript
try {
    await module.sendMessage(target, message);
} catch (error) {
    console.error('Failed to send message:', error);
    module.emit('error', error);
}

// Handle network errors
udpClient.on('error', (error) => {
    console.error('UDP Client error:', error);
    // Implement reconnection logic
});
```

## Performance Considerations

### Memory Management

- Stream processing for large binary data
- Buffer pooling for frequent allocations
- Garbage collection optimization

### Event Loop Optimization

- Non-blocking I/O operations
- Efficient event handling
- Proper error propagation

### Network Optimization

- UDP buffer tuning
- Chunk size optimization
- Connection pooling

## Debugging and Logging

### Logging

Built-in colored console output:

```javascript
const colors = require('./colors');

console.log(colors.info('Info message'));
console.log(colors.error('Error message'));
console.log(colors.success('Success message'));
```

### Debug Mode

Enable debug output:

```bash
DEBUG=* node client.js MyModule
```

## Integration Examples

### Sensor Module Integration

```javascript
const CModule = require('./de_module');
const { CMyFacade } = require('./my_facade');
const { TYPE_AndruavMessage_ServoChannel, NOTIFICATION_TYPE_INFO } = require('./messages');

class SensorFacade extends CMyFacade {
    constructor() {
        super();
        this.sensorData = {
            temperature: 0,
            humidity: 0,
            pressure: 0
        };
    }
    
    readSensorData() {
        // Simulate sensor reading
        this.sensorData.temperature = Math.random() * 30 + 20;
        this.sensorData.humidity = Math.random() * 40 + 30;
        this.sensorData.pressure = Math.random() * 50 + 1000;
        
        return this.sensorData;
    }
    
    sendTelemetry() {
        const data = this.readSensorData();
        this.sendJMSG('', {
            sensor_type: 'environmental',
            data: data,
            timestamp: Date.now()
        }, TYPE_AndruavMessage_ServoChannel, true);
    }
}

// Module setup
const cModule = new CModule();
const sensorFacade = new SensorFacade();
sensorFacade.setModule(cModule);

// Define module
cModule.defineModule(
    'gen',                    // MODULE_CLASS_GENERIC
    'EnvironmentalSensor',
    '123456789012',
    '1.0.0',
    [TYPE_AndruavMessage_ServoChannel]
);

// Add module features
cModule.addModuleFeatures('T');  // MODULE_FEATURE_SENDING_TELEMETRY
cModule.addModuleFeatures('R');  // MODULE_FEATURE_RECEIVING_TELEMETRY

// Initialize communication
cModule.init('0.0.0.0', 60000, '0.0.0.0', 61234, 8192);

// Start sensor data transmission
setInterval(() => {
    sensorFacade.sendTelemetry();
}, 1000);

console.log('Environmental Sensor Module RUNNING');
```

### Servo Control Module

```javascript
const CModule = require('./de_module');
const { CMyFacade } = require('./my_facade');
const { TYPE_AndruavMessage_ServoChannel, TYPE_AndruavMessage_RemoteExecute } = require('./messages');

class ServoFacade extends CMyFacade {
    constructor() {
        super();
        this.servoPositions = new Array(8).fill(1500); // 8 channels, center position
    }
    
    setServoChannel(channel, position) {
        if (channel >= 0 && channel < 8 && position >= 1000 && position <= 2000) {
            this.servoPositions[channel] = position;
            
            // Send servo command to drone
            this.sendJMSG('', {
                command: 'servo',
                channel: channel,
                position: position
            }, TYPE_AndruavMessage_ServoChannel, true);
            
            console.log(`Servo Channel ${channel} set to ${position}μs`);
        }
    }
    
    handleCommand(request) {
        if (request.command === 'set_servo') {
            this.setServoChannel(request.channel, request.position);
            return { status: 'success', message: 'Servo command executed' };
        }
        return { status: 'error', message: 'Unknown command' };
    }
}

// Module setup
const cModule = new CModule();
const servoFacade = new ServoFacade();
servoFacade.setModule(cModule);

// Define module
cModule.defineModule(
    'gen',                    // MODULE_CLASS_GENERIC
    'ServoController',
    '123456789013',
    '1.0.0',
    [TYPE_AndruavMessage_ServoChannel, TYPE_AndruavMessage_RemoteExecute]
);

// Add module features
cModule.addModuleFeatures('T');  // MODULE_FEATURE_SENDING_TELEMETRY
cModule.addModuleFeatures('R');  // MODULE_FEATURE_RECEIVING_TELEMETRY

// Initialize communication
cModule.init('0.0.0.0', 60000, '0.0.0.0', 61235, 8192);

// Example: Control servos based on commands
cModule.on('message', (message) => {
    if (message.type === TYPE_AndruavMessage_RemoteExecute) {
        servoFacade.handleCommand(message.data);
    }
});

console.log('Servo Control Module RUNNING');
```

## See Also

- [Main custom plugins page](./de-custom-plugins.md)
- [C++ implementation](./de-custom-plugins-cpp.md)  
- [Python implementation](./de-custom-plugins-python.md)
- https://nodejs.org/api/events.html - Node.js EventEmitter documentation
