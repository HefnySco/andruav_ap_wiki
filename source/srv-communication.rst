.. _srv-communication:


====================
Communication Server
====================

The **Communication Server** is the real-time message center of
DroneEngage. It keeps a WebSocket open to each unit and each WebClient, and
it routes all messages between them.

.. image:: /images/diagrams_2026/airgap_servers_overview_2026.svg
   :align: center
   :alt: The Communication Server in the middle of the four servers

|

**Program:** ``andruavmainserver`` (Rust) · **Source code:**
`droneengage_server <https://github.com/DroneEngage/droneengage_server>`_

What It Does
============

- Accepts secure WebSocket (WSS) connections from units and WebClients.
- Routes messages to a group or to one unit.
- Connects to the :ref:`srv-authentication` to accept logins.
- Connects to the :ref:`srv-storage` to keep tasks, missions and offline messages.
- Asks the :ref:`srv-udp-relay` to open MAVLink pairs for :ref:`webclient-udp-telemetry`.
- Can connect to other Communication Servers (S2S relay) for large systems.

When a unit or a WebClient logs in, the Authenticator asks the Communication
Server for a temporary login key. The client then opens its WebSocket with
this key.

Deployment Modes
================

- **Standalone** — one server, for example the air-gap Pi.
- **Child server** — connects to a parent server, which relays its messages.
- **Parent (super) server** — accepts child servers and forwards messages between them.

|

Settings
========

The settings are in ``server.config``. Put your changes in
``server.config.local`` (see :ref:`srv-airgap-servers`).

**Identity and network**

.. list-table::
   :header-rows: 1
   :widths: 30 22 48

   * - Setting
     - Default
     - What it does
   * - ``server_id``
     - ``DE_CommSrv``
     - The name of this server.
   * - ``server_ip``
     - ``::``
     - The IP that the server listens on. ``::`` means all addresses.
   * - ``server_port``
     - ``9966``
     - The WSS port for units and WebClients.
   * - ``public_host``
     - ``airgap.local``
     - The IP or name that units and WebClients use to reach this server.
       Andruav on a phone may not know a local name, so use the IP of the Pi.
   * - ``ssl_key_file``, ``ssl_cert_file``
     - ``./ssl_local/ssl_airgap/…``
     - The SSL key and certificate.
   * - ``allow_fake_SSL``
     - ``true``
     - Accept a self-signed certificate. Keep ``true`` on an air-gap Pi.
   * - ``ca_cert_path``
     - ``./ssl_local/ssl_airgap/root.crt``
     - The root certificate of the self-signed certificates.

**Links to the other servers**

.. list-table::
   :header-rows: 1
   :widths: 30 22 48

   * - Setting
     - Default
     - What it does
   * - ``s2s_ws_target_ip``
     - ``127.0.0.1``
     - The IP of the Authenticator S2S link.
   * - ``s2s_ws_target_port``
     - ``19001``
     - The port of the Authenticator S2S link. It must be the same as
       ``s2s_ws_listening_port`` of the Authenticator.
   * - ``s2s_my_private_key``
     - ``./ssl_local/DE_ServerComm_private.pem``
     - The Ed25519 private key, if the Authenticator uses S2S keys.
   * - ``s2s_shared_secret_file``
     - ``./s2s_shared_secret.key``
     - The shared secret for the Storage Server and the UDP Relay. Copy it
       from the Storage Server folder.
   * - ``enable_storage_server``
     - ``true``
     - Use the :ref:`srv-storage`.
   * - ``storage_server_host``, ``storage_server_port``
     - ``127.0.0.1``, ``9000``
     - The address of the Storage Server.
   * - ``udp_relay``
     - one relay at ``127.0.0.1:9100``
     - The list of UDP Relays. An empty list means no UDP telemetry.
   * - ``udp_relay_select``
     - ``hash``
     - How to select a relay when there are many: ``hash``,
       ``first_healthy`` or ``least_loaded``.
   * - ``command_plugin``
     - one plugin
     - The command plugins to use. An air-gap Pi does not need plugins:
       set ``[]``.

**Protection**

.. list-table::
   :header-rows: 1
   :widths: 30 22 48

   * - Setting
     - Default
     - What it does
   * - ``outbound_guard.enabled``
     - ``true``
     - Protects the server from a slow client. When the queue of a client
       is large, the server skips old telemetry for that client. When the
       queue is too large, the server closes that connection, and the
       client connects again.
   * - ``outbound_guard.high_water_bytes``
     - ``262144``
     - Above this queue size, the server skips old telemetry.
   * - ``outbound_guard.hard_cap_bytes``
     - ``4194304``
     - Above this queue size, the server closes the connection.
   * - ``memory_max``
     - ``973``
     - The memory limit in MB. Above it, the server stops, and systemd
       starts it again.
   * - ``ws_auth_no_frame_old_compatibility``
     - ``false``
     - ``true`` lets old clients send the login key in the URL.

**Logs**

.. list-table::
   :header-rows: 1
   :widths: 30 22 48

   * - Setting
     - Default
     - What it does
   * - ``ignoreLog``
     - ``true``
     - ``true`` means no log files.
   * - ``log_directory``
     - ``./logs/``
     - The folder of the log files.
   * - ``debug_logging``
     - ``false``
     - Show more details on the console.

|

**Example** — a full ``server.config`` for an air-gap Pi:

.. code-block:: json

    {
        "server_id"              : "DE_CommSrv",
        "server_ip"              : "::",
        "public_host"            : "192.168.1.161",  // the IP of the Pi
        "server_port"            : 9966,
        "ssl_key_file"           : "./ssl_local/ssl_airgap/domain.key",
        "ssl_cert_file"          : "./ssl_local/ssl_airgap/domain.crt",
        "allow_fake_SSL"         : true,
        "ca_cert_path"           : "./ssl_local/ssl_airgap/root.crt",

        // Authenticator
        "s2s_ws_target_ip"       : "127.0.0.1",
        "s2s_ws_target_port"     : "19001",
        "s2s_my_private_key"     : "./ssl_local/DE_ServerComm_private.pem",

        // Storage Server and UDP Relay
        "s2s_shared_secret_file" : "./s2s_shared_secret.key",
        "enable_storage_server"  : true,
        "storage_server_host"    : "127.0.0.1",
        "storage_server_port"    : 9000,
        "udp_relay"              : [{ "host": "127.0.0.1", "port": 9100, "id": "DE_UdpRelay_1" }],

        "command_plugin"         : [],

        "ignoreLog"              : true,
        "log_directory"          : "./logs/",
        "debug_logging"          : false,
        "memory_max"             : 973
    }

|

.. warning::
    The file is JSON, but you can write comments with ``//`` and ``/* */``.

|

For Developers
==============

- **Language**: Rust (tokio). It replaces the earlier Node.js server and keeps the same wire protocol.
- **Build**: ``cargo build --release``. The program is ``target/release/andruavmainserver``.
- **Configuration**: ``server.config`` plus ``server.config.local``, or ``--config=<file>``.
- **Shared code**: `droneengage_server_common <https://github.com/DroneEngage/droneengage_server_common>`_ — config loader, S2S authentication, web helpers.

See :doc:`Server Technicals <technicals/server/de-server-technicals>` for routing, S2S relay, and configuration details.
