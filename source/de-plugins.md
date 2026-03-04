# Plugins

DroneEngage's modular architecture allows extending functionality through plugins. Plugins can interface with custom hardware, sensors, and external systems.

## Available Plugins

- [SDR Plugin](./de-plugin-sdr.md)
- [Sound Plugin](./de-plugin-sound.md)
- [GPIO Plugin](./de-plugin-gpio.md)

## Plugin Development

Plugins can be written in:

- **C++** - For performance-critical applications
- **Python** - For rapid prototyping and scripting
- **Node.js** - For web-integrated solutions

All plugins communicate with the main DroneEngage system via the DataBus protocol.

See [Custom Plugin Development](./de-custom-plugins.md) for comprehensive custom plugin development guides and [General plugin development guide](./de-dev-plugin.md) for detailed development instructions.
