.. _de-account-create:

====================================
Create your Drone-Engage Account Key
====================================

Access to Drone-Engage requires registration and the acquisition of an :term:`Access Code` from the `Account Manager <http://cloud.ardupilot.org:8001/accounts.html>`_.  The registration process is straightforward, and the :term:`Access Code` will be delivered to the provided email address. This code is essential and should be securely stored for use with all drones.

Account validation is completed by logging into the `Drone-Engage Web Client <https://cloud.ardupilot.org:8001/webclient.html>`_.

The same :term:`Access Code` is used to configure the Communication Client (`de_comm.so`) on the Raspberry Pi, establishing the connection between the vehicle, the Drone-Engage server, and the web client.

.. tip::
    A single account is sufficient for managing multiple drones.

.. youtube:: baHWBc6RvaE

.. warning::
    Sharing your :term:`Access Code` grants access to your Drone-Engage account to other individuals, potentially allowing them to connect their devices. This functionality can be utilized to enable shared access, such as when collaborating with a ground control station (GCS) operator during a flight.