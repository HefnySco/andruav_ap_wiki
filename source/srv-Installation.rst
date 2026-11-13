.. _srv-Installation:



============================
Backend-Servers Installation
============================

The easiest backend is one Raspberry Pi: **airgap.local**. The Pi runs all
the servers, and it makes its own Wi-Fi network. Laptops, vehicles and
ground stations connect to this Wi-Fi. No internet is necessary.

.. image:: /images/diagrams_2026/airgap_local_network_2026.svg
   :align: center
   :alt: airgap.local - a Raspberry Pi with its own DE_SERVER Wi-Fi, its services and URLs, and the laptop, vehicle and GCS that connect to it

|

The backend can also run on many machines, with load balancing and
fail-over. See :ref:`srv-airgap-servers` for the four servers and their
config files.

|

Connect to airgap.local
=======================

#. Connect your laptop or tablet to the Wi-Fi **DE_SERVER**.
#. The Pi gives your device an IP address in ``192.169.9.0/24``. The Pi is
   ``192.169.9.1``.
#. Open a browser and use the addresses below.

.. list-table::
   :header-rows: 1
   :widths: 30 45 25

   * - Service
     - Address
     - Who uses it
   * - WebClient (GCS)
     - ``https://airgap.local:8001``
     - Operators
   * - Wiki and **GUIDME.md**
     - ``https://airgap.local:8080``
     - Everybody
   * - Authenticator admin
     - ``https://airgap.local:8089/admin/login``
     - Administrator
   * - Storage dashboard
     - ``https://airgap.local:9001/admin/login``
     - Administrator
   * - Offline maps
     - ``http://airgap.local:88``
     - The WebClient
   * - SSH
     - ``ssh pi@airgap.local``
     - Administrator

.. note::

   The certificates are self-signed, so the browser shows a warning. Install
   the root certificate on each device to stop the warning. See
   :ref:`srv-install-airgap-ready-image-w-ap`.

.. tip::

   Andruav on a phone may not know the name ``airgap.local``. Use the IP
   ``192.169.9.1`` on the phone.

|

Read GUIDME.md First
====================

Each air-gap card has a guide file: **GUIDME.md**. It describes this card
exactly: what is installed, what runs, the ports, the accounts and the rules.

* Open it in a browser: `https://airgap.local:8080/GUIDME.md <https://airgap.local:8080/GUIDME.md>`_
* Or read it on the Pi: ``/home/pi/GUIDME.md``

GUIDME.md contains:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Section
     - What it tells you
   * - Network
     - The host name, the Wi-Fi name, the IP addresses, DHCP, DNS and SSH.
   * - Services and ports
     - Each server, its port and how it runs (systemd or pm2).
   * - Admin URLs and logins
     - The admin pages, where each default login is defined, and that you
       must change them.
   * - Accounts
     - The logins of the card and the role of each login.
   * - Home folder layout
     - Where the WebClient, the wiki, the maps, the scripts and the
       certificates are.
   * - Offline maps
     - How to fill the map folder.
   * - Rules for the AI
     - What an AI assistant must not do on this card.

.. tip::

   **Use an AI assistant on the Pi.** Tell your assistant: *"Read
   https://airgap.local:8080/GUIDME.md first."* The file gives it the layout
   of the card and its safety rules. For example, it must never show
   passwords or keys, and it must not delete the Wi-Fi profile or the maps.

|

Accounts on the Card
====================

The card has five logins in one team. All of them see the same units.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Login
     - Role
   * - ``single@airgap.droneengage.com``
     - Administrator. All permissions.
   * - ``admin``
     - Administrator. All permissions.
   * - ``gcs``
     - Ground station. All actions. It cannot log in as a unit.
   * - ``unit``
     - Vehicle unit login.
   * - ``view``
     - Ground station, view only.

The passwords are not in this wiki. Ask the person who prepared the card.

.. warning::

   Change the default admin passwords of the Authenticator and the Storage
   dashboard before a real deployment. GUIDME.md tells where each one is
   defined. See :ref:`srv-airgap-servers`.

|

Check the Servers
=================

Connect with SSH. Then run:

.. code-block:: bash

    systemctl is-active de_auth de_comm de_storage de_udp_relay
    pm2 list
    ss -tln

Each server must show ``active``. ``pm2 list`` must show ``de_web_server``
and ``de_wiki``.

|

.. toctree::
   :caption: Contents:
   :titlesonly:
   :maxdepth: 2

   Air-Gap Tiny Server Installation </srv-install-airgap>
