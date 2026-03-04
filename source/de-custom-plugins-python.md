# Python Plugin Development

The Python implementation provides a clean, Pythonic interface to the DroneEngage DataBus. It's ideal for rapid prototyping, scripting, and integration with Python's extensive ecosystem of libraries.

## Features

- **Python 3.6+ Compatible** - Modern Python features and type hints
- **Singleton Pattern** - Thread-safe module and configuration management
- **JSON Configuration** - Full JSON parsing with C-style comment support
- **UDP Communication** - Compatible with C++ and Node.js implementations
- **Message Reassembly** - Automatic chunking for large messages (>8KB)
- **Binary Message Support** - Handle images, files, and binary data
- **Thread Safety** - Mutex-protected operations for concurrent access
- **Colored Console Output** - Comprehensive error handling and logging
- **Configuration Management** - File monitoring and hot-reloading

## Quick Start

### Installation

```bash
cd python
pip install colorama
```

### As a Python Package

```bash
cd /home/mhefny/TDisk/public_versions/drone_engage/de_databus/python
pip install -e .
```

### Basic Usage

```bash
python python_client.py --help              # Show comprehensive help
python python_client.py MyModule 60000 61233  # Run with all arguments
python python_client.py MyModule             # Uses default ports
```

## Architecture

The Python implementation mirrors the C++ architecture with Pythonic design patterns:

### Core Classes

**CModule (Singleton)**
- Main module interface and management
- Thread-safe singleton pattern implementation
- Message routing and filtering

**CUDPClient**
- UDP communication with chunking protocol
- Automatic message reassembly
- Periodic module identification broadcasting

**CFacade_Base**
- Simplified API for response generation
- Template method pattern implementation
- Command handling and validation

**AndruavMessageParserBase**
- JSON and binary message parsing
- Command dispatch and routing
- Message validation and filtering

**ConfigFile / LocalConfigFile**
- JSON configuration management
- File monitoring and hot-reloading
- C-style comment support

## Usage Examples

### Basic Module Setup

```python
from de_module import CModule
from de_facade_base import CFacade_Base
from messages import *

class MyFacade(CFacade_Base):
    def handleCommand(self, request):
        return {
            'status': 'success',
            'data': {'message': 'Command processed'}
        }

# Create module instance (singleton)
module = CModule()

# Define module properties
module.defineModule(
    name='MyModule',
    version='1.0.0',
    facade=MyFacade()
)

# Start communication
module.start()
```

### Message Handling

```python
from de_module import CModule
import json

module = CModule.getInstance()

# Send JSON message
message = {
    'command': 'get_status',
    'parameters': {'detail': 'full'}
}
module.sendMessage('target_module', message)

# Send binary data
with open('image.jpg', 'rb') as f:
    image_data = f.read()
    module.sendBinaryData('target_module', image_data, 
                         metadata={'type': 'image', 'format': 'jpeg'})
```

### Configuration Management

```python
from configFile import ConfigFile

# Load configuration
config = ConfigFile('config.json')
config.load()

# Access configuration values
port = config.get('network.port', 60000)
timeout = config.get('network.timeout', 5.0)

# Monitor configuration changes
config.startMonitoring()
config.onChanged(lambda: print('Configuration updated'))
```

### Message Filtering

```python
# Set message filter
module.setMessageFilter(['telemetry', 'command'])

# Custom message handler
def handleTelemetry(data):
    processTelemetryData(data)

module.registerMessageHandler('telemetry', handleTelemetry)
```

## API Reference

### CModule Class

```python
class CModule:
    """Singleton module manager for DroneEngage communication"""
    
    @staticmethod
    def getInstance():
        """Get singleton instance"""
        
    def defineModule(self, name, version, facade):
        """Define module properties"""
        
    def start(self):
        """Start module communication"""
        
    def stop(self):
        """Stop module communication"""
        
    def sendMessage(self, target, message):
        """Send JSON message to target module"""
        
    def sendBinaryData(self, target, data, metadata=None):
        """Send binary data to target module"""
        
    def setMessageFilter(self, filters):
        """Set message type filter"""
        
    def registerMessageHandler(self, messageType, handler):
        """Register custom message handler"""
```

### CUDPClient Class

```python
class CUDPClient:
    """UDP client with chunking and reassembly"""
    
    def __init__(self, callback):
        """Initialize with receive callback"""
        
    def initialize(self, port):
        """Initialize UDP socket"""
        
    def sendMessage(self, data):
        """Send message data"""
        
    def setJsonId(self, jsonId):
        """Set module JSON identifier"""
        
    def close(self):
        """Close UDP connection"""
```

### CFacade_Base Class

```python
class CFacade_Base:
    """Base class for command handling facades"""
    
    def handleCommand(self, request):
        """Handle incoming command request"""
        raise NotImplementedError
        
    def generateResponse(self, status, data):
        """Generate standardized response"""
        
    def generateError(self, message, code=None):
        """Generate error response"""
        
    def validateRequest(self, request):
        """Validate request format"""
```

## Package Structure

### Directory Layout

```
python/
├── __init__.py              # Package initialization
├── de_module.py             # Main module interface
├── udpClient.py             # UDP communication
├── de_facade_base.py        # Base facade class
├── de_message_parser_base.py # Message parsing
├── configFile.py            # Configuration management
├── localConfigFile.py       # Local configuration
├── messages.py              # Message definitions
├── colors.py                # Console colors
├── console_colors.py        # Color utilities
└── python_client.py         # Example client
```

### Dependencies

```python
# requirements.txt
colorama>=0.4.0
```

## Code Style

- **Variables**: snake_case (e.g., `module_name`, `message_data`)
- **Classes**: PascalCase (e.g., `CModule`, `CUDPClient`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `DEFAULT_PORT`, `MAX_PACKET_SIZE`)
- **Functions**: snake_case (e.g., `send_message`, `handle_command`)
- **Type Hints**: Use in newer code for better documentation

```python
from typing import Dict, List, Optional, Callable, Any

def sendMessage(self, target: str, message: Dict[str, Any]) -> bool:
    """Send message to target module"""
    pass

def registerHandler(self, message_type: str, 
                   handler: Callable[[Dict[str, Any]], None]) -> None:
    """Register message handler"""
    pass
```

## Thread Safety

The Python implementation uses threading.Lock() for singleton safety:

```python
import threading

class CModule:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

Mutex protection for shared resources:

```python
class CUDPClient:
    def __init__(self):
        self._send_lock = threading.Lock()
        self._receive_lock = threading.Lock()
    
    def sendMessage(self, data):
        with self._send_lock:
            # Thread-safe sending
            pass
```

## Error Handling

Comprehensive error handling with colored output:

```python
from colors import Colors

try:
    result = module.sendMessage(target, message)
except ConnectionError as e:
    print(Colors.red(f"Connection error: {e}"))
except ValueError as e:
    print(Colors.yellow(f"Invalid data: {e}"))
except Exception as e:
    print(Colors.red(f"Unexpected error: {e}"))
    raise
```

Custom exception classes:

```python
class DroneEngageError(Exception):
    """Base exception for DroneEngage errors"""
    pass

class CommunicationError(DroneEngageError):
    """Communication-related errors"""
    pass

class ConfigurationError(DroneEngageError):
    """Configuration-related errors"""
    pass
```

## Performance Considerations

### Memory Management

- Efficient binary data handling with memoryviews
- Buffer pooling for frequent allocations
- Garbage collection optimization

### Network Optimization

- UDP buffer tuning for high throughput
- Chunk size optimization for network conditions
- Connection reuse and pooling

### Threading Optimization

- Minimal lock contention
- Thread-local storage where appropriate
- Async/await patterns for I/O operations

## Debugging and Logging

### Colored Console Output

```python
from colors import Colors

print(Colors.info("Information message"))
print(Colors.success("Success message"))
print(Colors.warning("Warning message"))
print(Colors.error("Error message"))
```

### Debug Mode

Enable debug output:

```bash
python python_client.py MyModule --debug
```

### Logging Configuration

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info("Module started")
```


## See Also

- [Main custom plugins page](./de-custom-plugins.md)
- [C++ implementation](./de-custom-plugins-cpp.md)
- [Node.js implementation](./de-custom-plugins-nodejs.md)
- https://docs.python.org/3/library/threading.html - Python threading documentation
