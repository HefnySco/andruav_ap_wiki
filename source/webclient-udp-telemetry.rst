.. _webclient-udp-telemetry:

==================
Web UDP Telemetry
==================


|pic1|

|

This is not a module that you need to install like :ref:`webclient-web-plugin`. This is a built-in feature in Andruav_AP & DroneEngage as well. 
There are two sockets created at the :ref:`srv-communication`. A drone is streaming telemetry data to this UDP socket and then the user can connect to that socket using UDPCI in Mission Planner or any other GCS software.
This is much faster than the older :ref:`webclient-web-plugin` appraoch as the old module uses shared channel, tcp sockets, and multiple intermediate re-transmission which delays the mavlink messages compared to the new solution.






.. |pic1| image:: ./images/webclient_udp_proxy_diagram.png
   :width: 100 %
   :alt: UDP-Proxy
   :class: with-border

|

.. youtube:: C_AcmUGXFVQ

|

As you can see in the video, it is straight forward to use it. Just open WebClient to get the udp configuration settings, and connect via Mission Planner using UDPCI


|pic3|  and   |pic4|

.. |pic3| image:: ./images/webclient_udp_proxy.png
   :width: 35 %
   :alt: udp IP & Port

.. |pic4| image:: ./images/webclient_udp_proxy_mp.png
   :width: 35 %
   :alt: How to connect from Mission Planner

|

    The **LVL** section in WebClient is used to control rate of messages of the telemetry. Level 0 means full rate, and level 3 is the lowest rate.
    For DroneEngage you can control the details of this rates in :ref:`de-config-mavlink`


.. code-block:: json

   {
    "message_timeouts":
    { 
            "1": [0,250,500,1000],
            "2": [0,250,500,1000],     // SYSTEM_TIME
        "24": [0,800,1000,2000],    // GPS_RAW_INT
        "27": [0,500,1000,2000],    // RAW_IMU
        "28": [0,500,1000,2000],    // RAW_PRESSURE
        "29": [0,250,1000,2000],    // SCALED_PRESSURE
        "30": [0,250,1000,2000],    // ATTITUDE
        "32": [0,250,1000,2000],    // LOCAL_POSITION_NED
        "33": [0,250,1000,2000],    // GLOBAL_POSITION_INT
        "34": [0,500,1000,2000],    // RC_CHANNELS_SCALED
        "35": [0,500,1000,2000],    // RC_CHANNELS_RAW
        "36": [0,1000,2000,2000],   // SERVO_OUTPUT_RAW
        "42": [0,1000,2000,4000],    // MISSION_CURRENT
        "62": [0,250,500,1000],     // NAV_CONTROLLER_OUTPUT
        "65": [0,500,1000,2000],    // RC_CHANNELS
        "74": [0,500,1000,2000],    // VFR_HUD 
        "87": [0,500,1000,1000],     // POSITION_TARGET_GLOBAL_INT
        "116": [0,1000,2000,4000],  // SCALED_IMU2
        "124": [0,800,1000,2000],   // GPS2_RAW
        "125": [0,1000,2000,4000],  // POWER STATUS
        "129": [0,1000,2000,4000],  // SCALED_IMU3
        "136": [0,250,500,1000],    // TERRAIN_REPORT
        "137": [0,250,1000,2000],   // SCALED_PRESSURE2
        "143": [0,250,1000,2000],   // SCALED_PRESSURE3
        "147": [0,250,2000,4000],   // BATTERY_STATUS
        "152": [0,4000,8000,12000],  // MEMINO
        "163": [0,250,500,1000],     // AHRS
        "165": [0,250,1000,2000],    // HWSTATUS
        "178": [0,250,500,1000],     // AHRS2
        "182": [0,250,500,1000],     // AHRS3
        "193": [0,250,500,1000],     // EKF_STATUS_REPORT
        "241": [0,250,1000,2000],    // VIBRATION 
        "234": [0,250,1000,2000],    // HIGH_LATENCY 
        "235": [0,250,1000,2000],    // HIGH_LATENCY2 
        "11030": [0,1000,2000,5000],   // ESC_TELEMETRY_1_TO_4
        "11031": [0,1000,2000,5000],   // ESC_TELEMETRY_5_TO_8
        "11032": [0,1000,2000,5000]    // ESC_TELEMETRY_9_TO_12
        
    },
  }

For example message id 24 which is GPS_RAW_INT will have zero delay in level zero, but a minimum delay of 800ms in level 1, and a minimum 1 sec in level 2 and a minimum 2 seconds on level 3. This is how you can customize the optimization based on your needs. Other messages that are not mentioned will have zero delay for all levels.




    


|
This feature can be enabled in Andruav using the settings.

|pic5|

.. |pic5| image:: ./images/webclient_udp_proxy_andruav.jpg
   :width: 50 %
   :alt: Adnruav Settings
   :class: with-border


It also can be enabled in DroneEngage by changing **udp_proxy_enabled** in **config.module.json** of :ref:`de-config-mavlink`

.. code-block:: json

   {
   "udp_proxy_enabled": true,
   }

