.. _glossary:

========================
DroneEngage & Andruav Glossary
========================

This glossary defines key terms used throughout the DroneEngage and Andruav documentation.

|

.. glossary::
    :sorted:

    4G/LTE
        Fourth Generation Long-Term Evolution cellular network technology. DroneEngage uses 4G/LTE modems to provide internet connectivity for unlimited range telemetry.

    Access Code
        A system-generated password used with your email to authenticate devices on the DroneEngage server. Obtain yours from `Accounts @ cloud.ardupilot.org <https://cloud.ardupilot.org:8001/accounts.html>`_. Sharing your Access Code allows others to join your account (useful for shared GCS operations).

    Andruav
        `Andruav <https://play.google.com/store/apps/details?id=arudpilot.andruav&hl=en&gl=US>`_ is the Android-based predecessor to DroneEngage. It runs on Android phones mounted on drones. DroneEngage is the Linux-based evolution designed for Raspberry Pi.

    Ardupilot
        Open-source autopilot software that runs on :term:`FCB` hardware. Supports Copter, Plane, Rover, and Sub vehicles. See `ardupilot.org <https://ardupilot.org/>`_.

    Camera Module
        The DroneEngage module (``de_camera``) responsible for video streaming and photo capture. Supports Raspberry Pi cameras and USB cameras.

    Comm Module
        The main DroneEngage module (``de_comm``) that connects to the cloud server over the internet and manages communication between all local modules via the :term:`DataBus`.

    Companion Computer
        A secondary computer (typically Raspberry Pi) connected to the :term:`FCB` that provides additional capabilities like video streaming, 4G telemetry, and advanced processing.

    DataBus
        The internal UDP-based communication protocol used for inter-module communication within DroneEngage. Allows modules to exchange data efficiently.

    de_camera
        See :term:`Camera Module`.

    de_comm
        See :term:`Comm Module`.

    de_mavlink
        See :term:`MAVLink Module`.

    Drone Mode
        The operational mode for Andruav when running on a mobile device mounted on a drone. Essential for communicating with flight control boards, capturing images, and accessing flight information.

    DroneKit
        A library developed by 3DR that provides reliable connection with PixHawk, APM, SOLO and virtually any board that supports MAVLINK.

    FCB
        Flight Control Board. Hardware that runs autopilot firmware (e.g., `OBAL <https://ardupilot.org/copter/docs/common-obal-overview.html>`_, `Pixhawk <https://pixhawk.org/>`_, Cube, Kakute). Connects to the companion computer via serial or UDP.

    GCS
        Ground Control Station. Software used to monitor and control drones. Examples include `Mission Planner <https://ardupilot.org/planner/>`_, `QGroundControl <http://qgroundcontrol.com/>`_, Andruav App in GCS mode, and the `DroneEngage web client <https://cloud.ardupilot.org:8001/>`_.

    Geo-Fence
        A virtual boundary that restricts drone flight to specific areas. DroneEngage provides independent geo-fencing that works alongside or instead of the FCB's built-in geo-fence.

    JSON
        JavaScript Object Notation. A lightweight data format used for DroneEngage configuration files and communication protocols.

    Binary Payload
        Binary data that can be attached to DroneEngage messages after the JSON header. Used for images, files, and other binary data transfers.

    MAVLink
        Micro Air Vehicle Link. A lightweight messaging protocol for communicating with drones. Used between the :term:`FCB` and :term:`MAVLink Module`.

    MAVLink Module
        The DroneEngage module (``de_mavlink``) that communicates directly with the :term:`FCB` via serial port or UDP. Translates between MAVLink and DroneEngage protocols.

    Pin Code
        An alphanumeric text that uniquely identifies your Andruav app on a particular mobile device. This number never changes unless you remove and reinstall Andruav on the device. This number is not editable.

    RPI
        Raspberry Pi. A single-board computer commonly used as a :term:`Companion Computer` for DroneEngage.

    RPI Image
        A pre-configured Raspberry Pi OS image with DroneEngage modules pre-installed. Available for RPI-Zero 2 W and RPI-4.

    RC Blocking
        A safety feature allowing a field pilot with a physical transmitter to override all remote commands, providing emergency local control.

    SITL
        Software-In-The-Loop. A simulation mode that runs Ardupilot on a PC without physical hardware, useful for testing DroneEngage before flying.

    Smart Telemetry
        DroneEngage's bandwidth optimization feature that reduces data transmission on slower networks by filtering less critical MAVLink messages.

    Swarm
        A group of drones operating together under coordinated control. DroneEngage supports hierarchical swarm formations with leader and follower roles.

    Telemetry Manager
        The component within the Communicator Module responsible for communicating with other modules and the web client via the server communication protocol.

    TX Freeze
        A DroneEngage feature that locks the current throttle/control positions, useful for maintaining stable flight when the drone is beyond TX range.

    Unit
        A DroneEngage-equipped drone or vehicle. Each unit connects to the cloud server and appears in the web client.

    Message Type
        An identifier that categorizes messages in the DroneEngage communication protocol. Modules subscribe to specific message types to receive relevant data.

    Module Manager
        The component within the Communicator Module responsible for managing inter-module communication using a publisher/subscriber pattern.

    Plugin
        A custom module that extends DroneEngage functionality. Plugins can handle hardware (GPIO, sensors) or perform data processing. Written in C++, Python, or Node.js using the DataBus library.

    Port
        A network endpoint number used for UDP/TCP communication. DroneEngage modules use specific ports for inter-module communication.

    Publisher/Subscriber
        A messaging pattern where modules publish messages to topics and other modules subscribe to receive those messages. Used by the Module Manager for inter-module communication.

    Socket
        A network communication endpoint. DroneEngage uses UDP sockets for fast inter-module communication with automatic message chunking.

    UDP
        User Datagram Protocol. A fast, connectionless protocol used for inter-module communication within DroneEngage. Supports message chunking for large data transfers.

    Web Client
        The browser-based ground control station for DroneEngage. Access at `cloud.ardupilot.org:8001 <https://cloud.ardupilot.org:8001>`_.
