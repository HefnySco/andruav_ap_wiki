.. image:: ../images/de_studio/engage-studio-logo-light.svg
   :width: 420px
   :align: center
   :alt: DroneEngage Studio logo

.. _studio-design-scenarios:

=========================
Design Your Own Scenarios
=========================

This page shows how to write a new ``de.scenario/1`` file, run it, read
the PASS/FAIL evidence, and fix it. Read :doc:`studio-architecture`
first if you do not know the words *block*, *sim*, *transport* and
*journal*.

The full reference for every key, step, fault and assertion is
``docs/SCENARIOS.md`` in the Studio repository. ``./sim verbs`` prints
the same list from the engine.

|

Step 1 - Write down what PASS proves
====================================

Before you write YAML, write one sentence:

   *"When <this happens> to <these units>, the fleet must <do this>, and
   I see it in <this evidence>."*

Example: *"When copter c1 loses its server link for 15 s during a
mission, the mission must still complete, and the link monitor must see
c1 offline."*

This sentence becomes the first comment of the file. It is
**required**: the first line of each file must be a ``#`` comment that
tells what the file proves.

|

Step 2 - Make the file
======================

.. code-block:: bash

   ./sim new my_link_test

This writes ``scenarios/my_link_test.yaml`` from the template. Put your
own files in ``scenarios/``. Use ``tests/`` only for cases that CI must
run.

.. note::

   **All paths in the file are relative to the file.** A file in
   ``scenarios/`` uses ``../packages/...``. A file in
   ``scenarios/examples/`` uses ``../../packages/...``.

|

Step 3 - Select the transport
=============================

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Use
     - When
   * - ``transport: real``
     - the default choice: real routing through the real comm server
   * - ``transport: {type: real, link_proxy: true}``
     - link cuts, stalls and delay on the real server
   * - ``transport: fake``
     - packet loss (``loss``) and clock faults, or a unit with no SITL
       that only needs a link
   * - ``sim: copters3``
     - take the fleet and the server from a ``sims/`` file. Do not also
       write ``fleet:`` or ``transport:``.

|

Step 4 - Describe the fleet
===========================

Each unit has an ``id`` and a ``cls``. ``cls`` is ``copter``, ``plane``,
``rover``, ``static``, ``comm_only``, or the name of a block (for
example ``boat`` or ``copter_camera``).

.. code-block:: yaml

   fleet:
     - {id: c1, cls: copter}
     - {id: c2, cls: copter, at: {north_m: 0, east_m: 40}}   # 40 m east of home
     - {id: b1, cls: boat}
     - {id: s1, cls: static}                                 # ground node, no SITL

Optional unit keys: ``role``, ``modules`` (add stubs such as
``stub_ai_box``), ``params`` (flight controller parameters),
``config`` (module config overlay), ``home``, ``account``,
``fcb_proxy: true``, ``fcb_link``.

|

Step 5 - Write the timeline
===========================

Each step is ``{t: <seconds>, do: <step>, ...}`` or
``{t: <seconds>, fault: <kind>, ...}``. ``t`` counts from the start of
the scenario. The clock starts after bring-up.

.. code-block:: yaml

   timeline:
     - {t: 0,  do: mode, unit: c1, mode: GUIDED}   # GUIDED before a nav deploy
     - {t: 2,  do: deploy}                         # send the operation
     - {t: 6,  do: arm, unit: c1}                  # arm waits for GPS warm-up
     - {t: 9,  do: start}                          # start the mission
     - {t: 20, fault: link_cut, unit: c1, dur_s: 15}
     - {t: 25, do: wait_journal, unit: c1, re: "mission main completed",
        timeout: 300}

Steps you use most:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Step
     - Meaning
   * - ``mode``, ``arm``, ``disarm``, ``takeoff``, ``land``
     - flight controller commands (``unit``, ``mode``, ``alt``)
   * - ``deploy``, ``start``, ``abort``, ``stop``, ``clear``
     - operator actions on the operation
   * - ``wait``, ``wait_journal``, ``wait_log``, ``wait_online``
     - wait for time, a journal line, a module log line, or a unit
   * - ``kill``, ``restart``, ``freeze``, ``unfreeze``
     - process faults (``unit``, ``proc``)
   * - ``fire``
     - send an event to a unit
   * - ``operator``
     - act as the operator: ``approve``, ``deny``, ``confirm``,
       ``dismiss`` ...

Faults you use most: ``link_cut``, ``link_stall``, ``loss``, ``delay``,
``server_down``, ``module_kill``, ``battery``, ``gps_off``, ``gps_jam``,
``gps_glitch``, ``motor_out``, ``rc_fail``, ``compass_fail``,
``vibration``. ``dur_s`` restores the fault automatically where it
applies.

``unit:`` accepts a unit id, its position (``1``), ``block:<name>``, a
comma list, or ``all``.

.. tip::

   To react to an event, use a journal trigger in place of a time:

   .. code-block:: yaml

      - {on: {unit: s1, re: "comm line offline"},
         do: fire, event: go.now, once: true}

   The runner checks triggers only between steps. A long ``wait``
   blocks them. Use ``wait_journal`` with a ``timeout``.

|

Step 6 - Write the assertions
=============================

Assertions are the proof. Each one is ``{name: {args}}``.

.. code-block:: yaml

   assert:
     - journal_count: {unit: c1, re: "mission main completed", equals: 1}
     - link_offline:  {unit: c1, at_least: 1}
     - proc_alive:    {unit: c1, proc: de_comm}

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Assertion
     - Checks
   * - ``journal_count``
     - how many journal lines match ``re`` (``equals``, ``at_least``,
       ``at_most``)
   * - ``no_journal``
     - the pattern never appears
   * - ``journal_order``
     - line ``first`` comes before line ``then``
   * - ``journal_time_delta``
     - the time between two lines (``min_s``, ``max_s``)
   * - ``link_offline``
     - the monitor saw the unit drop offline
   * - ``proc_alive``, ``proc_dead``
     - process state at the end
   * - ``fc_mode``
     - the last flight controller mode
   * - ``telemetry_value``
     - a telemetry field in bounds (``pick: min|max`` for the extreme)
   * - ``no_unexpected_restart``
     - no process restarted outside a fault window
   * - ``recovers_after_fault``
     - link and telemetry come back within ``within_s``

.. important::

   A journal ``re:`` pattern matches only the message text of a line.
   It does not search the time stamp and header fields. Use a pattern
   such as ``"mission main completed"`` or ``"comm line offline"``.

|

Step 7 - Add the teardown and settle time
=========================================

.. code-block:: yaml

   settle_s: 20        # quiet seconds after the last step
   teardown: land      # land | reset | none

Use ``teardown: land`` for everything that flies or drives. A fleet
that stays in the air drains its battery and breaks the next run.

|

The complete file
=================

This is the full example from ``docs/SCENARIOS.md``:

.. code-block:: yaml

   # demo_fault - one copter loses its link mid-mission: the square must
   # still complete (missions are autonomous) and the link monitor must
   # have seen the unit offline.
   version: 1
   name: demo_fault
   transport: fake
   operation: ../packages/copter_square.json
   verify: {cli: ../tools/verify_wrap.js}
   settle_s: 20
   fleet:
     - {id: c1, cls: copter}
   timeline:
     - {t: 0,  do: mode, unit: c1, mode: GUIDED}
     - {t: 2,  do: deploy}
     - {t: 6,  do: arm, unit: c1}
     - {t: 9,  do: start}
     - {t: 20, fault: link_cut, unit: c1, dur_s: 15}
     - {t: 25, do: wait_journal, unit: c1, re: "mission main completed",
        timeout: 300}
   assert:
     - journal_count: {unit: c1, re: "mission main completed", equals: 1}
     - link_offline: {unit: c1, at_least: 1}
     - proc_alive: {unit: c1, proc: de_comm}
   teardown: land

For more examples, copy a file from ``scenarios/examples/``
(``mission_square``, ``link_fault``, ``unexpected_restart``,
``wp_reached_action``) or from ``tests/`` (``smoke_copters``,
``smoke_boat``, ``fault_link_loss``).

|

Step 8 - Validate, then run
===========================

.. code-block:: bash

   ./sim validate scenarios/my_link_test.yaml   # schema + files, starts nothing
   ./sim run scenarios/my_link_test.yaml

``validate`` finds an unknown step, fault or assertion, a wrong
argument, a missing file, or a fault that the transport does not
support. Fix all ``validate`` errors before you run.

Useful run flags:

.. code-block:: bash

   ./sim run <file> --seed 7       # a different seed (ports, faults, world)
   ./sim run <file> --keep         # keep the fleet up after the run
   ./sim run <file> --hold         # park after the timeline until Ctrl-C
   ./sim run <file> --shared       # do not stop the other live sims
   ./sim expand <file> --seed 7    # print the chaos fault schedule, run nothing

|

Step 9 - Read the evidence
==========================

Read the evidence in this order.

1. **The console.** Each timeline step prints a line. Each
   ``wait_journal`` prints when it matched. The ``== assertions ==``
   block prints ``[PASS]``, ``[FAIL]`` or ``[SKIP]`` with a detail, for
   example ``journal_count: value=1.0 (c1: 1 == 1)``. The last lines are
   the count (``5 PASS, 0 FAIL, 0 SKIP``) and
   ``RESULT <dir>/summary.json``.
2. **summary.json.** Each assertion has ``name``, ``status``, ``value``
   and ``detail``. ``step_ok`` tells if all steps passed. ``exit`` is
   the exit code. ``commits`` gives the commit of each component, so
   you know which build you tested.
3. **The unit journal** in ``var/results/<utc>/<name>/<unit>/``. It is
   the diary of each unit. Search it for the line your assertion
   expected.
4. **The module logs** for the real error: ``./sim logs <unit>
   <module>`` while the fleet is up, or the log files in the results
   folder.
5. ``links.jsonl``, ``telemetry.jsonl`` and ``operator.log`` for link,
   flight and operator evidence.

When the run uses the WebClient (for example with ``--hold`` or
``./sim view``), you can also read the evidence live in the **RUN**
view:

.. figure:: ../images/de_studio/Screenshot\ From\ 2026-11-13\ 22-07-39.png
   :width: 100%
   :align: center
   :alt: WebClient RUN view early in the run, with the timeline, the collaboration diagram and the story log

   The RUN view early in ``sar_fleet_a``. The story at the bottom shows
   the journal lines in time order, for example ``s3 emit
   detect.detected``. Use these lines to write your ``re:`` patterns.

.. figure:: ../images/de_studio/Screenshot\ From\ 2026-11-13\ 22-09-05.png
   :width: 100%
   :align: center
   :alt: RUN timeline with a hover box that lists the journal lines of unit sdr1

   Move the mouse over a mark in the timeline to see the journal lines
   behind it. Here ``sdr1`` starts the run, enters the ``search`` phase
   and activates the ``wide_search_rf`` mission.

.. note::

   SKIP is not FAIL. A test that needs a capability this machine does
   not have (``requires:``) SKIPs with the reason. A timing assertion
   in a ``realtime: true`` file SKIPs when SITL cannot run at 1x speed.

|

Step 10 - Fix it
================

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - What you see
     - What to do
   * - ``validate`` refuses a link fault on ``transport: real``
     - Use ``{type: real, link_proxy: true}``. For ``loss`` and clock
       faults, use ``transport: fake``.
   * - ``arm`` times out
     - Give a larger ``timeout``. SITL needs 1 to 2 minutes for GPS/EKF
       on a cold start.
   * - The deploy is refused
     - Set ``mode: GUIDED`` before ``deploy``. ``de_mavlink`` refuses
       nav loads in AUTO.
   * - ``wait_journal`` times out
     - Open the unit journal. Check that your ``re:`` matches the
       message text, not the header. Check that the step before it
       really happened.
   * - ``journal_count`` is 2, you expected 1
     - The fleet was reused and an old run was still loaded. Add
       ``{t: 0, do: stop}`` and ``{t: 0, do: clear}`` at the start, as
       ``tests/smoke_copters.yaml`` does.
   * - ``battery_low`` on the next run
     - Add ``teardown: land``. Do ``./sim down`` and run again.
   * - ``no_unexpected_restart`` fails
     - A process restarted outside a ``fault:`` window. Note that a
       ``do: kill`` is not a fault window; use ``fault: kill``.
   * - Results change from run to run
     - Set ``seed:`` in the file. The same seed gives the same ports,
       faults and world.

To try a new module build without a full rebuild of the fleet, use:

.. code-block:: bash

   ./sim try scenarios/my_link_test.yaml --module de_mavlink=<path-to-binary>

``try`` is ``run --keep``, so you can look at the live fleet after the
run with ``./sim ctl status``.

|

Step 11 - Make it strong
========================

- Run it with several seeds:
  ``./sim suite scenarios/my_folder --seeds 1,2,3``.
- Add a negative control: one assertion that must fail when the
  feature is broken (for example ``journal_count ... equals: 0`` for a
  line that must never appear).
- When the file is stable and CI must run it, move it to the correct
  feature folder under ``tests/`` (``faults/``, ``missions/``,
  ``fleet_bus/`` ...).

|

Record a session in place of writing it
=======================================

You can fly a sim by hand in the WebClient and let the Studio write
the timeline:

.. code-block:: bash

   ./sim record sims/copters3.yaml -o scenarios/my_recording.yaml
   # drive the WebClient, then push Ctrl-C
   ./sim validate scenarios/my_recording.yaml
   ./sim run scenarios/my_recording.yaml

Each WebClient command becomes a timeline step (``deploy``, ``arm``,
``mode``, ``start`` ...). A command with no verb stays in the file as a
``# unmapped:`` comment. The ``assert:`` block is a TODO: the recording
cannot know what you wanted to check, so you must write it.

``record`` works on ``server: {type: real}`` sims. It refuses a
``fake`` server. On an ``external`` server it prints one line that you
add to your own server's ``command_plugin``.

Next step: :doc:`studio-llm-prompts`.
