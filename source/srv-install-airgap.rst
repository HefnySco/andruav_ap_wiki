.. _srv-install-airgap:

=======================================
Air-Gap RPI-4 Backend-Server Deployment
=======================================

The DroneEngage Air-Gap Server is designed to provide a robust and secure, self-contained server solution, particularly valuable in situations where internet connectivity is unreliable, restricted, or entirely prohibited.


For a **ready image** please check, please check the following options:

:ref:`srv-install-airgap-ready-image-wo-ap`

:ref:`srv-install-airgap-ready-image-w-ap`


Standalone Functionality:
-------------------------

 * This server is engineered to operate independently. This means it doesn't rely on constant communication with external cloud services or internet-based infrastructure.

 * It's a "lightweight" solution, implying it's optimized for efficiency and can run on very light hardware such as RPI-Zero 2W, which is crucial for deployment in remote or resource-constrained environments.


Complete Isolation (Air-Gap):
-----------------------------

 * The "air-gap" designation signifies the server's ability to function in a truly isolated network. This is vital for security-sensitive applications where data confidentiality is paramount.

 * In such a configuration, the server has no direct connection to the internet, eliminating the risk of external cyber-attacks.


Local Domain and Secure SSL:
----------------------------

 * Even in isolation, the server can establish its own local domain. This allows for organized network management and user access within the local environment.

 * The inclusion of secure SSL (Secure Sockets Layer) ensures that communication between devices within the local network is encrypted, protecting data from unauthorized interception.


Local Maps:
-----------

 * A key feature is the ability to host local maps. This is particularly important for drone operations, where real-time geospatial data is essential.

 * By storing map data locally, the server eliminates reliance on internet-based map services, ensuring uninterrupted operation even in areas with no connectivity.

 * This local map storage, allows for cached maps. Therefore, maps of needed areas can be downloaded when internet is available, and then used when internet is not available.
    
    






