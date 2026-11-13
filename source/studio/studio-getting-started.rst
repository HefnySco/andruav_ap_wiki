.. image:: ../images/de_studio/engage-studio-logo-light.svg
   :width: 420px
   :align: center
   :alt: DroneEngage Studio logo

.. _studio-getting-started:

==============================
Getting Started and Fast Wins
==============================

This page gets you from an empty machine to a green test. It shows the
easy parts only. For the design of the Studio, read
:doc:`studio-architecture`.

The Studio runs on **Linux**. It is a set of Python 3 scripts. It has no
build step of its own. It starts programs that you build in other
repositories: ArduPilot SITL, the DroneEngage modules and the
DroneEngage servers.

|

What you need
=============

.. list-table::
   :header-rows: 1
   :widths: 30 45 25

   * - You need
     - How to get it
     - Needed for
   * - Python 3 packages
     - ``pip install websockets pymavlink pyyaml``
     - everything
   * - ArduPilot SITL
     - in your ``ardupilot`` checkout:
       ``./waf configure --board sitl && ./waf copter plane rover``
     - every flying or driving vehicle
   * - ``de_comm`` and ``de_mavlink`` binaries
     - ``./build.sh`` in ``droneengage_communication`` and
       ``droneengage_mavlink``
     - every unit
   * - The Rust servers
     - ``cargo build --release`` in ``droneengage_server`` (and in
       ``droneengage_authenticator`` for login tests)
     - the real server stack

Other modules (camera, GPIO, precision landing ...) are necessary only
when a block uses them. If a binary is missing, ``./sim up`` stops early
and gives the name of the binary.

|

Install
=======

Option A - Docker (fastest)
---------------------------

The Docker image has SITL, the DroneEngage binaries and the 3D viewer
inside it.

.. code-block:: bash

   docker build -f docker/Dockerfile -t de-sim .
   docker run -it --network host de-sim

The container runs the forest canopy search demo.

Option B - on your machine
--------------------------

1. Copy the example settings file. Do this one time on each machine.

   .. code-block:: bash

      cp sim.local.env.example sim.local.env

2. Open ``sim.local.env``. Set two paths:

   - ``DE_CODE`` - the folder that holds your DroneEngage checkouts.
   - ``ARDUPILOT_DIR`` - your ``ardupilot`` checkout with SITL built.

   All other lines are optional. Git ignores this file, so it stays on
   your machine.

3. Check the machine:

   .. code-block:: bash

      ./sim doctor

   ``doctor`` prints one ``OK``, ``MISSING`` or ``OPTIONAL`` line for each
   item. For each ``MISSING`` line, it gives the command that fixes it.
   When all lines are ``OK`` or ``OPTIONAL``, you are ready.

.. tip::

   ``./sim doctor sims/copters3.yaml`` checks only the items that this
   one sim needs. ``./sim doctor --caps`` shows the optional
   capabilities (camera, v4l2loopback, Android, 3D viewer) that this
   machine has.

|

Your first look: ``./sim show``
===============================

``./sim show`` reads a sim file and prints the units and ports it makes.
It **starts nothing**, so it is safe to try first.

.. code-block:: bash

   ./sim show sims/copters3.yaml

Example output (the ports are filled in when the sim starts):

.. code-block:: text

   Server real: wss None control None slot 40
     copter1     block=copter   copter sysid=40 ...  @-35.363262,149.165237
     copter2     block=copter   copter sysid=41 ...  @-35.363082,149.165237
     copter3     block=copter   copter sysid=42 ...  @-35.362903,149.165237

Other read-only commands:

.. code-block:: bash

   ./sim list                 # every file you can run, with one line each
   ./sim blocks               # the vehicle types you can use
   ./sim validate tests/smoke_copters.yaml   # check a file, start nothing

|

Your first run: ``./sim run``
=============================

.. code-block:: bash

   ./sim run tests/smoke_copters.yaml

This is the "hello world" test. The Studio:

1. starts three simulated copters and a real DroneEngage server,
2. sends each copter a square mission,
3. arms the copters and starts the mission,
4. waits until each copter reports ``mission main completed``,
5. checks the assertions and prints PASS or FAIL,
6. lands the fleet.

.. important::

   **The first run is slow.** A simulated vehicle needs about 1 to 2
   minutes of GPS warm-up before it can arm, the same as a real drone.
   Later runs on the same fleet use the warm fleet again, so they start
   faster.

The end of the output looks like this:

.. code-block:: text

   == assertions ==
     [PASS] journal_count: value=1.0 (...)
     ...
   5 PASS, 0 FAIL, 0 SKIP
   results: .../var/results/<utc>/smoke_copters
   RESULT .../var/results/<utc>/smoke_copters/summary.json

Exit code ``0`` means that all steps and assertions passed. The
``RESULT`` line is always the last line. It points to the full report.

.. note::

   ``./sim run`` **owns the machine**: it stops all other live sims
   first, because a test needs a clean machine. Add ``--shared`` to
   keep the other sims alive.

When you finish, stop everything:

.. code-block:: bash

   ./sim down

|

Fast wins
=========

These files are in the Studio repository. Each one runs with no extra
hardware. Run them in this order.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Command
     - What you see
   * - ``./sim run scenarios/examples/link_fault.yaml``
     - The smallest fault test. One ground unit (no SITL) on the fake
       server loses its link for 20 s. The test passes when the link
       monitor sees the unit go offline and ``de_comm`` stays alive.
       There is no GPS warm-up, so it is fast.
   * - ``./sim run scenarios/examples/mission_square.yaml``
     - The smallest flight. One copter on the real server gets the
       square mission, flies it and lands.
   * - ``./sim run tests/smoke_copters.yaml``
     - Three copters fly the square together on the real server.
   * - ``./sim run tests/smoke_boat.yaml``
     - One motor boat (ArduRover SITL, motorboat frame) drives a
       2-waypoint mission and holds.
   * - ``./sim run tests/fault_link_loss.yaml``
     - Three copters fly on the fake server. ``copter2`` gets 40 %
       packet loss. ``copter3`` loses its link for 45 s. The missions
       must still complete.
   * - ``./sim suite --tier smoke``
     - The fast first-pass set: one probe for each main subsystem.

|

Sit at a live fleet
===================

A test runs to the end and stops. To fly a fleet by hand, use
``studio`` or ``up``.

.. code-block:: bash

   ./sim studio sims/copters3.yaml

``studio`` starts the fleet, opens the WebClient planner already logged
in to the sim, starts the Mavlink3DMap 3D viewer when it is installed,
and prints one status block. Push Ctrl-C to leave. The fleet stays up.
Add ``--down`` to stop it when you leave.

To start a fleet and control it from the command line:

.. code-block:: bash

   ./sim up sims/copters3.yaml
   ./sim ctl status                  # units, ports, online state
   ./sim ctl arm all
   ./sim ctl mode copter2 RTL
   ./sim ctl land all
   ./sim logs copter1 de_comm        # tail one module log
   ./sim down copters3

``./sim ctl`` with no arguments prints all operator commands.

Watch a demo in 3D
------------------

.. code-block:: bash

   ./sim view scenarios/demos/world_canopy_viewer.yaml

A copter sweeps a forest to find a hiker. The command prints the 3D
viewer URL. The viewer needs ``MAVLINK3DMAP_DIR`` in ``sim.local.env``.

The full search and rescue demo has six copters:

.. code-block:: bash

   ./sim view scenarios/demos/sar_fleet_a.yaml --with viewer

.. figure:: ../images/de_studio/Screenshot\ From\ 2026-11-13\ 22-06-29.png
   :width: 100%
   :align: center
   :alt: Mavlink3DMap 3D viewer in a four-view layout over a forest canopy, with drone labels, a phone marker and the world truth panel

   ``sar_fleet_a`` in the Mavlink3DMap 3D viewer, with four views. The
   panel at the top right shows the world truth: ``phone_1`` is seen,
   ``person_1`` is not seen yet.

.. figure:: ../images/de_studio/Screenshot\ From\ 2026-11-13\ 22-06-45.png
   :width: 100%
   :align: center
   :alt: 3D viewer help overlay that lists the keyboard keys

   Push **F1** in the 3D viewer to show the keys: select a drone (1-9),
   change the camera (O, P, W A S D Q E), show labels (L) and save
   the multi-view layout (Ctrl+S).

.. figure:: ../images/de_studio/Screenshot\ From\ 2026-11-13\ 22-07-29.png
   :width: 100%
   :align: center
   :alt: WebClient with six simulated drones on the map and the fleet table with role, state, mission and battery for each unit

   The same demo in the WebClient. The six units (``amb1``, ``s1`` to
   ``s3``, ``scout1``, ``sdr1``) are online. The fleet table shows the
   role, state, mission and battery of each unit.

|

Use your own servers and WebClient
==================================

You can show simulated vehicles in your own WebClient. First start the
local server stack, then connect a drone, then start the WebClient:

.. code-block:: bash

   ./sim up de_servers
   ./sim up quadcopter
   ./sim up de_webclient --open-web

``sims/quadcopter.yaml``, ``sims/rover.yaml``, ``sims/plane.yaml`` and
``sims/boat.yaml`` connect to a server stack that you run. The logins
come from ``SIM_AUTH_*`` in ``sim.local.env``, or you can add
``--user <email> --password <code>`` to ``up``.

.. important::

   The unit accounts and the WebClient account must be in the **same
   team**. If not, the WebClient does not show the drones.

To let a phone (for example the Andruav app) connect to these servers,
give the address that the phone can reach:

.. code-block:: bash

   ./sim up de_servers --out 192.168.1.20

Stop in this order: ``./sim down quadcopter``, ``./sim down``, then
``./sim down de_servers``.

|

When something goes wrong
=========================

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Symptom
     - Cause and fix
   * - ``missing binaries`` on ``sim up``
     - A module is not built. The error gives its name. Run
       ``./build.sh`` in that repository.
   * - ``arm`` waits for a long time
     - This is normal on a cold start. SITL needs 1 to 2 minutes for
       GPS/EKF. ``arm`` waits for it.
   * - ``port already in use``
     - Another sim or your own server has the port. ``./sim sims`` shows
       what is live. ``./sim down`` stops it.
   * - Login fails on an ``external`` sim
     - The account does not exist, it is in a different team, or you
       did more than 10 logins in one minute. Wait one minute and try
       again.
   * - Test fails with ``battery_low``
     - An earlier run left the fleet in the air. Use ``teardown: land``,
       or do ``./sim down`` and start again.
   * - Everything looks stuck
     - Do ``./sim down``, then ``./sim up <file> --fresh``. Read
       ``./sim logs <unit> <module>`` for the real error.
   * - Old files use disk space
     - ``./sim clean --dry-run`` shows what it removes. ``./sim clean``
       removes old run and result folders. It never touches a live sim.

Next step: :doc:`studio-architecture`.
