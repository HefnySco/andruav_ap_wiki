.. _andruav-communication-protocol-messages:

=====================
Andruav Messages Type
=====================

.. warning::
    Message IDs are under constant updates. The authoritative source is
    always the code: `de_common/de_databus/messages.hpp
    <https://github.com/DroneEngage/droneengage_communication/blob/master/src/messages.hpp>`_,
    which as of the 2026 protocol audit carries a doc comment above every
    message constant (direction, send rate, and drop/keep-latest guidance).
    This page is a curated, browsable rendering of that same header - if
    the two ever disagree, the header wins.

How to Read This Reference
===========================

Each entry below documents one message type as it is actually used in the
current codebase (traced through sender + receiver code across all C++/
Python/Node.js modules and the React webclient), not just its original
intent.

:Direction:
    ``WEB_TO_MODULE`` - GCS webclient sends it to an onboard module (a command).
    ``MODULE_TO_WEB`` - onboard module sends it to the GCS webclient (telemetry/status).
    ``BIDIRECTIONAL`` - used both ways, often request/response.
    ``MODULE_TO_MODULE`` - internal only, never reaches the webclient.
    ``DRONE_TO_DRONE`` - peer unit to peer unit, via the comm server or P2P mesh.
    ``DEAD/UNUSED`` - the constant is defined but no matching sender+receiver pair exists in the current codebase.

:Rate:
    How often the message is actually sent, for periodic/frequent messages:
    ``ON_DEMAND`` (one-shot, event/user-triggered) · ``LOW`` (interval
    ≥5s) · ``MEDIUM`` (~1-5s) · ``HIGH`` (~100-999ms) · ``REALTIME``
    (streamed continuously, ≤100ms, or tied to frame rate).

:Discard:
    Guidance for a link-quality-aware sender - can this message be safely
    dropped or coalesced (keep-latest-only) when the connection is
    congested? ``YES`` - latest-value semantics, a newer message fully
    supersedes an older one. ``NO`` - must be delivered reliably (a
    command, a one-time event, a chunk in a reassembled payload, or a raw
    byte stream where loss corrupts state).

Messages marked **DEAD/UNUSED** are kept in this reference because the
constant still exists in the header and may still appear in older client
code - but nothing in the current codebase sends and receives a matching
pair. Treat them as historical, not as something to build new integrations against.

Binary & Chunked Messages
===========================

Two distinct byte-layout mechanisms show up across the categories below
- worth understanding once rather than re-deriving from each message's
field list.

.. image:: /images/diagrams_2026/binary_message_anatomy_2026.svg
   :alt: Binary message anatomy - JSON header plus null terminator plus binary payload, and WayPoints' separate manual chunk format
   :width: 90%
   :align: center

*Draft diagram - under review, see*
``images/diagrams_2026/binary_message_anatomy_2026.txt``
*for the intended content and known issues.*

A **binary-attachment** message (``IMG``, ``SDR_SPECTRUM``, ``TELNET_DATA``)
is a JSON text header, a null terminator, then raw binary bytes appended
directly after. A **manually-chunked** message (``WayPoints`` only) is
a different mechanism entirely: each UDP packet carries its own small
``i`` field marking ``WAYPOINT_CHUNK`` (1) or ``WAYPOINT_LAST_CHUNK``
(999), with no per-chunk acknowledgment - do not confuse this with
de_common's own lower-level UDP chunking (2-byte chunk number + data,
``0xFFFF`` = last chunk), which is a separate, transparent mechanism
used by large single messages like ``UploadWayPoints``.

Envelope & Routing (constants, not message types)
=================================================

.. rubric:: CMD_TYPE_INTERMODULE ("uv") / CMD_TYPE_SYSTEM_MSG ("s") — uv / s


Top-level command-type marker. ``uv`` sends a message from one module to another (e.g. emulate a GCS-originated command from inside a module). Anything else routes through the communicator as a normal message.

.. rubric:: CMD_COMM_GROUP / CMD_COMM_INDIVIDUAL / CMD_COMM_SYSTEM — g / i / s


Routing type carried in field ``ty``. GROUP broadcasts to a group (overrides individual); INDIVIDUAL targets one party_id (or a reserved name below); SYSTEM is handled by the comm server itself (task/account-level messages).

.. rubric:: Reserved target names — _GCS_ / _AGN_ / _GD_ / _SYS_


``_GCS_`` = all GCS/web clients; ``_AGN_`` = all agents/drones; ``_GD_`` = all GCS and agents; ``_SYS_`` = the comm server itself.

.. rubric:: Andruav protocol envelope fields — gr, sd, tg, mt, ms, p, ty, GU, ew, ef, ls


Every message carries: ``gr`` group id, ``sd`` sender party id, ``tg`` target party id, ``mt`` message type (numeric, this reference), ``ms`` message command payload (JSON string), ``p`` permission bitmask, ``ty`` routing type (see above), ``GU`` module key. ``ew``/``ef``/``ls`` support the wait/fire event linking mechanism between chained mission actions.

.. rubric:: Socket status codes — 1-8


FRESH(1), CONNECTING(2), DISCONNECTING(3), DISCONNECTED(4), CONNECTED(5), REGISTERED(6, connected + AddMe executed), UNREGISTERED(7), ERROR(8).

Module Registration & Internal RPC
==================================

.. rubric:: TYPE_AndruavModule_ID — 9100

:Direction: MODULE_TO_MODULE
:Rate: ON_DEMAND - once on connect, plus on-demand resend
:Discard: NO - identity/registration, must be delivered

Module registers itself with the comm broker.

**Fields:** a module_id, b module_class, c module_messages filter list, d module_features [T,R], e module_key, s hardware_serial, t hardware_serial_type, v module_version, z resend flag — all REQUIRED

.. rubric:: TYPE_AndruavModule_RemoteExecute — 9101

:Direction: MODULE_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO - it is an RPC call, dropping it silently loses the request

Generic "call this action on another module" RPC envelope; sub-command carried in nested field "C" (often reuses a TYPE_AndruavMessage_* id as the verb).

**Fields:** C int REQUIRED - sub-command/action id

.. rubric:: TYPE_AndruavModule_Location_Info — 9102

:Direction: MODULE_TO_MODULE
:Rate: HIGH - periodic ~300ms
:Discard: YES - latest position supersedes older ones

FCB broadcasts vehicle position to other onboard modules (e.g. camera geotagging).

**Fields:** la/ln int REQUIRED (lat/lon degE7), a int REQUIRED (abs alt mm), r int REQUIRED (rel alt mm), ha int OPTIONAL (horiz accuracy mm), y int OPTIONAL (yaw cdeg)

Core Telemetry & Unit State
===========================

.. rubric:: TYPE_AndruavMessage_GPS — 1002

:Direction: MODULE_TO_WEB
:Rate: HIGH - periodic ~1000ms (1Hz)
:Discard: YES - only the latest fix matters

Reports a unit's own GPS fix (sent by de_comm for a control-unit; the drone/FCB instead forwards raw MAVLink GPS under MAVLINK).

**Fields:** la/ln float REQUIRED; a/r float REQUIRED (abs/rel altitude, m); y int always 0 (unused); 3D int REQUIRED (3D fix indicator); SC int REQUIRED (satellite count); p int REQUIRED (provider, always 0); c/t/s OPTIONAL (accuracy/timestamp/ground speed)

.. rubric:: TYPE_AndruavMessage_POWER — 1003

:Direction: DEAD/UNUSED

Defined but never constructed or parsed anywhere. Real battery telemetry is forwarded as raw MAVLink BATTERY_STATUS under TYPE_AndruavMessage_MAVLINK.

.. rubric:: TYPE_AndruavMessage_ID — 1004

:Direction: BIDIRECTIONAL
:Rate: LOW - ~10s heartbeat, plus immediate resend on connect/restart/state change
:Discard: YES for the periodic refresh - but always resend after reconnect or a real state change

Unit identity/state heartbeat: vehicle type, flight mode, GPS mode, name, permissions, module list. Also answerable on-demand via RemoteExecute{C:1004}.

**Fields:** VT,GS,VR,B,FM,GM,C,UD,DS,p,dv,m1,T REQUIRED; TP OPTIONAL; b,FI,AP,FL,AR,SD,x,y,n,o,q,z,a OPTIONAL (present only when truthy/non-default)

.. rubric:: TYPE_AndruavMessage_DroneReport — 1020

:Direction: MODULE_TO_WEB
:Rate: ON_DEMAND - fired only when a mission waypoint is reached
:Discard: NO - a discrete milestone event

Drone-side report event (currently only "mission waypoint reached").

**Fields:** R int REQUIRED (report type, only Drone_Report_NAV_ItemReached=1 defined); P int REQUIRED (mission sequence number reached)

.. rubric:: TYPE_AndruavMessage_Error — 1008

:Direction: MODULE_TO_WEB
:Rate: ON_DEMAND - fired only on error conditions, no timer
:Discard: NO - alerts must be delivered

Error/notification report (module lifecycle failures, permission denials, etc).

**Fields:** EN int REQUIRED (error number); IT int REQUIRED (reporting component); NT int REQUIRED (severity, see NOTIFICATION_TYPE_*); DS string REQUIRED (description)

.. rubric:: TYPE_AndruavMessage_NAV_INFO — 1036

:Direction: DEAD/UNUSED as this JSON type

Roll/pitch/yaw/nav-error info. The webclient still has a legacy parser for it, but drone_engage_mavlink sends the equivalent as raw MAVLink (ATTITUDE/NAV_CONTROLLER_OUTPUT/VFR_HUD) under TYPE_AndruavMessage_MAVLINK instead.

.. rubric:: TYPE_AndruavMessage_CommSignalsStatus — 1059

:Direction: MODULE_TO_WEB
:Rate: unknown from this repo, treat as MEDIUM/LOW
:Discard: YES - a signal-strength snapshot, latest reading is sufficient

Cellular signal status of a unit (sender module - likely an Android/mobile companion app - not present in this repo, only consumers found here).

**Fields:** r number REQUIRED (signal dBm); s number REQUIRED (network type code); op/c/ds OPTIONAL (operator, country ISO, data state)

.. rubric:: TYPE_AndruavMessage_MODULE_HEALTH_STATUS — 6535

:Direction: MODULE_TO_WEB
:Rate: LOW - ~15-30s depending on module
:Discard: YES - the single best candidate in the whole protocol to drop entirely under a degraded link

Periodic self-reported module health/memory status (RSS, VmPeak, VmSwap, thread count, growth trend). Sent by CFacade_Base::sendMemoryStatus(); any C++ module linking de_common gets this for free, but sdr/telnet/tracking/camera_2025/mavlink do not currently call it.

**Fields:** a MODULE_HEALTH_ACTION_STATUS; rs/pk/sw MB (RSS/VmPeak/VmSwap); th thread count; sl MB/hour growth rate; tr trend (UP/DOWN/STABLE); hs status (OK/WARNING/CRITICAL); up seconds since monitor start

Flight Control Commands
=======================

.. rubric:: TYPE_AndruavMessage_FlightControl — 1010

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO - flight-mode command, safety-relevant

Change flight mode.

**Fields:** F unsigned int REQUIRED - Andruav flight-mode code

.. rubric:: TYPE_AndruavMessage_Arm — 1030

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO - critical safety command, permission-gated (PERMISSION_ALLOW_GCS_MODES_CONTROL)

Arm/disarm the vehicle.

**Fields:** A bool REQUIRED (arm/disarm); D bool OPTIONAL (force/emergency disarm)

.. rubric:: TYPE_AndruavMessage_ChangeAltitude — 1031

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO

Change target altitude (routes to DE-Pilot or direct MAVLink).

**Fields:** a float/unsigned REQUIRED - target altitude (m)

.. rubric:: TYPE_AndruavMessage_Land — 1032

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO - critical safety command

Land the vehicle.

**Fields:** none (empty payload)

.. rubric:: TYPE_AndruavMessage_GuidedPoint — 1033

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO

"Fly here" - fly to a guided point. Module replies with DistinationLocation.

**Fields:** a/g float REQUIRED (lat/lon); l float/unsigned OPTIONAL (alt mm, keeps current relative alt if absent); x/y/z OPTIONAL (sent but not consumed)

.. rubric:: TYPE_AndruavMessage_CirclePoint — 1034

:Direction: WEB_TO_MODULE (intended) - DEAD on receiving side
:Rate: ON_DEMAND (intended)
:Discard: NO (intended)

"Circle here" - webclient sends it (API_do_CircleHere) but drone_engage_mavlink has no case for it. Currently a no-op end-to-end.

**Fields:** a lat, g lon, l alt, r radius, t turns

.. rubric:: TYPE_AndruavMessage_DoYAW — 1035

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO

Yaw the vehicle to a target angle/rate; routed to DE-Pilot or direct MAVLink.

**Fields:** A number REQUIRED (target_angle); R number REQUIRED (turn_rate); C bool REQUIRED (clockwise); L bool REQUIRED (relative)

.. rubric:: TYPE_AndruavMessage_DistinationLocation — 1037

:Direction: MODULE_TO_WEB
:Rate: ON_DEMAND - one-shot echo
:Discard: YES - purely informational echo of the just-sent command

Confirms the target of a GuidedPoint/CirclePoint after processing.

**Fields:** P int REQUIRED (target_type/DESTINATION_* marker); T/O/A float REQUIRED (lat/lon/alt)

.. rubric:: TYPE_AndruavMessage_ChangeSpeed — 1040

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO

Change target speed.

**Fields:** a float/unsigned REQUIRED (speed); b bool REQUIRED (is_ground_speed); c float/int REQUIRED (throttle); d bool REQUIRED (is_relative)

.. rubric:: TYPE_AndruavMessage_SET_HOME_LOCATION — 1048

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO

Set the home location.

**Fields:** T/O float REQUIRED (lat/lon); A float REQUIRED (alt; falls back to current FCB home alt if 0)

.. rubric:: TYPE_AndruavMessage_HomeLocation — 1022

:Direction: BIDIRECTIONAL
:Rate: ON_DEMAND
:Discard: YES - idempotent/re-derivable, safe to drop under a congested link

Home position: pushed on FCB update, and as reply to an explicit request.

**Fields:** T/O/A float REQUIRED (lat/lon/alt)

.. rubric:: TYPE_AndruavMessage_RemoteControlSettings — 1047

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO - a mode-change command

Engage/release RC input mode (gamepad session start/stop), not a per-frame stream itself.

**Fields:** b unsigned int REQUIRED - RC_SUB_ACTION (0 RELEASED, 1 CENTER_CHANNELS, 2 FREEZE_CHANNELS, 4 JOYSTICK_CHANNELS, 8 JOYSTICK_CHANNELS_GUIDED)

.. rubric:: TYPE_AndruavMessage_RemoteControl2 — 1052

:Direction: WEB_TO_MODULE
:Rate: REALTIME - streamed every 250ms while gamepad engaged
:Discard: YES - the canonical "safe to drop under a bad link" message in this protocol

Continuous joystick/gamepad axis stream while engaged (RC channel values).

**Fields:** R/T/A/E unsigned REQUIRED (Rudder/Throttle/Aileron/Elevator, [0,1000]); w/x/y/z int OPTIONAL (Aux 1-4; -999 = release channel)

.. rubric:: TYPE_AndruavMessage_ServoChannel — 6001

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO - permission-gated (PERMISSION_ALLOW_GCS_MODES_SERVOS)

Sets a servo channel value from the webclient's manual servo dialog and gamepad handlers. Despite the legacy "OBSOLETE" naming, this is ACTIVELY USED.

**Fields:** n int REQUIRED (servo channel); v int REQUIRED (servo value, 0->1000, 9999->2000 special-cased)

.. rubric:: TYPE_AndruavMessage_DEPilot_Control — 1081

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO - permission-gated (PERMISSION_ALLOW_GCS_MODES_CONTROL) flight-behavior command

Engage DE-Pilot autonomous control (stabilization/altitude/tracking/yaw).

**Fields:** e bool OPTIONAL (enable); m int OPTIONAL (DEPILOT_OP_* mode); q bool OPTIONAL (enqueue vs immediate); d int(ms) OPTIONAL (duration); l float(m) OPTIONAL (target altitude); y float(deg) OPTIONAL (target yaw)

RemoteExecute Envelope & Sub-Commands
=====================================

.. image:: /images/diagrams_2026/remoteexecute_pattern_2026.svg
   :alt: RemoteExecute request/response idiom - WebClient sends RemoteExecute with C equal to a target message type, module replies with a message of that same type
   :width: 85%
   :align: center

*Draft diagram - under review, see*
``images/diagrams_2026/remoteexecute_pattern_2026.txt``
*for the intended content and known issues.*

.. rubric:: TYPE_AndruavMessage_RemoteExecute — 1005

:Direction: BIDIRECTIONAL - mostly WEB_TO_MODULE, also MODULE_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO - it is a command/request envelope, not a state snapshot

Execute a remote command on another unit. "C" can be a command id below 1000 (RemoteCommand_*) or equal to another TYPE_AndruavMessage_* id, in which case the target replies with that same message type (e.g. RemoteExecute(TYPE_AndruavMessage_ID) == "send me your ID").

**Fields:** C int REQUIRED (target command id); Act OPTIONAL (context-dependent activate flag); other fields vary by C

.. rubric:: RemoteCommand_* (sub-commands, carried in RemoteExecute's "C" field) — 500-508, 105-118

:Direction: WEB_TO_MODULE unless noted
:Rate: ON_DEMAND
:Discard: NO (one-shot commands)

GET_WAY_POINTS(500, DEAD - no receiving case today), RELOAD_WAY_POINTS_FROM_FCB(501), CLEAR_WAY_POINTS(502, permission-gated), CLEAR_FENCE_DATA(503, permission-gated), SET_START_MISSION_ITEM(504), REQUEST_PARA_LIST(505), SET_UDPPROXY_CLIENT_PORT(506, permission-gated), MISSION_COUNT(507), MISSION_CURRENT(508, shares handler with 507) — mission/waypoint sub-commands.

Camera sub-commands: ROTATECAM(105), TELEMETRYCTRL(108, permission-gated), STREAMVIDEO(110, DEAD-ish), RECORDVIDEO(111), STREAMVIDEORESUME(112, DEAD), SWITCHCAM(114, DEAD in practice), CONNECT_FCB(118, no-op stub).

Camera & Video
==============

.. rubric:: TYPE_AndruavMessage_IMG — 1006

:Direction: MODULE_TO_WEB
:Rate: ON_DEMAND - one per captured image, can burst
:Discard: NO - each image is unique payload data

Captured still image (binary message: JSON header + raw image bytes).

**Fields:** prv OPTIONAL ("gps" or absent); lat/lng/alt float REQUIRED (0 if no fix); tim int REQUIRED; trailing binary image bytes REQUIRED (may be zero-length on failure); des/spd/ber/acc OPTIONAL, reserved

.. rubric:: TYPE_AndruavMessage_CameraList — 1012

:Direction: MODULE_TO_WEB
:Rate: ON_DEMAND - event-triggered, plus reply to request
:Discard: NO - reasonably low frequency, treat as authoritative state

List of cameras available on a unit (capabilities, recording state).

**Fields:** T array REQUIRED, each {v,ln,id,active,r,p,s,a}; R bool REQUIRED (true only when replying to a request)

.. rubric:: TYPE_AndruavMessage_Signaling — 1021

:Direction: BIDIRECTIONAL
:Rate: ON_DEMAND - one per signaling event
:Discard: NO - SDP/ICE loss breaks call setup

WebRTC signaling (SDP offer/answer, ICE candidates, hangup) for camera streaming.

**Fields:** w object REQUIRED - {packet, number (target party id), channel}; webclient falls back to raw payload if w absent

.. rubric:: TYPE_AndruavMessage_Ctrl_Cameras — 1041

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO

Trigger still-image capture (a bounded burst, not continuous video - video streams over WebRTC). Module replies with CameraList.

**Fields:** a string REQUIRED (channel, ""=first available); b number REQUIRED (image count); c number REQUIRED (ms between shots); d OPTIONAL (not consumed); e OPTIONAL (0/1: low-res vs full-res)

.. rubric:: TYPE_AndruavMessage_CameraZoom — 1049

:Direction: WEB_TO_MODULE (intended) - DEAD/UNUSED end-to-end

Webclient sends it but drone_engage_camera_2025 does not subscribe to it - no handler.

.. rubric:: TYPE_AndruavMessage_CameraSwitch — 1050

:Direction: WEB_TO_MODULE (intended) - DEAD/UNUSED end-to-end

Webclient sends it (API_SwitchCamera) but camera module has no handler. Actual camera-switch UI goes through RemoteCommand_SWITCHCAM(114) instead, which is itself dead.

.. rubric:: TYPE_AndruavMessage_CameraFlash — 1051

:Direction: WEB_TO_MODULE (intended) - DEAD/UNUSED on this module today

Webclient sends it (legacy/mobile Andruav support) but camera module has no handler.

Geofence & Mission
==================

.. rubric:: TYPE_AndruavMessage_GeoFence — 1023

:Direction: BIDIRECTIONAL
:Rate: ON_DEMAND
:Discard: NO - a request/response pair, must be delivered

Request/response of geofence list. Web requests via RemoteExecute{C:1023}; module replies directly.

**Fields:** fn string OPTIONAL - fence-name filter; if absent, all fences of the party are sent back one by one

.. rubric:: TYPE_AndruavMessage_ExternalGeoFence — 1024

:Direction: BIDIRECTIONAL/system-mediated
:Rate: ON_DEMAND - triggered when tasks/fences are (re)loaded
:Discard: NO - must be applied to be effective, not a snapshot

Applies a fence definition pushed from storage/system ("_sys_") or saved by the web.

**Fields:** fence-definition object per CGeoFenceFactory schema; "n" string REQUIRED (fence name)

.. rubric:: TYPE_AndruavMessage_GEOFenceHit — 1025

:Direction: MODULE_TO_WEB
:Rate: MEDIUM - event-driven, can repeat while near a boundary
:Discard: YES - only the latest in/out-zone state matters

Fired whenever geofence proximity/in-zone status changes.

**Fields:** n string REQUIRED (fence name); z bool REQUIRED (in_zone); d number OPTIONAL (distance); o bool/legacy-int OPTIONAL (should_keep_outside)

.. rubric:: TYPE_AndruavMessage_GeoFenceAttachStatus — 1029

:Direction: BIDIRECTIONAL
:Rate: ON_DEMAND
:Discard: NO

Whether a fence is currently attached to the vehicle.

**Fields:** request: fn string OPTIONAL; response: n string REQUIRED (fence name), a bool REQUIRED (isAttachedToFence)

.. rubric:: TYPE_AndruavMessage_WayPoints — 1027

:Direction: MODULE_TO_WEB
:Rate: ON_DEMAND - one-shot burst of several UDP packets
:Discard: NO - losing ONE chunk corrupts the whole list (no per-chunk retransmission)

Mission waypoint list, sent as a manually-chunked burst (max 20 items/chunk, no per-chunk ack).

**Fields:** n int REQUIRED (item count); i int REQUIRED (WAYPOINT_CHUNK/LAST_CHUNK/NO_CHUNK marker); "0".."n-1" object REQUIRED per item (t,s,a,g,l,h,y,...)

.. rubric:: TYPE_AndruavMessage_UploadWayPoints — 1046

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO - loss corrupts the uploaded mission

Upload a full mission (legacy serialized text format; also carries fences). Relies on de_common's own UDP-layer chunking.

**Fields:** a string REQUIRED - serialized mission-plan text

.. rubric:: TYPE_AndruavMessage_Upload_DE_Mission — 1075

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO - loss corrupts the mission

Upload DroneEngage mission file (current format).

**Fields:** j string REQUIRED - serialized DE mission JSON; e bool OPTIONAL (erase existing fences/mission first)

.. rubric:: TYPE_AndruavMessage_Mission_Item_Sequence — 6518

:Direction: MODULE_TO_MODULE - internal only, never reaches the webclient
:Rate: ON_DEMAND - once per waypoint reached
:Discard: NO - drives mission-attached-command triggering

Fires once per mission-item transition during mission execution.

**Fields:** s string REQUIRED - event/mission-item sequence ID

Swarm
=====

.. rubric:: TYPE_AndruavMessage_FollowHim_Request — 1054

:Direction: BIDIRECTIONAL - WEB_TO_MODULE and DRONE_TO_DRONE
:Rate: ON_DEMAND
:Discard: NO - state-changing swarm membership request

Tell a drone that another drone is in its team (a follower). Can be sent from GCS or another drone; the receiver should not assume it is a follower, only forward the request to the leader.

**Fields:** a int REQUIRED for FOLLOW/CHANGE_FORMATION (follower index, -1=any); b string OPTIONAL (leader party id); c string REQUIRED (target/slave party id); d int OPTIONAL (formation id); f int REQUIRED (SWARM_FOLLOW/UNFOLLOW/CHANGE_FORMATION); h/v int OPTIONAL

.. rubric:: TYPE_AndruavMessage_FollowMe_Guided — 1055

:Direction: DEAD/UNUSED in this codebase

Intended: leader guides a follower to a destination point. Registered in de_mavlink's MESSAGE_FILTER but no handler exists. Actual leader->follower guidance flows through SWARM_MAVLINK instead.

.. rubric:: TYPE_AndruavMessage_Make_Swarm — 1056

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO

Instruct a drone to be a leader with a swarm formation. FORMATION_SERB_NO_SWARM demotes the leader.

**Fields:** a int REQUIRED (formation id); b string REQUIRED (must equal own party_id); h/v int OPTIONAL (min spacing)

.. rubric:: TYPE_AndruavMessage_SwarmReport — 1057

:Direction: DEAD/UNUSED

Defined but never constructed or parsed anywhere.

.. rubric:: TYPE_AndruavMessage_UpdateSwarm — 1058

:Direction: DRONE_TO_DRONE - follower -> leader, via comm server
:Rate: ON_DEMAND
:Discard: NO - swarm membership state change

Add or remove a slave drone in a swarm at a given index (leader resolves index conflicts).

**Fields:** a int REQUIRED (SWARM_ADD/DELETE); c string REQUIRED (leader party id); d string REQUIRED (follower party id); b (index, documented but unused)

.. rubric:: TYPE_AndruavMessage_SWARM_MAVLINK — 6503

:Direction: MODULE_TO_MODULE (DRONE_TO_DRONE)
:Rate: HIGH - periodic ~1000ms
:Discard: YES - latest leader position/attitude supersedes older ones

Leader shares its position/attitude with swarm followers (packed MAVLink GLOBAL_POSITION_INT + ATTITUDE).

Tracking & AI Recognition
=========================

.. rubric:: TYPE_AndruavMessage_TrackingTarget_ACTION — 1042

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND - only on user click/drag
:Discard: NO - a discrete user action

User selects/clears a tracking point or region on the video.

**Fields:** a int REQUIRED (0 POINT,1 REGION,2 STOP,3 PAUSE,4 ENABLE,5 QUERY_CONFIG,6/7 AI_DRIVER on/off); b/c/r/d/e float, action-dependent

.. rubric:: TYPE_AndruavMessage_TrackingTargetLocation — 1043

:Direction: MODULE_TO_MODULE - not normally relayed to the web client
:Rate: REALTIME - ~2Hz (tracker) / ~10Hz (IR camera)
:Discard: YES - latest offset supersedes older ones

Streamed tracked-target position deltas feeding DE-Pilot's autonomous camera-pointing. IR camera module reuses this same ID for unrelated hot/cold thermal point reporting.

**Fields:** tracker: t array {x,y} normalized -0.5..0.5; IR camera (same id): t array {type:"hot"|"cold", x, y, temp}

.. rubric:: TYPE_AndruavMessage_TrackingTarget_STATUS — 1044

:Direction: MODULE_TO_WEB - force-broadcast by the comm broker regardless of internal_message flag
:Rate: ON_DEMAND - state transitions only
:Discard: NO - the one tracking message the broker force-broadcasts

Tracking state transition (lost/detected/enabled/stopped/config).

**Fields:** a int REQUIRED (0 LOST,1 DETECTED,2 ENABLED,3 STOPPED,4 CONFIG); b uint8 REQUIRED (camera direction); c bool REQUIRED (ai_priority)

.. rubric:: TYPE_AndruavMessage_AI_Recognition_ACTION — 1076

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO

Select/search/enable/disable AI recognition targets, or request the class list.

**Fields:** a int REQUIRED (0 POINT[unused],1 SEARCH,2 DISABLE,3 ENABLE,4 CLASS_LIST); i array of int REQUIRED for a=1

.. rubric:: TYPE_AndruavMessage_AI_Recognition_STATUS — 1077

:Direction: MODULE_TO_WEB
:Rate: ON_DEMAND - state transitions only
:Discard: NO

AI recognition state transition, or the detectable class list.

**Fields:** a int REQUIRED (0 LOST,1 DETECTED,2 ENABLED,3 DISABLED,4 CLASS_LIST); c array of string REQUIRED only when a=4

.. rubric:: TYPE_AndruavMessage_AI_Recognition_TargetLocation — 1078

:Direction: MODULE_TO_MODULE - internal_message=true, never reaches the comm server/web
:Rate: REALTIME - essentially every inference frame
:Discard: YES - ideal candidate to drop under congestion

Best-detected-object bounding box, feeding de_tracker's AI-assisted driver.

**Fields:** b object REQUIRED {x,y,w,h} normalized; conf float OPTIONAL; t array DEBUG-ONLY (never sent in release builds)

.. rubric:: TYPE_AndruavMessage_IR_CAMERA_MI48_ACTION — 6528

:Direction: DEAD/UNIMPLEMENTED

Parser case exists but body is an empty switch ("TODO: LATER"); no sender anywhere.

.. rubric:: TYPE_AndruavMessage_IR_CAMERA_MI48_STATUS — 6529

:Direction: MODULE_TO_MODULE (intended), currently a no-op end-to-end
:Rate: ON_DEMAND (intended)

Sent on IR detection state changes, but the receiving parser case is an empty stub and nothing else parses it.

**Fields:** a int REQUIRED (reuses TrackingTarget_STATUS_* constants); b uint8 REQUIRED (camera direction)

Viewlink Gimbal Module
======================

.. rubric:: TYPE_AndruavMessage_Viewlink_ACTION — 1079

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO

Viewlink module control (laser/tracker/AI/camera/gimbal + get-status).

**Fields:** a int REQUIRED (1 LASER,2 TRACKER,3 AI,4 CAMERA,5 GIMBAL,6 GET_STATUS); b int REQUIRED for most categories; value/x/y/c/p/y depend on category

.. rubric:: TYPE_AndruavMessage_Viewlink_STATUS — 1080

:Direction: MODULE_TO_WEB
:Rate: MIXED - up to REALTIME (10Hz) for gimbal attitude, ON_DEMAND for state transitions
:Discard: depends on subtype - YES for attitude/telemetry, NO for connection/tracking/error

Viewlink status: connection/tracking/recording/error/telemetry/gimbal attitude.

**Fields:** a int REQUIRED (0 CONNECTION,1 TRACKING,2 RECORDING,3 ERROR,4 TELEMETRY,6 GIMBAL_ATTITUDE,7 ALL); fields depend on a

.. rubric:: TYPE_AndruavMessage_Viewlink_Telemetry — 1083

:Direction: MODULE_TO_WEB
:Rate: HIGH/REALTIME - ~100ms (10Hz)
:Discard: YES - latest telemetry snapshot supersedes older ones

Viewlink telemetry stream (gimbal angles, target/vehicle coords, LRF distance, AI targets). Reassigned from 1081 to 1083 in 2026 to resolve a collision with DEPilot_Control (1081 was independently reused by viewlink_module's vendored messages.py).

**Fields:** a int REQUIRED (always 4/TELEMETRY); angles/vehicle/target objects OPTIONAL; lrf_distance float OPTIONAL; ai_targets array OPTIONAL

MAVLink Relay & UDP Proxy
=========================

.. rubric:: TYPE_AndruavMessage_MAVLINK — 6502

:Direction: BIDIRECTIONAL
:Rate: HIGH, multi-rate by sub-message (position/attitude ~500ms, wind/terrain ~1000ms, power/EKF ~5000ms)
:Discard: YES for telemetry direction - NO for the web->module command subset (e.g. parameter writes)

Raw MAVLink v2 message(s), packed back-to-back (binary, no JSON "ms" payload). Carries almost all telemetry module->web; parameter writes etc. web->module.

.. rubric:: TYPE_AndruavMessage_INTERNAL_MAVLINK — 6504

:Direction: DEAD/UNUSED

Intended for other modules to exchange MAVLink info between each other; defined but no construction or parsing found anywhere.

.. rubric:: TYPE_AndruavMessage_UDPProxy_Info — 1071

:Direction: MODULE_TO_WEB - implemented in drone_engage_mavlink
:Rate: ON_DEMAND - reply to a request or after a pause/resume rate change
:Discard: YES - a status snapshot, latest value supersedes older ones

Sends information about the UDP Proxy of the unit.

**Fields:** a string REQUIRED (proxy IP); p number REQUIRED (proxy port); o number REQUIRED (optimization level); en bool REQUIRED (enabled); z bool OPTIONAL (paused)

.. rubric:: TYPE_AndruavMessage_LocalServer_ACTION — 6522

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO

Set IP/Port of the local communication server.

**Fields:** u string REQUIRED (URL/IP); p string REQUIRED (port). BUG: drone_engage_communication_pro's handler parses u/p but then calls reconnectToCommServer() with hardcoded literals - the parsed values are discarded.

.. rubric:: TYPE_AndruavMessage_LocalServer_STATUS — 6523

:Direction: DEAD/UNUSED

Only the #define exists; no construction or parsing anywhere.

.. rubric:: TYPE_AndruavMessage_LocalServer_REMOTE_EXECUTE — 6524

:Direction: DEAD/UNUSED

Meant to replace LocalServer_ACTION per a TODO comment, but never wired up.

.. rubric:: TYPE_AndruavMessage_Communication_Line_Set — 6509

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO - a link-control command

Turn communication channels (cloud websocket / local websocket) on/off.

**Fields:** ws bool OPTIONAL (cloud on/off); wsd number OPTIONAL (auto-revert seconds); w2 bool OPTIONAL (LOCAL on/off); wd2 number OPTIONAL (LOCAL auto-revert seconds). Note: documented "p2p" field is not implemented by the handler.

.. rubric:: TYPE_AndruavMessage_Communication_Line_Status — 6510

:Direction: MODULE_TO_WEB
:Rate: ON_DEMAND - fired as the line goes offline
:Discard: NO in principle, but delivery races the link going down

Reports that the comm websocket line was just turned off.

**Fields:** ws bool REQUIRED; p2p bool documented but never populated

P2P Mesh (ESP32 radio)
======================

.. rubric:: TYPE_AndruavMessage_P2P_ACTION — 6505

:Direction: BIDIRECTIONAL - WEB_TO_MODULE and MODULE_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO - a mesh state-change command

P2P mesh control (restart/connect/scan/access to a MAC).

**Fields:** a int REQUIRED (P2P_ACTION_* code); b string REQUIRED for CONNECT_TO_MAC; p string OPTIONAL (wifi password); c int OPTIONAL (channel)

.. rubric:: TYPE_AndruavMessage_P2P_STATUS — 6506

:Direction: DEAD/UNUSED

Both p2p and mavlink modules validate/parse this defensively but nothing ever constructs/sends it.

.. rubric:: TYPE_AndruavMessage_P2P_InRange_BSSID — 6507

:Direction: MODULE_TO_WEB
:Rate: MEDIUM - ~10s or immediate on change
:Discard: YES - a scan snapshot, latest results supersede older ones

Detected mesh access points (BSSIDs) near this unit.

**Fields:** keyed by party_id; per entry: b bssid, p party id, s ssid, c channel, r rssi, t usec since last seen

.. rubric:: TYPE_AndruavMessage_P2P_InRange_Node — 6508

:Direction: MODULE_TO_WEB
:Rate: MEDIUM - ~10s
:Discard: YES - a scan snapshot, latest results supersede older ones

Detected mesh peer nodes/pings near this unit.

**Fields:** keyed by party_id; per entry: m mac, p party id, c connected, t usec since last action

.. rubric:: TYPE_AndruavMessage_P2P_INFO — 6517

:Direction: MODULE_TO_WEB
:Rate: MEDIUM - ~10s
:Discard: YES - a status snapshot, latest value wins

Own P2P mesh connection status of this unit.

**Fields:** c connection type; a1/a2 own/AP address; wc wifi channel; wp wifi password; pa parent node address; pc parent connected; f firmware version; lp expected parent mac; a/o/d driver/p2p connected/disabled

.. rubric:: TYPE_AndruavMessage_Ping_Unit — 1073

:Direction: DRONE_TO_DRONE - P2P mesh only
:Rate: ON_DEMAND
:Discard: YES - a liveness probe, occasional loss is tolerable

Ping a unit to verify P2P mesh presence, or request/reply like TYPE_AndruavMessage_ID.

**Fields:** a string (sender party id, ping use); k 1=request ack (ID-like use)

SDR (Software Defined Radio)
============================

.. rubric:: TYPE_AndruavMessage_SDR_ACTION — 6514

:Direction: BIDIRECTIONAL
:Rate: ON_DEMAND per command/reply; TRIGGER is event-driven
:Discard: NO - configuration/commands and trigger alerts must be delivered

Generic SDR module message: connect/disconnect/set-config/read-data/pause-data (web->module) and SDR_INFO reply/device-list reply/trigger alert (module->web).

**Fields:** a int REQUIRED (SDR_ACTION_*); fc/g/r/i/t/l depend on action. Fixed 2026: field "t" (streaming interval, ms) was previously mis-consumed as whole seconds (1e9 instead of 1e6), making 1000ms wait ~16.7 minutes.

.. rubric:: TYPE_AndruavMessage_SDR_REMOTE_EXECUTE — 6515

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO

Request SDR info or device list (wraps a sub-action inside SDR_ACTION's namespace).

**Fields:** C int REQUIRED (always TYPE_AndruavMessage_SDR_ACTION); a int REQUIRED (SDR_ACTION_SDR_INFO or LIST_SDR_DEVICES)

.. rubric:: TYPE_AndruavMessage_SDR_SPECTRUM — 6516

:Direction: MODULE_TO_WEB
:Rate: REALTIME - continuous while active, interval = SDR_ACTION's "t" field
:Discard: YES - the definitive keep-latest message in the SDR module

Streamed FFT spectrum bars (binary: JSON header + float32 array).

**Fields:** fcm double REQUIRED (min frequency); fcst float REQUIRED (frequency step); tim uint64 REQUIRED; binary attachment REQUIRED (raw float array)

GPIO
====

.. rubric:: TYPE_AndruavMessage_GPIO_ACTION — 6519

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO - a hardware-control command

Configure or write a GPIO pin.

**Fields:** i string OPTIONAL (target module_key); a int REQUIRED (PORT_CONFIG/PORT_WRITE, PORT_READ unimplemented); CONFIG: p pin, m mode, v/n OPTIONAL; WRITE: v REQUIRED, n/p lookup, d REQUIRED in PWM mode

.. rubric:: TYPE_AndruavMessage_GPIO_STATUS — 6520

:Direction: MODULE_TO_WEB
:Rate: MEDIUM/LOW - internal tick 1000ms, sent to GCS every 10s, plus on-change
:Discard: YES for the periodic snapshot - on-change updates worth keeping but recoverable

GPIO pin status (full snapshot or a single targeted pin).

**Fields:** a int REQUIRED (always GPIO_ACTION_INFO); s array REQUIRED, each {i,p/b,m,t,d(if PWM),v,n(optional)}

.. rubric:: TYPE_AndruavMessage_GPIO_REMOTE_EXECUTE — 6521

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO

Request current GPIO status (full or a specific pin).

**Fields:** a int REQUIRED (only GPIO_STATUS request handled); p int OPTIONAL (specific pin); i string OPTIONAL (module_key)

Sound / TTS
===========

.. rubric:: TYPE_AndruavMessage_SOUND_TEXT_TO_SPEECH — 6511

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO

Text-to-speech request.

**Fields:** t string REQUIRED (text); l string OPTIONAL (language); p/v OPTIONAL (pitch/volume)

.. rubric:: TYPE_AndruavMessage_SOUND_PLAY_FILE — 6512

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO

Play a sound file.

**Fields:** f string REQUIRED (file path)

.. rubric:: TYPE_AndruavMessage_SOUND_LIST — 6530

:Direction: MODULE_TO_WEB
:Rate: ON_DEMAND - startup, after config apply, or on request
:Discard: NO - low frequency, not a candidate for dropping

Sound library list (available TTS/sound files).

**Fields:** T array REQUIRED, each {n name, f file_path}; R bool REQUIRED (true when replying to a request)

Telnet / Remote Terminal
========================

.. rubric:: TYPE_AndruavMessage_TELNET_ACTION — 6531

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND - one-shot per user action
:Discard: NO - dropping "close" leaks a pty, dropping "open" silently fails a user action

Open/close/list/resize a remote shell session on a unit. The de_telnet module owns the pty lifecycle.

**Fields:** a int REQUIRED (TELNET_ACTION_*); i string REQUIRED for CLOSE/RESIZE; sh string OPTIONAL (OPEN); c/r int OPTIONAL default 80/24 (RESIZE)

.. rubric:: TYPE_AndruavMessage_TELNET_STATUS — 6532

:Direction: MODULE_TO_WEB
:Rate: ON_DEMAND - one-shot per lifecycle transition
:Discard: NO - a lifecycle transition, must be delivered

Telnet session lifecycle status (opened/closed/list/error/resized).

**Fields:** a int REQUIRED (TELNET_STATUS_*); i string (session_id); e string OPTIONAL (error); ec int (exit code); c/r int (cols/rows); l array (session list)

.. rubric:: TYPE_AndruavMessage_TELNET_DATA — 6533

:Direction: BIDIRECTIONAL
:Rate: REALTIME - continuous while a session is open
:Discard: NO - unlike telemetry, each message carries unique unrepeatable terminal bytes; do NOT keep-latest-only this

Raw terminal I/O byte stream: keystrokes (web->module) and pty output (module->web).

**Fields:** i string REQUIRED (session_id); a int (output direction only, TELNET_STATUS_DATA); input as binary attachment (preferred) or d string (fallback)

.. rubric:: TYPE_AndruavMessage_TELNET_REMOTE_EXECUTE — 6534

:Direction: DEAD/UNUSED

Defined for possible future use; de_telnet's handler is an explicit no-op stub.

Configuration Management
========================

.. rubric:: TYPE_AndruavMessage_CONFIG_ACTION — 6525

:Direction: WEB_TO_MODULE - handled generically by every C++ module via de_common
:Rate: ON_DEMAND
:Discard: NO - a config-management command

Restart/apply-config/fetch-template/fetch-config/shutdown/restart-hw.

**Fields:** a int REQUIRED (CONFIG_ACTION_*); b string OPTIONAL (target module_key, ignored if mismatched); c object REQUIRED only for APPLY_CONFIG

.. rubric:: TYPE_AndruavMessage_CONFIG_STATUS — 6526

:Direction: MODULE_TO_WEB
:Rate: ON_DEMAND - reply to a fetch request
:Discard: NO - config content must arrive intact, not a state snapshot

Reply carrying a module's config template or current config JSON.

**Fields:** a int REQUIRED (FETCH_CONFIG_TEMPLATE/FETCH_CONFIG); b object REQUIRED (template/config JSON); k string REQUIRED (module_key); R bool REQUIRED

.. rubric:: TYPE_AndruavMessage_MAVLINK_EVENTS — 6527

:Direction: DEAD/UNUSED

Defined but never constructed or parsed anywhere, not even in the webclient parser.

Chat, Sync & Misc
=================

.. rubric:: TYPE_AndruavMessage_Sync_EventFire — 1061

:Direction: BIDIRECTIONAL - WEB_TO_MODULE, MODULE_TO_MODULE, and DRONE_TO_DRONE rebroadcast
:Rate: ON_DEMAND - event-driven (mission item triggers, GCS UI action)
:Discard: NO - an event trigger, dropping it means a mission/sync event never fires

Fire a droneengage sync/mission event.

**Fields:** d string REQUIRED (event id); m object OPTIONAL (event payload). Also carries c/s (sender module class/id) per some callers.

.. rubric:: TYPE_AndruavMessage_SearchTargetList — 1062

:Direction: DEAD/UNUSED (experimental, disabled)

Webclient has request/response code for it but both are gated behind CONST_EXPERIMENTAL_FEATURES_ENABLED=false, and no module answers it.

.. rubric:: TYPE_AndruavMessage_Unit_Name — 1072

:Direction: WEB_TO_MODULE
:Rate: ON_DEMAND
:Discard: NO - a rename command

Set unit name and description.

**Fields:** UN string REQUIRED (unit name); DS string REQUIRED (description); PR bool OPTIONAL (reset party_id flag)

.. rubric:: TYPE_AndruavMessage_Prepherials — 1070

:Direction: DEAD/UNUSED

andruav_facade.cpp::API_sendPrepherals() is fully implemented but explicitly commented "NOT USED" and never called.

.. rubric:: TYPE_AndruavMessage_LightTelemetry — 2022

:Direction: DEAD/UNUSED

Deprecated telemetry technology; no sender found. Superseded by TYPE_AndruavMessage_MAVLINK + UDP proxy.

.. rubric:: TYPE_AndruavMessage_SensorsStatus — 1053

:Direction: DEAD/UNUSED

Defined but never constructed or parsed anywhere.

.. rubric:: TYPE_AndruavMessage_ConfigCOM — 1038

:Direction: DEAD/UNUSED

Only a #define, no construction or parsing found anywhere (C++ or JS).

.. rubric:: TYPE_AndruavMessage_ConfigFCB — 1039

:Direction: DEAD/UNUSED

Same situation as ConfigCOM - only a #define, no builder or parser found in mavlink, communication_pro, or webclient.

.. rubric:: TYPE_AndruavMessage_DUMMY — 9999

:Direction: DEAD/UNUSED in production traffic

Test/debug only - used by de_databus client library examples to smoke-test the message bus.

System / Connection-Layer Messages (9001-9009)
==============================================

.. rubric:: TYPE_AndruavSystem_LoadTasks — 9001

:Direction: BIDIRECTIONAL
:Rate: ON_DEMAND - on connect / task-management UI action
:Discard: NO - a data-management request, not a snapshot

Load saved tasks/mission-and-fence set. Dual purpose: a top-level System WS command (web<->storage server) AND a reused inter-module RemoteExecute "C" action code.

.. rubric:: TYPE_AndruavSystem_SaveTasks — 9002

:Direction: WEB_TO_MODULE-equivalent (web -> comm/storage server)
:Rate: ON_DEMAND
:Discard: NO

Save tasks (fences/missions) to storage.

.. rubric:: TYPE_AndruavSystem_DeleteTasks — 9003

:Direction: WEB_TO_MODULE-equivalent
:Rate: ON_DEMAND
:Discard: NO

Delete saved tasks.

.. rubric:: TYPE_AndruavSystem_DisableTasks — 9004

:Direction: WEB_TO_MODULE-equivalent
:Rate: ON_DEMAND
:Discard: NO

Disable saved tasks.

.. rubric:: TYPE_AndruavSystem_Ping — 9005

:Direction: MODULE_TO_MODULE - module <-> cloud comm server link keepalive
:Rate: LOW - floor ~10s
:Discard: YES - a heartbeat, a dropped ping is recovered by the next one

Connection-layer heartbeat/keepalive, not part of the web UI protocol.

**Fields:** t number REQUIRED (timestamp usec)

.. rubric:: TYPE_AndruavSystem_LogoutCommServer — 9006

:Direction: BIDIRECTIONAL
:Rate: ON_DEMAND
:Discard: NO - connection state, must be delivered

Deregister from the comm server (logout/disconnect).

.. rubric:: TYPE_AndruavSystem_ConnectedCommServer — 9007

:Direction: MODULE_TO_MODULE-equivalent (comm server -> connecting module/web)
:Rate: ON_DEMAND - once per handshake
:Discard: NO - connection state

Comm server's registration acknowledgment.

.. rubric:: TYPE_AndruavSystem_UDPProxy — 9008

:Direction: MODULE_TO_MODULE (mavlink <-> comm server)
:Rate: ON_DEMAND
:Discard: NO - a one-time setup handshake

Request/confirm UDP proxy telemetry sockets.

**Fields:** en bool REQUIRED; socket1/socket2 object REQUIRED, each {address, port}

.. rubric:: TYPE_AndruavSystem_LocalServer — 9009

:Direction: DEAD/UNUSED

Only appears in de_databus/nodejs/messages.js; not to be confused with the actively-used LocalServer_ACTION/STATUS (6522-6524).

Constants Reference (Selected)
================================

Compact reference for enum-style constants referenced by the fields
above. Not exhaustive - see ``messages.hpp`` for the complete list.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Group
     - Values
   * - GCS Permissions (bitmask, field ```p```)
     - ALLOW_GCS=0x1, ALLOW_UNIT=0x10, ALLOW_GCS_WP_CONTROL=0x100, ALLOW_GCS_MODES_CONTROL=0x200, ALLOW_GCS_MODES_SERVOS=0x400, ALLOW_GCS_FULL_CONTROL=0xf00, ALLOW_GCS_VIDEO=0xf000, ALLOW_SWARM=0xf0000
   * - Notification/Error Severity
     - EMERGENCY=0, ALERT=1, CRITICAL=2, ERROR=3, WARNING=4, NOTICE=5, INFO=6, DEBUG=7 (mirrors MAV_SEVERITY_*)
   * - GPS Mode
     - AUTO=0, EXTERNAL=1 (mobile/non-board GPS), FCB=2
   * - Waypoint Chunk Markers
     - NO_CHUNK=0, CHUNK=1, LAST_CHUNK=999
   * - Fence Actions
     - SOFT=0, RTL=2, LAND=12, LOITER=10, BRAKE=17, SMART_RTL=21
   * - Swarm Actions
     - UpdateSwarm: ADD=1, DELETE=2. FollowHim_Request: FOLLOW=1, UNFOLLOW=2, CHANGE_FORMATION=3
   * - Swarm Formation (TASHKEEL_SERB_*)
     - NO_SWARM=0, THREAD=1, VECTOR=2, VECTOR_180=3
   * - DistinationLocation Type
     - GUIDED_POINT=0, SWARM_MY_LOCATION=1
   * - Reserved Special Names
     - _any_, _generic_ (all receivers), _drone_ (vehicle receivers), _gcs_ (GCS receivers)
   * - Tracking Camera Direction
     - NONE=0, FRONT=1, BACK=2, DOWN=3, UP=4
   * - Custom/User Message IDs
     - 80000-90000 (``TYPE_AndruavMessage_USER_RANGE_START/END``) reserved for project-specific extensions, outside the ranges used above
   * - Reserved but unimplemented
     - A commented-out ``Sonar_Info/Action/RemoteExecute`` block (13001-13003) exists in the header as a placeholder for a future sonar module - not a real message type today

See Also
=========

- :doc:`Andruav Communication Protocol <de-dev-andruav-communication-protocol>` - the envelope/header structure (sender, target, message type, payload) that carries these message types.
- :doc:`DataBus (Inter-Module Communication) <de-dev-databus>` - how modules exchange these messages internally via de_common.
- `messages.hpp on GitHub <https://github.com/DroneEngage/droneengage_communication/blob/master/src/messages.hpp>`_ - the source of truth this page is generated from.
