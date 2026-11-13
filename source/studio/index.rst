.. image:: ../images/de_studio/engage-studio-logo-light.svg
   :width: 420px
   :align: center
   :alt: DroneEngage Studio logo

.. _studio-index:

==================
DroneEngage Studio
==================

**DroneEngage Studio** (repository ``droneengage_studio``, also called
*Engage Studio*) is the simulation and test environment for DroneEngage.
It flies simulated copters, planes, rovers and boats on one computer.
Each simulated vehicle runs the **real** DroneEngage modules
(``de_comm`` and ``de_mavlink``) and talks to a **real** or a **fake**
DroneEngage server. You do not need a drone, a radio or root access.

You use one command for everything: ``./sim``.

- Start a fleet and look at it in the WebClient.
- Run a scripted test and get a PASS or FAIL result with evidence.
- Break things on purpose: cut a link, jam the GPS, kill a module,
  stop the server. Every fault has a seed, so you can repeat the run.

.. figure:: ../images/de_studio/Screenshot\ From\ 2026-11-13\ 22-09-26.png
   :width: 100%
   :align: center
   :alt: WebClient map of the search and rescue demo: drones fly to a detect.detected marker and an approval request for a payload drop waits at the bottom

   The ``sar_fleet_a`` search and rescue demo in the WebClient. The
   scout drones fly to the ``detect.detected`` point. The ambulance
   drone ``amb1`` asks the operator to approve the payload drop.

Read the pages in this order:

.. toctree::
   :titlesonly:
   :maxdepth: 1

   1. Getting Started and Fast Wins <studio-getting-started>
   2. Architecture and Design <studio-architecture>
   3. Design Your Own Scenarios <studio-design-scenarios>
   4. Use an AI Assistant (LLM Prompts) <studio-llm-prompts>

|

Which page do I need?
=====================

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - I want to...
     - Read
   * - install the Studio and see a test pass
     - :doc:`studio-getting-started`
   * - know how the Studio is built and what a server stack is
     - :doc:`studio-architecture`
   * - write a new test for my own feature
     - :doc:`studio-design-scenarios`
   * - ask an AI assistant to write or fix a scenario
     - :doc:`studio-llm-prompts`

.. note::

   These pages give the main facts. The full reference is in the
   Studio repository: ``README.md``, ``wiki/USER_GUIDE.md`` and
   ``docs/SCENARIOS.md``. ``./sim help`` shows every command and
   ``./sim <command> --help`` shows its flags.
