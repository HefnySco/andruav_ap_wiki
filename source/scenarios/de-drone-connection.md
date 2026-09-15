# On-Board DroneEngage
This is the default DroneEngage installation, where DroneEngage is running RPI-Board or similar boards and installed on the drone itself.

<iframe width="560" height="315" src="https://www.youtube.com/embed/9FCykA5E8iw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

In this configuration, DroneEngage unit RPI board is connected to the flight controller via serial connection, UDP or TCP connection.

**de_comm** is the communication module that handles the connection between DroneEngage unit and DroneEngage server and it represents DroneEngage Unit. Other modules runs with **de_comm** only communicates with **de_comm**.





**de_mavlink** can be connected via 3 ways:
- Serial connection
- UDP connection
- TCP connection


The challenge is how to connect RPI-Board to DroneEngage server, which is on ground. Server could be accessible via Internet or a local isolated server, and this can be done using different connection methods:

## TCP/UDP Connection
this is a wireless/ethernet connection. ethernet is reliable and allow longer cables. wirelss connnections can be easily jammed and interrupted, and sniffing is possible.

## Optical Connection

<iframe width="560" height="315" src="https://www.youtube.com/embed/qjVyVDqJ6To" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This is the same form of TCP/UDP connection, but we use Optical cables in-between. This allows multiple kilometers very secured connection.

## 4/5G Connection
This is a wireless connection that uses 4G/5G networks to connect the drone to the ground. This is useful when the drone is far from the ground and there is no ethernet or optical connection available. [Andruav](https://github.com/mhefny/Andruav) app is originally designed based on this type of connections [Andruav SourceCode](https://github.com/HefnySco/andruav_android_app).

## Serial Connection
This is a very tricky connection method. DroneEngage cannot work using serial communication between DroneEngage unit and server. What you need is to run TCP/IP over serial port. so the serial port is seen as a network interface, and the same configuration is applied on a ground computer where is connects the whole system to Internet. This is done by running a TCP/IP over serial port bridge on the ground computer.

## VPN Connection
This connection allows your drone to connect to the server through a secure virtual private network. Although one of the advantage of DroneEngage is that its ability to stream video without the need to VPN as opposed to many similar systems, but VPN here is useful when you want to run your own Local [AirGap server](../srv-install-airgap)
