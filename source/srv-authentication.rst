.. _srv-authentication:



=====================
Authentication Server
=====================

The **Authenticator** is the central authentication and authorization server for DroneEngage. It issues accounts, access codes, and session tokens, and it authenticates Communication Servers using Ed25519 server-to-server (S2S) cryptography.

.. image:: ./images/seq_diagram_authentication.png
   :height: 400px
   :align: center
   :alt: Authentication Sequence Diagram

|

What It Does
============

- Registers users and generates Access Codes.
- Authenticates WebClient logins and unit connections.
- Manages registered Communication Servers.
- Provides an admin web interface for users and servers.
- Exposes a WebSocket S2S endpoint for server authentication.

The authenticator does not perform an HTTP redirect. Instead, it returns a JSON response containing the communication server address, port, and a temporary login key. The client then uses these details to establish a WebSocket connection to the communication server.

The accounts can be stored in various formats such as MySQL database, JSON file or as a single account defined in the server.config file.

Components
==========

The Authenticator runs three services simultaneously:

1. **API Server** (default port ``19408``) — REST API for login, register, agent routes.
2. **Views Server** (default port ``8089``) — EJS-based admin web interface.
3. **S2S WebSocket Server** (default port ``19001``) — Ed25519 challenge-response auth for servers.

|

**Source Code:** `https://github.com/DroneEngage/droneegnage_authenticator <https://github.com/DroneEngage/droneegnage_authenticator>`_


|

Settings
========

Settings is defined in a file called **server.config** the most important fields are:
    |br| **server_id**: Defines name of the server.
    |br| **server_ip**: Defines ip that is the server is listening to. default:0.0.0.0
    |br| **server_port**: Defines the port that is the server is listening to. default:19408
    |br| **account_storage_type**: Can be [single,file,db]. **single** means a single constant account, **file** means a simple JSON file stores names and passwords. **db** means a separate mysql database.
    |br| **single_account_user_name**: e.g. "single@airgap.droneengage.com" which is a single account when **account_storage_type** is **single**
    |br| **single_account_access_code**: e.g. "test" which is the password when **account_storage_type** is **single**
    |br| **db_users**: e.g. "./db_users.db" which is the JSON file name of accounts when  **account_storage_type** is **file**
    |br| **s2s_ws_target_ip**: The listinning ip that :ref:`srv-authentication` listens to waiting for a websocket connection from a :ref:`srv-communication`.
    |br| **s2s_ws_target_port**: This is the port for the same websocket connection between :ref:`srv-authentication` and :ref:`srv-communication`.

|

.. code-block:: json

    {
        "server_id"                 : "AndruavAuth", // server id
        "server_ip"                 : "0.0.0.0",
        "server_port"               : 19408,
        
        "account_storage_type"   : "single",  //[single,file,db]
        "single_account_user_name"  : "single@airgap.droneengage.com",
        "single_account_access_code": "test",
        "db_users"                  :"./db_users.db",
        

        
        "enableLog"                 : false,
        "log_directory"             : "./logs/",
        "log_timeZone"              : "GMT",
        "log_detailed"              : true,

        
        "s2s_ws_listening_ip"       : "127.0.0.1", 
        "s2s_ws_listening_port"     : "19001", 
        
        "enable_SSL"                : true,
        "ssl_key_file"              : "ssl/privkey.pem",
        "ssl_cert_file"             : "ssl/fullchain.pem",     
        

    }

|

.. warning::
    Although above is a JSON file but you can add comments to the code using ``//`` and ``/* */`` blocks.


|

DB_USERS File
-------------

When **account_storage_type** is **file** then field **db_users** is used to specify file path and name.

The file is a simple JSON format like in the following example:

.. code-block:: json

    {
        "user1@email.com": {
            "sid": 1,
            "pwd": "0001",
            "isadmin": true,
            "prm": "0xffffffff"
        },
        "user2@email.com": {
            "sid": 1,
            "pwd": "drone",
            "isadmin": true,
            "prm": "0xffffffff"
        },
        "user3@email.com": {
            "sid": 3,
            "pwd": "drone",
            "isadmin": true,
            "prm": "0xffffffff"
        },
    }

|

**user1** and **user2** share the same drones, they are just to logins that can be used via webclient and DroneEngage Communicator.
**user3** is another user that is separated from then as he/she has a separate SID value.

 

.. important::
    
    IP & port are defined in all DroneEngage-Communicator and Webclient because they need to connect to the server.

|

For Developers
==============

- **Runtime**: Node.js 18+.
- **Stack**: Express, EJS, SQLite3, Helmet, CORS, CSRF, rate limiting.
- **Key files**:
  - ``server.js`` — spawns all three services.
  - ``auth_server/js_auth_server.js`` — main auth controller.
  - ``auth_server/js_account_manager.js`` — user CRUD.
  - ``auth_server/js_s2s_auth.js`` — Ed25519 S2S auth.
  - ``routes/js_router_admin.js`` — admin routes.
- **Configuration**: ``server.config`` (JSON, supports ``--config`` override).
- **Database**: SQLite with migrations in ``database/migrations/``.

See :doc:`Server Technicals <technicals/server/de-server-technicals>` for the authentication flow, database schema, and API details.
