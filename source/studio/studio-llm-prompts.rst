.. image:: ../images/de_studio/engage-studio-logo-light.svg
   :width: 420px
   :align: center
   :alt: DroneEngage Studio logo

.. _studio-llm-prompts:

=================================
Use an AI Assistant (LLM Prompts)
=================================

An AI assistant (LLM) can write a good scenario quickly, if you give it
the correct context. ``docs/SCENARIOS.md`` in the Studio repository is
written for this purpose: you paste it into the prompt, and the
assistant has the full format.

This page tells you what context to give, and gives prompts that you
can copy.

.. warning::

   An assistant can invent a step, a fault or an assertion that does
   not exist. **Always run** ``./sim validate`` on what it writes. The
   validator refuses an unknown name and gives the correct list.

|

The context to give
===================

Give the assistant these items. The first two are the most important.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Item
     - Why
   * - ``docs/SCENARIOS.md`` (the full file)
     - the authoring reference: file shape, fleet keys, every ``do:``
       step, ``fault:`` kind and ``assert:`` check, rules and a complete
       example
   * - the output of ``./sim verbs --json``
     - the verb list from the engine registry. It is always current with
       the code that you run.
   * - one or two example files that are near your goal
     - the assistant copies a style that works. Good starters:
       ``scenarios/examples/mission_square.yaml``,
       ``scenarios/examples/link_fault.yaml``,
       ``tests/smoke_copters.yaml``, ``tests/fault_link_loss.yaml``.
   * - the output of ``./sim blocks``
     - the unit types that exist on your machine
   * - the output of ``./sim show <sim.yaml>``
     - when you use a ``sims/`` fleet: the real unit names
   * - ``README.md`` and ``wiki/BLOCKS_AND_SIMS.md``
     - when the task is about blocks, sims or server stacks, not a
       scenario

**For a coding agent** that can read files and run commands (Claude
Code, Codex, Cursor ...), point it at the repository in place of a
paste. The Studio has an ``AGENTS.md`` file and an index of topic files
in ``.agents/wiki/``:

- ``agents_run.md`` - the ``./sim`` CLI and exit codes,
- ``agents_extend.md`` - add blocks, modules, sims, tests, steps and
  assertions,
- ``agents_stubs.md`` - stub sensors,
- ``agents_notes.md`` - invariants and gotchas.

|

Rules to put in every prompt
============================

Copy these rules into your prompt. They prevent the most frequent
errors.

.. code-block:: text

   Rules for de.scenario/1 files:
   - The first line must be a '#' comment that says what the file proves.
   - Use only steps, faults and assertions from docs/SCENARIOS.md or
     `./sim verbs`. Do not invent names or arguments.
   - All paths are relative to the scenario file.
   - Link faults (link_cut, link_stall, link_profile, delay) need
     transport: fake, or transport: {type: real, link_proxy: true}.
     loss and clock faults need transport: fake.
   - Set mode GUIDED before a deploy of a nav mission.
   - arm waits for SITL GPS/EKF warm-up (1-2 min cold); use generous timeouts.
   - Journal re: patterns match the message text only, not the header.
   - Use teardown: land for anything that flies or drives.
   - Do not write fleet: or transport: together with sim:.

|

Prompt 1 - Write a new scenario
===============================

.. code-block:: text

   You are helping me write a DroneEngage Studio scenario in the
   de.scenario/1 format. The full reference is below (docs/SCENARIOS.md),
   then the output of `./sim verbs --json`, then one example file that works.

   <paste docs/SCENARIOS.md>
   <paste ./sim verbs --json>
   <paste scenarios/examples/mission_square.yaml>

   <paste the "Rules for de.scenario/1 files" block>

   Goal: <one sentence - what happens, to which units, and what PASS proves>
   Example: "Two copters fly copter_square on the real server. During the
   mission, copter c2 gets a 20 s GPS jam. Both missions must complete and
   de_comm on c2 must stay alive."

   Write the file as scenarios/<name>.yaml. After the file, list each
   assertion and tell in one line which evidence it reads.

Then run:

.. code-block:: bash

   ./sim validate scenarios/<name>.yaml
   ./sim run scenarios/<name>.yaml

|

Prompt 2 - Fix a validation error
=================================

.. code-block:: text

   `./sim validate` refuses my scenario. Here is the file and the full
   error output. Fix only what the error names. Do not change the goal
   of the test. Use only names from the reference.

   <paste the yaml>
   <paste the validate output>
   <paste ./sim verbs --json, if not already in the conversation>

|

Prompt 3 - Debug a FAIL
=======================

Give the assistant the evidence, not only the YAML. The ``RESULT`` line
at the end of the run gives the folder.

.. code-block:: text

   My scenario ran and failed. Find the cause. Tell me if the cause is
   (a) the scenario itself (wrong step order, wrong pattern, too short
   timeout, wrong transport), or (b) a real defect in a DroneEngage module.
   Give the evidence lines that prove your answer.

   The scenario:
   <paste the yaml>

   The last 60 lines of the console output (from "== assertions =="):
   <paste>

   summary.json:
   <paste var/results/<utc>/<name>/summary.json>

   The journal of the failing unit:
   <paste var/results/<utc>/<name>/<unit>/... journal lines>

   The module log, if a process died:
   <paste the relevant log lines>

.. tip::

   A coding agent can open the folder itself. Give it the ``RESULT``
   path and ask it to read ``summary.json`` first, then the unit
   journal, then the module logs.

|

Prompt 4 - Extend a scenario
============================

.. code-block:: text

   Here is a scenario that passes. Extend it. Keep all current steps and
   assertions. Add:
   - a <fault kind> fault on <unit> at t=<s> for <n> s,
   - an assertion that proves the fleet recovered (for example
     recovers_after_fault, or a journal_order offline -> online).
   If the new fault needs another transport, change it and tell me why.

   <paste the yaml>
   <paste docs/SCENARIOS.md, if not already in the conversation>

Other extensions you can ask for:

- "Add a negative control: one assertion that must fail when the
  feature is broken."
- "Make it a chaos run: add a ``chaos:`` block that draws ``loss``,
  ``freeze`` and ``mode`` faults on all units from t=120."
- "Change the fleet to ``sim: {base: copters3, with: [faults]}`` and
  update the unit names."
- "Add a boat (``cls: boat``) to the fleet and check that it ends in
  HOLD (``fc_mode``)."

|

Prompt 5 - Finish a recorded session
====================================

``./sim record`` writes the timeline but leaves ``assert:`` as a TODO.

.. code-block:: text

   This scenario was recorded from a live WebClient session with
   `./sim record`. The timeline is correct. Write the assert: block.
   What I wanted to check: <one sentence>.
   Also replace each "# unmapped:" comment with a correct step if one
   exists in the reference, or tell me that none exists.

   <paste the recorded yaml>
   <paste docs/SCENARIOS.md>

|

Prompt 6 - Explain a test
=========================

.. code-block:: text

   Explain this DroneEngage Studio test in plain words for a new team
   member. For each timeline step, tell what it does. For each assertion,
   tell what it proves and what a FAIL would mean.

   <paste the yaml, for example tests/fault_link_loss.yaml>

|

Prompt 7 - For a coding agent in the repository
===============================================

.. code-block:: text

   Work in the droneengage_studio repository. Read AGENTS.md, then
   .agents/wiki/agents_run.md and docs/SCENARIOS.md.
   Task: write scenarios/<name>.yaml that proves <goal>.
   Loop:
   1. Run ./sim validate on the file and fix each error.
   2. Run ./sim run on the file. If another sim is live, add
      --shared --slot-base any. Do not `./sim down` sims you did not start.
   3. Read the RESULT summary.json. If an assertion fails, read the unit
      journal and module logs and decide: scenario error or module defect.
   4. Fix scenario errors and run again. Report module defects to me with
      the evidence; do not change module code.
   Report: the file, the PASS/FAIL counts, and the RESULT path.

|

Check the work of the assistant
===============================

Before you keep a file that an assistant wrote:

1. ``./sim validate <file>`` passes.
2. The first comment really tells what PASS proves.
3. Each assertion reads evidence that your goal needs. An assertion
   that is always true proves nothing.
4. ``./sim run <file>`` passes. Run it again with another
   ``--seed`` if it has faults.
5. Break the feature on purpose (or change one value) and check that
   the test fails. Then put it back.
