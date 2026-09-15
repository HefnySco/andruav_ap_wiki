# Plugins

DroneEngage's modular architecture allows extending functionality through plugins. Plugins can interface with custom hardware, sensors, and external systems.

## Available Plugins

- [SDR Plugin](de-plugin-sdr)
- [Sound Plugin](de-plugin-sound)
- [GPIO Plugin](de-plugin-gpio)

## Plugin Development

Plugins can be written in:

- **C++** - For performance-critical applications
- **Python** - For rapid prototyping and scripting
- **Node.js** - For web-integrated solutions

All plugins communicate with the main DroneEngage system via the DataBus protocol.

See [Custom Plugin Development](technicals/de_common/de-custom-plugins) for comprehensive custom plugin development guides and [General plugin development guide](technicals/de_common/de-dev-plugins) for detailed development instructions.
