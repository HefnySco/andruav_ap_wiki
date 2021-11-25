.. _andruav-tx-freeze:

=================
Andruav TX Freeze
=================


This command is called from :ref:`andruav-web-client` only. 
This function is used to simulate signals from TX. 
For example if you switch to loiter mode then you need to keep TX throttle at a level to keep your drone from falling. 
You can set your TX throttle then press TX-Freeze then Andruav will copy the last value from TX and keep using it while your drone is far out of your TX range.


.. image:: ./images/web_telemetry_on.png
    :align: center
    :alt: Web TX-Freeze


.. warning::

    This is a very critical feature to use. As it will make your TX unable to communicate with your drone. 
    However :ref:`andruav-tx-block` can override this button.


