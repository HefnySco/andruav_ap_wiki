.. _andruav-gps-injection:


=====================
Andruav GPS-injection
=====================


Mobile GPS is a powerful GPS. Andruav version 4.0 uses GPS signal and inject it to FCB board. 
You can depend on mobile GPS by defining **GPS_TYPE** as MAV, or if you have a GPS you can define a secondary GPS as MAV.


.. image:: ./images/gps_injection.png
    :align: center
    :alt: GPS Injection


You also need to enable GPS injection in Andruav Drone Preference.

.. image:: ./images/gps_settings.png
    :align: center
    :height: 400px
    :alt: GPS Prefrerence

.. warning::
    
    This feature is available on mobiles running Android Orio or later.
