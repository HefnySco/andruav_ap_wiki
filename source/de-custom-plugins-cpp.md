# C++ Plugin Development

The C++ implementation provides high-performance, low-latency communication with the DroneEngage DataBus. It's ideal for performance-critical applications and hardware integration.

## Features

- **C++17 Standard** - Modern C++ features and best practices
- **High Performance** - Optimized for real-time applications
- **Comprehensive Examples** - Sample applications for various use cases
- **Complete API Reference** - Detailed documentation of all classes
- **Binary Data Transmission** - Efficient handling of images and files
- **MAVLink Integration** - Built-in support for MAVLink messages
- **Adaptive Rate Control** - Dynamic data rate management
- **Queue-based Processing** - Asynchronous message handling

## Quick Start

### Installation

```bash
cd client
mkdir build && cd build
cmake ..
make
```

### Basic Usage

```bash
./client --help                    # Show comprehensive help
./client MyModule 60000 61111      # Run with all arguments
./client MyModule                  # Uses default ports
```

## Architecture

The C++ implementation consists of several key components:

### Core Classes

**CModule**
- Singleton module manager
- Handles module registration and message routing
- Thread-safe operations

**CUDPClient** 
- UDP communication with automatic chunking
- Message reassembly for large payloads
- Periodic module identification broadcasting

**FacadeBase**
- Simplified API for response generation
- Template method pattern for message parsing
- Observer pattern for message callbacks

**Message Parser**
- JSON and binary message processing
- Command dispatch and handling
- Error handling and validation

## Examples

The C++ implementation includes comprehensive examples demonstrating all aspects of module communication:

### 1. Basic Module Communication (client.cpp)

**Purpose:** Demonstrates basic module registration, help system, and periodic message sending.

**Usage:**
```bash
./client [OPTIONS] MODULE_NAME [DE_COMM_PORT] [LISTEN_PORT]
./client sample_mod_cpp 60000 61111
./client CPP_Plugin                    # Uses default ports
./client --help                        # Show help
```

**Key Features:**
- Comprehensive help system with colored output
- Module registration with random ID generation
- Flexible argument parsing with defaults
- Input validation with clear error messages
- Periodic message transmission (every 1 second)
- Demonstrates `sendJMSG()` for JSON messages
- Empty message filter (receives no messages)
- Appears in WebClient Details tab

**Code Highlights:**
```cpp
// Help system with colored output
void printUsage() {
    std::cout << _INFO_CONSOLE_BOLD_TEXT << "DroneEngage C++ Client Module" << _NORMAL_CONSOLE_TEXT_ << std::endl;
    std::cout << _SUCCESS_CONSOLE_BOLD_TEXT_ << "USAGE:" << _NORMAL_CONSOLE_TEXT_ << std::endl;
    std::cout << "  ./client [OPTIONS] MODULE_NAME [DE_COMM_PORT] [LISTEN_PORT]" << std::endl;
    // ... comprehensive help output
}

// Argument parsing with defaults and validation
if (argc < 2) {
    printUsage();
    return 1;
}

// Parse optional port arguments with error handling
int target_port = (argc >= 3) ? std::stoi(argv[2]) : 60000;
int listen_port = (argc >= 4) ? std::stoi(argv[3]) : 61111;

// Define module with random ID
cModule.defineModule(
    MODULE_CLASS_GENERIC,
    module_name,
    module_id,
    "0.0.1",
    Json_de::array()  // Empty message filter
);

// Add module features
cModule.addModuleFeatures(MODULE_FEATURE_SENDING_TELEMETRY);
cModule.addModuleFeatures(MODULE_FEATURE_RECEIVING_TELEMETRY);

// Initialize connection
cModule.init("0.0.0.0", target_port, "0.0.0.0", listen_port, DEFAULT_UDP_DATABUS_PACKET_SIZE);

// Send JSON message
Json_de message = {{"t", "THIS IS A TEST MESSAGE"}, {"long", "..."}};
cModule.sendJMSG("", message, TYPE_AndruavMessage_DUMMY, true);
```

---

### 2. Binary Data Transmission (image_sender.cpp)

**Purpose:** Demonstrates sending binary data (images) through the databus.

**Usage:**
```bash
./image_sender <image_file_path>
./image_sender ./img.jpeg
```

**Key Features:**
- Reads binary files (images) from disk
- Sends binary data using `sendBMSG()` method
- Transmits image every 10 seconds
- Includes metadata (lat, lng, alt, timestamp)
- Connects to default port 60000

**Code Highlights:**
```cpp
// Read binary file
readBinaryFile(file_name, content, content_length);

// Prepare metadata
Json_de msg_cmd;
msg_cmd["lat"] = 0;
msg_cmd["lng"] = 0;
msg_cmd["alt"] = 0;
msg_cmd["tim"] = get_time_usec();

// Send binary message
cModule.sendBMSG("", content, content_length, TYPE_AndruavMessage_IMG, false, msg_cmd);
```

---

### 3. MAVLink Message Handling (mavlink_listener.cpp)

**Purpose:** Demonstrates receiving MAVLink messages and using the facade API.

**Usage:**
```bash
./mavlink_listener
```

**Key Features:**
- Subscribes to MAVLink message types
- Uses `CFacade_Base` for high-level API access
- Implements `onReceive()` callback for message handling
- Demonstrates message filtering with extensive filter list
- Sends notification messages via facade

**Code Highlights:**
```cpp
// Define message filter for MAVLink and other messages
#define MESSAGE_FILTER {TYPE_AndruavMessage_MAVLINK, TYPE_AndruavMessage_SWARM_MAVLINK, ...}

// Set receive callback
cModule.setMessageOnReceive(&onReceive);

// Use facade to send messages
CFacade_Base facade_base;
facade_base.sendErrorMessage(std::string(""), 0, ERROR_USER_DEFINED, 
                             NOTIFICATION_TYPE_INFO, "Hello World mavlink_listener.");

// Handle received messages
void onReceive(const char* message, int len, Json_de jMsg) {
    const int msgid = jMsg[ANDRUAV_PROTOCOL_MESSAGE_TYPE].get<int>();
    // Process incoming messages
}
```

---

### 4. Adaptive Rate Control - Sender (sender_adapter.cpp)

**Purpose:** Demonstrates adaptive message sending with rate control based on receiver feedback.

**Usage:**
```bash
./sender_adapter <module_name> <DE_COMM_PORT> [rate_ms]
./sender_adapter sender_mod 60000 1000
```

**Key Features:**
- Sends messages at configurable rate (default 1000ms)
- Listens for rate adjustment commands
- Uses custom message types (`TYPE_AndruavMessage_USER_RANGE_START`)
- Dynamic rate adjustment based on receiver feedback
- Message counter for tracking

**Code Highlights:**
```cpp
// Define custom message types
#define TYPE_CUSTOM_SOME_DATA     TYPE_AndruavMessage_USER_RANGE_START+0
#define TYPE_CUSTOM_CHANGE_RATE   TYPE_AndruavMessage_USER_RANGE_START+1

// Subscribe to custom messages
#define MESSAGE_FILTER {TYPE_AndruavMessage_USER_RANGE_START+1, TYPE_AndruavMessage_USER_RANGE_START+2}

// Handle rate change requests
void onReceive(const char* message, int len, Json_de jMsg) {
    if (msgid == TYPE_CUSTOM_CHANGE_RATE) {
        const int delta_delay = jMsg["ms"]["value"].get<int>();
        if (delta_delay == 0) {
            delay = delay / 2;  // Speed up
        } else {
            delay += delta_delay;  // Adjust rate
        }
    }
}

// Send data with counter
Json_de message = {{"t", "SENDING DATA"}, {"counter", counter}};
cModule.sendJMSG("", message, TYPE_AndruavMessage_USER_RANGE_START, true);
```

---

### 5. Queue-Based Processing - Receiver (receiver_adapter.cpp)

**Purpose:** Demonstrates message queuing, processing, and adaptive rate control feedback.

**Usage:**
```bash
./receiver_adapter <module_name> <DE_COMM_PORT> [processing_delay_ms]
./receiver_adapter receiver_mod 60000 1000
```

**Key Features:**
- Thread-safe message queue with mutex protection
- Asynchronous message processing
- Queue depth monitoring
- Sends feedback to sender to adjust transmission rate
- Demonstrates backpressure handling

**Code Highlights:**
```cpp
// Thread-safe queue
std::queue<std::vector<char>> messageQueue;
std::mutex messageQueueMutex;
std::condition_variable messageQueueConditionVariable;

// Receive and queue messages
void onReceive(const char* message, int len, Json_de jMsg) {
    std::vector<char> msg(message, message + len);
    std::unique_lock<std::mutex> lock(messageQueueMutex, std::defer_lock);
    
    if (lock.try_lock()) {
        messageQueue.push(msg);
        messageQueueConditionVariable.notify_one();
        lock.unlock();
    }
}

// Process messages and send feedback
void processMessages() {
    while (messageQueue.size() > 0) {
        // Process message with delay
        std::this_thread::sleep_for(std::chrono::milliseconds(delay));
        
        // Adjust sender rate based on queue depth
        if (counter > 2 && diff > 0) {
            sendMsg(+2 * counter);  // Tell sender to slow down
        } else {
            sendMsg(0);  // Tell sender to speed up
        }
    }
}
```

## Common Patterns

### Help System Implementation

Modern C++ clients should include comprehensive help systems:

```cpp
void printUsage() {
    std::cout << _INFO_CONSOLE_BOLD_TEXT << "Application Name" << _NORMAL_CONSOLE_TEXT_ << std::endl;
    std::cout << std::endl;
    std::cout << _SUCCESS_CONSOLE_BOLD_TEXT_ << "USAGE:" << _NORMAL_CONSOLE_TEXT_ << std::endl;
    std::cout << "  ./app [OPTIONS] REQUIRED_ARG [OPTIONAL_ARG1] [OPTIONAL_ARG2]" << std::endl;
    std::cout << std::endl;
    std::cout << _SUCCESS_CONSOLE_BOLD_TEXT_ << "ARGUMENTS:" << _NORMAL_CONSOLE_TEXT_ << std::endl;
    std::cout << "  REQUIRED_ARG    Description of required argument" << std::endl;
    std::cout << "  OPTIONAL_ARG1   Description of optional argument (default: value)" << std::endl;
    std::cout << std::endl;
    std::cout << _SUCCESS_CONSOLE_BOLD_TEXT_ << "OPTIONS:" << _NORMAL_CONSOLE_TEXT_ << std::endl;
    std::cout << "  -h, --help     Show this help message and exit" << std::endl;
}

int main(int argc, char* argv[]) {
    // Check for help flags
    bool showHelp = false;
    if (argc > 1) {
        std::string arg1(argv[1]);
        if (arg1 == "-h" || arg1 == "--help") {
            showHelp = true;
        }
    }

    // Show help if requested or missing required args
    if (showHelp || argc < 2) {
        printUsage();
        return showHelp ? 0 : 1;
    }

    // Parse arguments with validation
    try {
        std::string required_arg = argv[1];
        int optional_arg1 = (argc >= 3) ? std::stoi(argv[2]) : DEFAULT_VALUE;
        // ... continue with application logic
    } catch (const std::exception& e) {
        std::cout << _ERROR_CONSOLE_TEXT_ << "Error: " << e.what() << _NORMAL_CONSOLE_TEXT_ << std::endl;
        return 1;
    }
}
```

### Module Initialization

All examples follow this initialization pattern:

```cpp
// 1. Get module singleton
CModule& cModule = CModule::getInstance();

// 2. Define module
cModule.defineModule(
    MODULE_CLASS_GENERIC,    // Module class
    "module_name",           // Display name
    "unique_id",             // Unique identifier
    "0.0.1",                 // Version
    Json_de::array()         // Message filter (empty or with types)
);

// 3. Add features (optional)
cModule.addModuleFeatures(MODULE_FEATURE_SENDING_TELEMETRY);
cModule.addModuleFeatures(MODULE_FEATURE_RECEIVING_TELEMETRY);

// 4. Set hardware info (optional)
cModule.setHardware("123456", ENUM_HARDWARE_TYPE::HARDWARE_TYPE_CPU);

// 5. Set receive callback (if receiving messages)
cModule.setMessageOnReceive(&onReceive);

// 6. Initialize UDP connection
cModule.init(
    "0.0.0.0",                          // Server IP (0.0.0.0 = localhost)
    60000,                              // Broker port
    "0.0.0.0",                          // Listen IP
    listen_port,                        // Listen port (unique per module)
    DEFAULT_UDP_DATABUS_PACKET_SIZE     // Max packet size
);
```

### Sending Messages

**JSON Messages:**
```cpp
Json_de message = {
    {"field1", "value1"},
    {"field2", 123}
};
cModule.sendJMSG("", message, TYPE_AndruavMessage_DUMMY, true);
```

**Binary Messages:**
```cpp
cModule.sendBMSG("", binary_data, data_length, TYPE_AndruavMessage_IMG, false, metadata_json);
```

### Receiving Messages

```cpp
void onReceive(const char* message, int len, Json_de jMsg) {
    // Extract message type
    const int msgid = jMsg[ANDRUAV_PROTOCOL_MESSAGE_TYPE].get<int>();
    
    // Handle specific message types
    if (msgid == TYPE_CUSTOM_MESSAGE) {
        // Process message
    }
}
```

## Message Types

Examples use various message types:

- **`TYPE_AndruavMessage_DUMMY`** - Test messages
- **`TYPE_AndruavMessage_IMG`** - Image data
- **`TYPE_AndruavMessage_MAVLINK`** - MAVLink protocol messages
- **`TYPE_AndruavMessage_USER_RANGE_START`** - Custom user-defined messages (start of range)
- **`TYPE_AndruavMessage_USER_RANGE_START+N`** - Custom message types (offset from start)

## Port Configuration

Each module must use a **unique listening port**:

- **Broker Port:** Typically `60000` (DroneEngage communicator)
- **Module Listen Ports:** Examples use:
  - `client.cpp`: User-defined (e.g., 61111)
  - `image_sender.cpp`: 50000
  - `mavlink_listener.cpp`: 70014
  - `sender_adapter.cpp`: 70034
  - `receiver_adapter.cpp`: 70024

## Testing Scenarios

### Scenario 1: Basic Communication Test
```bash
# Terminal 1: Start DroneEngage communicator (port 60000)
# Terminal 2: Run client
./client test_module 60000 61111
```

### Scenario 2: Image Streaming
```bash
# Terminal 1: Start DroneEngage communicator
# Terminal 2: Send images
./image_sender ./img.jpeg
```

### Scenario 3: Adaptive Rate Control
```bash
# Terminal 1: Start DroneEngage communicator
# Terminal 2: Start receiver
./receiver_adapter receiver_mod 60000 1000
# Terminal 3: Start sender
./sender_adapter sender_mod 60000 500
```

The sender and receiver will automatically adjust transmission rates based on queue depth.

## Architecture Overview

```
┌─────────────────┐
│  Application    │
│  (Examples)     │
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│   CModule       │  ← Module registration & routing
│   CFacade_Base  │  ← High-level API
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  CUDPClient     │  ← UDP transport with chunking
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  de_comm        │  ← DroneEngage Communicator
│  (Port 60000)   │
└─────────────────┘
```

## Debugging

Enable debug output by defining `DEBUG` or `DDEBUG`:

```bash
g++ -DDEBUG client.cpp -o client
```

Debug output includes:
- Message reception logs
- Message content dumps
- Queue status
- Rate adjustments

## Thread Safety

The examples demonstrate thread-safe patterns:

- **Mutex protection** for shared resources (receiver_adapter.cpp)
- **Condition variables** for thread synchronization
- **Lock guards** for RAII-style locking
- **Try-lock patterns** for non-blocking access

## Best Practices

1. **Unique Module IDs:** Use `generateRandomModuleID()` or hardcoded unique IDs
2. **Unique Listen Ports:** Each module needs its own port
3. **Message Filters:** Subscribe only to needed message types for efficiency
4. **Error Handling:** Check return values and handle connection failures
5. **Resource Cleanup:** Properly delete allocated memory (see image_sender.cpp)
6. **Rate Limiting:** Implement backpressure mechanisms for high-frequency data
7. **Help System:** Always include comprehensive help with `-h/--help` flags
8. **Argument Validation:** Validate user input with clear error messages
9. **Default Values:** Provide sensible defaults for optional arguments
10. **Colored Output:** Use console colors for better user experience
11. **Input Handling:** Use robust input handling for user prompts:
    ```cpp
    #include <limits>
    std::cout << "Press ENTER to continue ..." << std::endl;
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cin.get();
    ```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Module not appearing in WebClient | Check broker port (60000), ensure communicator is running |
| Port already in use | Change listen port to unused value |
| Messages not received | Verify message type is in MESSAGE_FILTER array |
| Segmentation fault | Check buffer sizes, ensure proper initialization |
| High CPU usage | Add sleep delays in main loops |

## Build System

### CMake Configuration

The project uses CMake for cross-platform building:

```bash
cd client
mkdir build && cd build
cmake ..
make
```

### Dependencies

- **CMake 3.10+** - Build system
- **C++17 Compiler** - GCC 7+, Clang 5+, or MSVC 2017+
- **pthread** - Threading support (Linux/macOS)
- **Winsock2** - Network sockets (Windows)
- **nlohmann/json** - JSON library (included in de_common)
- **DroneEngage communicator** - Running on port 60000

## API Reference

### CModule Class

```cpp
class CModule {
public:
    static CModule& getInstance();
    void defineModule(int moduleClass, const std::string& name, 
                     const std::string& id, const std::string& version, 
                     const Json_de& messageFilter);
    void addModuleFeatures(int feature);
    void setHardware(const std::string& hardwareId, int hardwareType);
    void setMessageOnReceive(void (*callback)(const char*, int, Json_de));
    void init(const std::string& serverIP, int serverPort, 
             const std::string& listenIP, int listenPort, int packetSize);
    void sendJMSG(const std::string& target, const Json_de& message, 
                  int messageType, bool requireAck);
    void sendBMSG(const std::string& target, const char* data, int length, 
                  int messageType, bool requireAck, const Json_de& metadata);
};
```

### CUDPClient Class

```cpp
class CUDPClient {
public:
    CUDPClient(CCallBack_UDPClient* callback);
    bool initialize(int port);
    void sendMessage(const std::vector<uint8_t>& data);
    void setJsonId(const std::string& jsonId);
};
```

### CFacade_Base Class

```cpp
class CFacade_Base {
public:
    virtual Json_de handleCommand(const Json_de& request) = 0;
    Json_de generateResponse(const std::string& status, const Json_de& data);
    void sendErrorMessage(const std::string& target, int partyId, 
                         int errorCode, int notificationType, 
                         const std::string& message);
};
```

## Code Style

- **Variables**: camelCase (e.g., `moduleName`, `messageData`)
- **Classes**: PascalCase (e.g., `CModule`, `CUDPClient`) 
- **Constants**: UPPER_SNAKE_CASE (e.g., `DEFAULT_PORT`, `MAX_PACKET_SIZE`)
- **Files**: snake_case (e.g., `de_module.cpp`, `udp_client.h`)

## Performance Considerations

### Memory Management

- RAII principles for resource management
- Smart pointers for automatic memory cleanup
- Memory pools for frequent allocations

### Thread Safety

- Mutex protection for shared data
- Lock-free queues for high-frequency operations
- Atomic operations for simple state changes

### Network Optimization

- UDP buffer tuning for high throughput
- Chunk size optimization for network conditions
- Adaptive retransmission strategies

## Debugging and Testing

### Logging

Comprehensive logging system with multiple levels:

```cpp
LOG_INFO("Module registered: %s", moduleName.c_str());
LOG_ERROR("Failed to send message: %s", errorMessage.c_str());
LOG_DEBUG("Received chunk %d/%d", chunkNum, totalChunks);
```

### Unit Tests

Test coverage for:

- Module registration and communication
- Message chunking and reassembly
- Binary data transmission
- Error handling and edge cases

## Additional Resources

- **Main custom plugins page** - [./de-custom-plugins.md](./de-custom-plugins.md)
- **Python implementation** - [./de-custom-plugins-python.md](./de-custom-plugins-python.md)
- **Node.js implementation** - [./de-custom-plugins-nodejs.md](./de-custom-plugins-nodejs.md)
- **C++ core library** - https://github.com/DroneEngage/droneengage_common
- **Test examples** - [../../droneengage_databus/client/test/README.md](../../droneengage_databus/client/test/README.md)
- **Core Library Documentation** - [../../droneengage_databus/client/src/de_common/README.md](../../droneengage_databus/client/src/de_common/README.md)
- **DroneEngage WebClient** - Access at `http://localhost:8080` (when communicator is running)
- **Message Protocol** - See `de_common/de_databus/andruav_message_id.hpp` for message type definitions
