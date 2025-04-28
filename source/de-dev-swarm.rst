.. _de-dev-swarm:


=================
DroneEngage SWARM
=================


The following diagram shows the main logic of SWARMS in DroneEngage.

|
.. image:: ./images/swarm_1_uml.png
   :align: center
   :alt: SWARM Logic

|


Unit-1 is a DroneEngage unit that should be a leader of the swarm. Unit-2 is a DroneEngage unit that should be a follower of the swarm.

Transition to Leader
-----------------

The process for establishing Unit-1 as the leader is as follows:

 - User clicks on SWARM Leader button to make Unit-1 a leader of the swarm.
 - WebClient Sends AndruavMessage_Make_Swarm Message to Unit-1.
 - Unit-1 receives the message and starts the SWARM Leader mode.
 - Unit-1 sends an updated AndruavMessage_ID to confirm that it is a leader.


Transition to Follower
-------------------

The process for establishing Unit-2 as a follower is as follows:

 - The user selects Unit-1 as the leader for Unit-2.
 - The WebClient sends an AndruavMessage_Join_Swarm message to Unit-2.
 - Unit-2 receives the message and performs necessary validations, including disassociating from any previous leader, before sending a request to Unit-1 to join the SWARM.
 - Unit-1 receives the request and determines the appropriate location (index) for Unit-2 within the current swarm configuration.
 - Unit-1 responds to Unit-2 with the relevant configuration details (formation shape and location within the formation).
 - Unit-2 receives the configuration reply and, if accepted, sends a confirmation back to Unit-1.
 - Unit-2 then sends an updated AndruavMessage_ID to confirm its status as a follower.



