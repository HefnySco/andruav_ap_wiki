.. _srv-authentication:



=====================
Authentication Server
=====================

The **Authenticator** is the login server of DroneEngage. It keeps the
accounts and the access codes. It checks each login and tells the client
which Communication Server to use.

**Program:** ``andruavauth`` (Rust) · **Source code:**
`droneengage_authenticator <https://github.com/DroneEngage/droneengage_authenticator>`_

.. image:: /images/diagrams_2026/airgap_login_flow_2026.svg
   :align: center
   :alt: Login sequence between a client, the Authenticator and the Communication Server

|

What It Does
============

- Registers users and makes access codes.
- Checks the logins of WebClients and units.
- Keeps a list of the Communication Servers that are connected.
- Has an admin web page for users and servers.
- Accepts the Communication Servers on an S2S link.

The Authenticator does not redirect the client. It sends a JSON reply with
the address and the port of the Communication Server and a temporary login
key. The client then uses them to open a WebSocket to the Communication
Server.

The accounts can be in one of three places: one account in
``server.config``, a JSON file, or a SQLite database.

Components
==========

The Authenticator runs three services at the same time:

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Service
     - Port
     - What it does
   * - API server
     - ``19408``
     - Login, register and the unit routes (HTTPS).
   * - Admin web page
     - ``8089``
     - Users, teams and the status of the servers. See :ref:`srv-admin-web-interface`.
   * - S2S server
     - ``19001``
     - The Communication Servers connect here and register.

|

Settings
========

The settings are in ``server.config``. Put your changes in
``server.config.local`` (see :ref:`srv-airgap-servers`).

**Server and accounts**

.. list-table::
   :header-rows: 1
   :widths: 32 24 44

   * - Setting
     - Default
     - What it does
   * - ``server_id``
     - ``AndruavAuth``
     - The name of this server.
   * - ``server_ip``
     - ``0.0.0.0``
     - The IP that the API server listens on.
   * - ``server_port``
     - ``19408``
     - The port of the API server. Units and the WebClient use this port.
   * - ``account_storage_type``
     - ``single``
     - Where the accounts are: ``single``, ``file`` or ``db`` (see below).
   * - ``single_account_user_name``
     - ``single@airgap.droneengage.com``
     - The account email for ``single`` mode.
   * - ``single_account_access_code``
     - ``test``
     - The access code for ``single`` mode. **Change it.**
   * - ``file_db``
     - ``./file_db.json``
     - The JSON file for ``file`` mode.
   * - ``dbdatabase``
     - ``database/andruav_DB.db``
     - The SQLite file for ``db`` mode.
   * - ``ignoreEmail``
     - ``true``
     - Do not send the access code by email. Keep ``true`` on an air-gap Pi.

**S2S link**

.. list-table::
   :header-rows: 1
   :widths: 32 24 44

   * - Setting
     - Default
     - What it does
   * - ``s2s_ws_listening_ip``
     - ``127.0.0.1``
     - The IP of the S2S server. Keep ``127.0.0.1`` when the Communication
       Server is on the same Pi.
   * - ``s2s_ws_listening_port``
     - ``19001``
     - The port of the S2S server.
   * - ``s2s_auth_enabled``
     - ``false``
     - ``true``: a Communication Server must prove its name with an Ed25519
       key from ``s2s_trusted_server_keys``.
   * - ``s2s_trusted_server_keys``
     - one key
     - The public key of each Communication Server, by ``server_id``.

**Admin web page and security**

.. list-table::
   :header-rows: 1
   :widths: 32 24 44

   * - Setting
     - Default
     - What it does
   * - ``webadmin_enable``
     - ``true``
     - Show the admin web page.
   * - ``webadmin_port``
     - ``8089``
     - The port of the admin web page.
   * - ``admin_username``, ``admin_password``
     - ``admin``, a hash
     - The admin login. Write ``$$HASH$$('my-password')`` to set a new password.
   * - ``session_secret``
     - —
     - A long random text that protects the admin sessions. **Change it.**
   * - ``servers_admin_url_guid``
     - empty
     - A secret word. When set, the admin page is only at
       ``/admin/<word>/login``. All other admin links give 404.
   * - ``webadmin_terminal_enabled``
     - ``true``
     - A shell terminal on the admin page. Set ``false`` if you do not need it.
   * - ``altcha_enabled``
     - ``true``
     - A small proof-of-work check on the public "create access code" form.
       You can set ``false`` on a closed network.
   * - ``enable_SSL``
     - ``true``
     - Use HTTPS. The key and the certificate are in ``ssl_key_file`` and
       ``ssl_cert_file``.

|

**Example** — ``server.config`` for an air-gap Pi:

.. code-block:: json

    {
        "server_id"                 : "AndruavAuth",
        "server_ip"                 : "0.0.0.0",
        "server_port"               : 19408,

        "account_storage_type"      : "single",   // single, file or db
        "single_account_user_name"  : "single@airgap.droneengage.com",
        "single_account_access_code": "my-new-code",
        "file_db"                   : "./file_db.json",
        "dbdatabase"                : "database/andruav_DB.db",
        "ignoreEmail"               : true,

        "s2s_ws_listening_ip"       : "127.0.0.1",
        "s2s_ws_listening_port"     : "19001",
        "s2s_auth_enabled"          : false,

        "enable_SSL"                : true,
        "ssl_key_file"              : "./ssl_local/ssl_airgap/domain.key",
        "ssl_cert_file"             : "./ssl_local/ssl_airgap/domain.crt",

        "webadmin_enable"           : true,
        "webadmin_port"             : 8089,
        "webadmin_listening_ip"     : "0.0.0.0",
        "admin_username"            : "admin",
        "admin_password"            : "$$HASH$$('my-admin-password')",
        "session_secret"            : "write-a-long-random-text-here",
        "webadmin_terminal_enabled" : false,

        "enableLog"                 : false,
        "log_directory"             : "./logs/"
    }

|

.. warning::
    The file is JSON, but you can write comments with ``//`` and ``/* */``.

|

Account Modes
=============

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Mode
     - Use it when
   * - ``single``
     - You need only one account. All units and WebClients share it. This
       is the easiest mode for an air-gap Pi.
   * - ``file``
     - You need a few accounts. The server keeps them in ``file_db.json``.
       Add and edit the accounts on the admin web page.
   * - ``db``
     - You need many accounts and teams. The server keeps them in a SQLite
       file. Manage them on the admin web page (**Teams & Logins**).

Logins in the same team share the same units. Logins in different teams do
not see the units of each other.

.. important::

    The IP and the port of the Authenticator are in the config of each
    DroneEngage unit and in the WebClient, because they connect to it first.

|

Tools
=====

Two helper programs are built with the server:

.. code-block:: bash

    # reset the access code of an account (in file mode, stop the server first)
    ./target/release/reset_access <account-name>

    # make a SQLite account database from a file-mode JSON file
    ./target/release/migrate_file_db ./file_db.json --output database/andruav_DB.db

|

For Developers
==============

- **Language**: Rust (tokio).
- **Build**: ``cargo build --release``. The program is ``target/release/andruavauth``.
- **Configuration**: ``server.config`` plus ``server.config.local``, or ``--config=<file>``.
- **Database**: SQLite, with migrations in ``database/migrations/``.

See :doc:`Server Technicals <technicals/server/de-server-technicals>` for the authentication flow, database schema, and API details.
