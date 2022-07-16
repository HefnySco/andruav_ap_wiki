.. _andruav-gcs-telemetry:



=====================
Andruav GCS Telemetry
=====================

Andruav Mobile App in GCS mode can stream telemetry data. The following video shows how easy it can be done.

.. youtube:: XHCfO6Zq4ek

|

Open Andruav GCS Mobile and connect online. Goto FCB screen. Once your GCS detects an active drone it will be listed is in image below

|

.. image:: ./images/gcs2.jpg
   :height: 400px
   :align: center
   :alt: FCB Screen for GCS Mobile

Multiple drones can be found in this list if there are multiple active drones online.
Select only one at a time to stream telemetry data to GCS applications such as Mission Planner.

.. image:: ./images/gcs1.jpg
   :height: 400px
   :align: center
   :alt: FCB Screen for GCS Mobile


.. important::

    Andruav GCS telemetry uses TCP connection, while :ref:`webclient-webplugin` uses UDP connection. You need to be careful when you select the connection in your GCS App such as `Mission Planner <https://ardupilot.org/planner/>`_ and `QGroundControl <http://qgroundcontrol.com/>`_.


|


The next video shows two mobiles the first is Andruav Drone mobile that is connected to a Rover using Bluetooth-to-USB,
and the second is Andruav Mobilein GCS mode. The latter acts as a telemetry for `Tower App <https://discuss.ardupilot.org/t/why-tower-and-droidplanner-app-disappear-from-goole-play-store/36977>`_ .

.. youtube:: Hv4Fp-b0wLM&t=150

|

.. warning::

    `Tower App <https://discuss.ardupilot.org/t/why-tower-and-droidplanner-app-disappear-from-goole-play-store/36977>`_ is not active, others GCS apps are available on mobile such as `Android QGrounControl <https://play.google.com/store/apps/details?id=org.mavlink.qgroundcontrol&hl=en>`_.




