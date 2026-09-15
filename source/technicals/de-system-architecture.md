# DroneEngage System Architecture

## Overview

DroneEngage is a distributed drone management ecosystem that enables remote monitoring and control of autonomous vehicles via the Internet. The system consists of four main components that work together to provide secure, scalable communication between drone units, ground control stations, and cloud infrastructure.

## System Components

### 1. Authentication Server (`droneegnage_authenticator`)

**Purpose**: Central authentication and authorization server for the DroneEngage ecosystem.

**Tech Stack**:
- Runtime: Node.js >= 18
- Web Framework: Express.js
- Database: SQLite3 with migration support
- Authentication: Custom token-based + Ed25519 S2S authentication
- Real-time: WebSocket (ws library)
- Templates: EJS with express-ejs-layouts
- Security: Helmet, CORS, CSRF protection, express-rate-limit

**Architecture**: Three independent servers running simultaneously:
- **API Server** (port 19408): REST API for authentication
- **Views Server** (port 8089): Admin web interface with EJS templating
- **S2S WebSocket Server** (port 19001): Server-to-Server communication with Ed25519 auth

**Key Responsibilities**:
- User and vehicle registration
- Authentication token generation
- Assignment of users/vehicles to communication servers
- Ed25519 cryptographic authentication for server-to-server communication
- Account management (single/file/db storage modes)

**Version**: 5.0.0

---

### 2. Communication Server (`droneengage_server`)

**Purpose**: Real-time messaging backbone for WebSocket-based communication between drone units and Ground Control Stations (GCS).

**Tech Stack**:
- Runtime: Node.js >= 18
- Web Framework: Express.js
- Database: MySQL2
- Real-time: WebSocket (ws library)
- Authentication: Ed25519 S2S authentication
- UDP: udp-packet for UDP proxy functionality
- Utilities: lodash, moment, uuid, randomstring, jspack

**Architecture**: Three operational modes:
- **Standalone**: Independent server for local communication
- **Child Server**: Connects to parent server for message relay
- **Parent (Super) Server**: Accepts child connections and forwards messages

**Core Components**:
- **WebSocket Server**: Main communication channel for units and GCS
- **S2S Relay**: Server-to-server mesh network for message propagation
- **UDP Proxy**: Handles UDP packet forwarding
- **Chat System**: Message routing and room management

**Key Features**:
- Message routing based on type (group/individual/system) and target
- Loop prevention using path tracking
- Memory monitoring with auto-restart
- Ed25519 cryptographic S2S authentication

**Version**: 3.9.11

---

### 3. Communication Module (`droneengage_communication`)

**Purpose**: Linux-based distributed communication broker that runs on vehicles, coordinating between various modules (Mavlink, Video, etc.) and the Andruav Server/WebClients.

**Tech Stack**:
- Language: C++17
- Build System: CMake 3.10+
- Core Libraries: Boost 1.74.0+ (coroutine, context, thread, system, chrono), libcurl4-openssl-dev, OpenSSL
- Architecture: Plugin-Broker pattern with UDP communication
- Package Management: Debian (.deb) packages via CPack
- Logging: plog (3rdparty library)

**Architecture**: Plugin-Broker Pattern

**Plugin Side** (de_comm library):
- `CModule` - Main interface for plugins (singleton pattern)
- `CUDPClient` - UDP communication with chunking support
- `CFacade_Base` - High-level API wrapper
- `CAndruavMessageParserBase` - Message parsing

**Broker Side** (de_comm broker module):
- `CUavosModulesManager` - Central module manager
- `CUDPCommunicator` - UDP server for modules
- `CMessageBuffer` - Thread-safe message queue

**Message Routing Types**:
- `CMD_TYPE_INTERMODULE` - Plugin-to-plugin communication only
- `CMD_COMM_SYSTEM` - Plugin-to-broker system commands
- `CMD_COMM_GROUP` / `CMD_COMM_INDIVIDUAL` - Messages forwarded to external DroneEngage server

**Module Classes**: FCB, Video, P2P, GPIO, Tracking, AI Recognition, SDR, Sound

**Version Format**: MAJOR.MINOR.BUGFIX.BUILD (auto-incremented on RELEASE builds)

---

### 4. MAVLink Module (`droneengage_mavlink`)

**Purpose**: Bridge between Ardupilot/PX4 flight controllers and the DroneEngage ecosystem. Runs on companion computers (e.g., Raspberry Pi) and communicates with flight controllers via MAVLink protocol.

**Tech Stack**:
- Language: C++17
- Build System: CMake 3.1+
- Core Libraries: pthreads, libstdc++6
- MAVLink: Custom MAVLink v2 library (c_library_v2)
- Architecture: Plugin pattern with UDP communication to DE Comm broker
- Package Management: Debian (.deb), TGZ, STGZ packages via CPack
- Logging: plog (3rdparty library)

**Architecture**: Plugin to DroneEngage Communication broker

**Key Components**:
- **MAVLink SDK**: Vehicle communication class (singleton), MAVLink message parsing/generation, connection management (Serial, UDP, TCP)
- **FCB Facade**: High-level API for flight control board communication, telemetry forwarding
- **FCB Main**: Main application logic, RC channel handling, mode management
- **Message Parser**: Parses messages from DE Comm broker, executes commands

**Key Features**:
- **Vehicle Types**: Quad, Plane, Rover, Heli, Boat, Submarine, VTOL, etc.
- **Flight Modes**: RTL, GUIDED, AUTO, LOITER, LAND, TAKEOFF, and PX4-specific modes
- **RC Override**: Joystick control, channel freezing, smart RC mapping
- **Follow-Me**: PID-based tracking with Kalman filtering
- **Swarm**: Leader-follower formation flying
- **Geofence**: Polygon and circular geofence with breach detection
- **UDP Proxy**: Telemetry forwarding to external UDP endpoints
- **Mission Planning**: Waypoint management and mission execution

**Version Format**: MAJOR.MINOR.BUGFIX.BUILD (auto-incremented on RELEASE builds)

---

## System Communication Flow

### Authentication Flow

1. **User Registration**: User registers → access code generation → email (unless ignoreEmail)
2. **User Login**: User login → session token generation → client uses token
3. **S2S Authentication**: WebSocket connection → Ed25519 challenge → signature verification → connection established

### Server-to-Server Communication

1. **Server Startup**: Communication server connects to authentication server via WebSocket
2. **Client Authentication**: Client sends HTTP POST to authentication server with credentials
3. **Server Selection**: Authentication server validates credentials and selects a communication server
4. **Login Reservation**: Authentication server requests communication server to generate temporary login key
5. **Key Generation**: Communication server generates temporary login key and stores it
6. **Key Delivery**: Communication server returns key and connection details to authentication server
7. **Client Connection**: Client receives connection details and establishes WebSocket to communication server
8. **Connection Acceptance**: Communication server validates temporary key and accepts WebSocket connection

### Vehicle Communication Flow

1. **MAVLink Module** connects to flight controller via Serial/UDP/TCP
2. **MAVLink Module** registers with **Communication Module** (broker) via UDP
3. **Communication Module** authenticates with **Authentication Server**
4. **Communication Module** establishes WebSocket connection to **Communication Server**
5. **Communication Server** routes messages between vehicles and GCS based on account/group membership
6. **S2S Relay** enables mesh network for scalable message propagation across multiple communication servers

### Message Routing

Messages are routed based on `ty` (type) and `tg` (target) fields:
- **Types**: `'g'` (group broadcast), `'i'` (individual), `'s'` (system/local)
- **Targets**: `'_GCS_'` (all GCS), `'_GD_'` (all units), `'_AGN_'` (all agents), or specific unit ID
- **Loop Prevention**: Uses `_path` array to track message traversal
- **Local Messages**: Forwarded to relay servers
- **External Messages**: Delivered locally only (no re-forwarding)

---

## Security Architecture

### Authentication Security
- HTTPS-based authentication
- Hardware ID validation
- Ed25519 cryptographic signatures for S2S communication
- Secure password hashing
- Configurable session secrets
- SSL/TLS for all connections

### Communication Security
- SSL/TLS for WebSocket connections
- Ed25519 cryptographic S2S authentication
- Configurable trusted server keys
- Helmet.js for HTTP security headers
- CORS configuration
- CSRF protection
- Rate limiting on API endpoints

### Module Security
- License validation via hardware serial and type
- Module key uniqueness enforcement
- SSL/TLS support for server communication

---

## Deployment Architecture

### Standalone Deployment
- Single communication server handling all clients
- Suitable for small-scale operations
- No S2S relay required

### Distributed Deployment
- Multiple communication servers in parent-child hierarchy
- Parent (super) server accepts child connections
- Child servers connect to parent for message relay
- S2S mesh network for scalable message propagation
- Automatic load balancing via server selection

### Vehicle Deployment
- Companion computer (e.g., Raspberry Pi) runs Communication Module (broker)
- MAVLink Module runs as plugin to Communication Module
- Additional modules (Video, GPIO, etc.) can be added as plugins
- All modules communicate via UDP with the broker
- Broker handles external communication with cloud servers

---

## Integration Points

### Web Client Integration
- React-based web client for GCS interface
- WebSocket connection to communication server
- Real-time telemetry display
- Remote control capabilities
- Mission planning and execution

### External System Integration
- UDP proxy for external telemetry forwarding
- REST API for third-party integration
- WebSocket API for real-time data
- Plugin system for custom extensions

---

## Development Workflow

### Building C++ Components (Communication Module, MAVLink Module)
```bash
# Prerequisites
sudo apt install git cmake build-essential
sudo apt install libcurl4-openssl-dev libssl-dev
sudo apt install libboost-all-dev

# Build
rm -rf ./build
mkdir build && cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON ../
make -j$(nproc)
cpack -G DEB  # Generate Debian package

# Install
sudo dpkg -i package-name.deb
```

### Building Node.js Components (Authentication Server, Communication Server)
```bash
# Prerequisites
npm install

# Configuration
cp server.config server.config.local
# Edit server.config.local

# SSL Certificates
mkdir -p ssl
openssl req -x509 -newkey rsa:4096 -keyout ssl/domain.key -out ssl/domain.crt -days 365 -nodes

# Run
npm start
```

---

## Related Documentation

- [Authentication Server Technicals](server/de-server-technicals-authentication)
- [Communication Server Technicals](server/de-server-technicals-communication)
- [Communication Module Technicals](communication/de-comm-technicals)
- [MAVLink Module Technicals](mavlink/de-mavlink-technicals)
- [Authentication ↔ Communication Flow](server/de-server-technicals-auth-comm-flow)
- [Message Propagation](server/de-server-technicals-mesh-relay)
