.. _andruav-faq:

===========
Andruav FAQ
===========

.. image:: ./images/andruav.png
   :height: 160px
   :align: center
   :alt: Andruav app icon

|

For questions about accounts, access codes and servers, also read
:ref:`de-faq` and the :ref:`glossary`.

|

General
=======

**Is Andruav a ground station app?**
   No. Andruav runs only on the phone on the vehicle. You monitor and control
   the vehicle from the :ref:`webclient-whatis` in a browser. On a phone, use
   the :ref:`webclient-mobile`. You do not install an app on the ground.

**Which vehicles can I use?**
   ArduPilot drones, boats and rovers. Andruav connects to the ArduPilot
   flight controller of the vehicle.

**What is new in Andruav 15?**
   The phone now runs the real DroneEngage modules, the same modules that run
   on a Raspberry Pi. See :ref:`andruav-de-native`.

**Should I use a phone or a Raspberry Pi?**
   Use a phone to learn and to prove your idea. Use a DroneEngage Raspberry Pi
   when people depend on the vehicle. The WebClient and the account are the
   same, so you can move from the phone to the Pi easily.

**Is Andruav free?**
   Yes. Download it from `Google Play <https://play.google.com/store/apps/details?id=arudpilot.andruav>`_
   and make a free account. See :ref:`andruav-getting-started`.

|

Phone
=====

**Which phones can I use?**
   A phone with Android 7.0 or later and a 64-bit processor (``arm64``). The
   DroneEngage modules are built for 64-bit phones only.

**Must I give all the permissions?**
   No. Andruav starts without them, but a feature that needs a permission
   does not work without it. For example, FPV needs ``CAMERA`` and SMS
   commands need the SMS permissions. See :ref:`andruav-de-native`.

**How do I make the screen easy to read in the sun?**
   Open the menu (⋮), tap **Theme** and select **Sun**.

|

Connection
==========

**Do I need the internet?**
   The phone needs a link to a Mission Server. This can be the internet to
   ``cloud.ardupilot.org``, or a local Wi-Fi to your own
   :ref:`air-gap server <srv-airgap-servers>` with no internet.

**I tap CONNECT and the login screen opens. Why?**
   Andruav has no access code. Tap **SIGN-IN**, type your email and access
   code, and then tap **CONNECT** again.

**The card shows "Native Unit Online" but not "SECURED". Why?**
   **Settings > Require SSL verification** is off. The link works, but the
   phone does not check the certificate of the server. Turn it on, except for
   a private server whose certificate the phone cannot check.

**How do I connect the flight controller?**
   Tap the **FCB** tile and select Bluetooth, USB, Wi-Fi or UDP. See
   :ref:`andruav-serial`. To test with a simulator, see :ref:`andruav-simulators`.

**Can I use Mission Planner or QGroundControl?**
   Yes. Tap **ENABLE TELEMETRY** on the home screen. Then connect Mission
   Planner with UDPCI to the address that the Flight Telemetry card shows.
   See :ref:`andruav-telemetry`.

|

Safety
======

**What occurs if the phone loses the server link in flight?**
   If you turn on **Settings > DroneEngage native > Comm-loss flight
   failsafe**, the phone sets the flight controller to the mode that you
   select, for example RTL. It does this without the app screen and without
   a ground station. Test it in SITL first. See :ref:`andruav-simulators`.

**Can I control the vehicle when there is no internet?**
   You can send some commands by SMS, for example RTL and LAND. See
   :ref:`andruav-sms`. Do not use SMS as your only safety link.

**Can a pilot stop the commands from the WebClient?**
   Yes. Turn on **Settings > Enable RC Block**. Then an RC switch blocks the
   commands from all ground stations. See :ref:`de-tx-block`.

**How do I find a lost vehicle?**
   Use **Settings > Lost Siren** and **Flash Screen**. Also send
   ``ATT:LOC:<PIN>`` by SMS to get its location. See :ref:`andruav-sms`.

|

GPS and RTK
===========

**Can the phone GPS be the GPS of the flight controller?**
   Not yet. GPS Injection is *coming*. The setting is visible, but it is not
   active in this version. See :ref:`andruav-gps-injection`.

**Can Andruav send RTK corrections (NTRIP)?**
   Not yet. NTRIP RTK is *coming*. See :ref:`andruav-settings`.
