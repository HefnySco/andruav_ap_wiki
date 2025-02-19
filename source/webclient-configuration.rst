.. _webclient-configuration:


=============
Configuration
=============


The following is the `js_siteConfig.js <https://github.com/DroneEngage/droneengage_webclient_react/blob/master/src/js/js_siteConfig.js>`_ the configuration file for the WebClient. This file is used to configure the WebClient to connect to the correct server and to enable or disable features.

.. code-block:: JAVASCRIPT

    /**
    * 
    * SITE Configuration File
    * 
    * Auth: Mohammad Hefny
    * 
    */


    /**
    * Communication Server
    */

    export const CONST_TEST_MODE = false;
    export const CONST_PROD_MODE_IP = 'airgap.droneengage.com'; 
    export const CONST_PROD_MODE_PORT = '19408';
    
    export const CONST_TEST_MODE_IP = '127.0.0.1';
    export const CONST_TEST_MODE_PORT = '19408';
    
    export const CONST_TEST_MODE_ENABLE_LOG = false;  // should be used together with CONST_TEST_MODE
    export const CONST_TITLE = 'Drone Engage';

    /**
    * Links that are used in Header
    */
    export const CONST_HOME_URL = "https://cloud.ardupilot.org/";
    export const CONST_MANUAL_URL = "https://cloud.ardupilot.org/";
    export const CONST_FAQ_URL = "https://cloud.ardupilot.org/de-faq.html";
    export const CONST_CONTACT_URL = "https://droneengage.com/contact.html";

    /**
    * Location of GCS are not sent over network. Only The existence of connected GCS are shared.
    */
    export const CONST_DONT_BROADCAST_TO_GCSs = false;


    /**
    * This is for disable experimental features.
    * If a feature is not explicitly mentioned or has a value of true, it is considered to be enabled.
    */
    export const CONST_FEATURE = 
    {
        DISABLE_UNIT_NAMING: false,
        DISABLE_UDPPROXY_UPDATE: false,
        DISABLE_SWARM: false,
        DISABLE_SWARM_DESTINATION_PONTS: false,
        DISABLE_P2P: false,
        DISABLE_SDR: false,
        DISABLE_GPIO: false,
        DISABLE_VOICE: false,
    };

    export const CONST_ICE_SERVERS =  [
        {urls: 'turn:cloud.ardupilot.org', 'credential':'1234', 'username':'andruav_ap'},
        {urls: "stun:stun1.l.google.com:19302"},
        ];


|
|

Fields Meaning
==============

The following are the fields that are used in the configuration file.


Connection to the Server
------------------------

.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - Field Name
     - Description
     - Example
   * - CONST_TEST_MODE
     - if true then use - if true then use CONST_TEST_MODE_IP and CONST_TEST_MODE_PORT for connection.
     - default is false.
   * - CONST_PROD_MODE_IP
     - IP of the production server.
     - "airgap.droneengage.com"
   * - CONST_PROD_MODE_PORT
     - Port of the production server.
     - "19408"
   * - CONST_TEST_MODE_IP
     - IP of the test server.
     - "
   * - CONST_TEST_MODE_PORT
     - Port of the test server.
     - "19408"
   * - CONST_TEST_MODE_ENABLE_LOG
     - Enable log for the test server.
     - default is false.
   * - CONST_TITLE 
     - Title of the WebClient.
     - "My Own Drone Engage Site"




Header Links
------------

These are the links that are used in the header of the WebClient.

.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - Field Name
     - Description
     - Example
   * - CONST_HOME_URL
     - URL of the Home link. If you have your own server you need to change this link accordingly.
     - "https://cloud.ardupilot.org/"
   * - CONST_MANUAL_URL
     - URL of the Manual link. If you have your own server you need to change this link accordingly.
     - "https://cloud.ardupilot.org/"
   * - CONST_FAQ_URL
     - URL of the FAQ link. If you have your own server you need to change this link accordingly.
     - "https://cloud.ardupilot.org/de-faq.html"
   * - CONST_CONTACT_URL
     - URL of the Contact link. If you have your own server you need to change this link accordingly.
     - "https://droneengage.com/contact.html"
        

Features
--------

There are features that you can enable or disable in the WebClient. Some of these features are experimental and are disabled by default.

.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - Field Name
     - Description
     - Example
   * - DISABLE_UNIT_NAMING
     - This feature prevents the user from re-naming DroneUnit from WebClient.
     - false
   * - DISABLE_UDPPROXY_UPDATE
     - This feature enables and disables the ability to update the UDP proxy from the WebClient.
     - false
   * - DISABLE_SWARM
     - This feature enable and disable the ability to form swarms from webclient. It only hides the GUI interface from WebClient.
     - false
   * - DISABLE_SWARM_DESTINATION_PONTS
     - These are small drone icons that points to where follower drones should go. Related to DISABLE_SWARM feature.
     - false
   * - DISABLE_P2P
     - P2P module is an experimental module to for P2P drone communication.
     - false
   * - DISABLE_SDR
     - SDR module is an experimental module to run SDR on the drone.
     - false
   * - DISABLE_GPIO
     - GPIO module is a DroneEngage module that is used to control the GPIO pins on the drone unit.
     - false
   * - DISABLE_VOICE
     - Voice module is a DroneEngage module that is used to speak or play audi on the drone unit.
     - false

Some of the above features will not display any GUI unless the correspondent module is up and running on the unit.


Other Parameters
----------------


.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - CONST_DONT_BROADCAST_TO_GCSs
     - This is to disable the broadcasting of the location of the GCSs to the network.
     - false
    
    * - CONST_ICE_SERVERS
      - This is the ICE servers used for WebRTC. Donot change unless you know what you do or you might cannot establish video connection.
      - 
        