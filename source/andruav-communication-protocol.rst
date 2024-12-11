.. _andruav-communication-protocol:



==============================
Andruav Communication Protocol
==============================

Andruav Communication Protocol is the protocol that is used to communicate between units and server, and between units modules.

Protocol is a text JSON message header. Payload can be text or binary, but header is always JSON text. The protocol is very flexible and can be even carry embedded mavlink messages or any other message protocol as a payload.

Please note that this is not a serial protocol, so 

Protocol Header Fields 
======================


sender:
-------
This is the sender unique-id called party-id. It uniquely identifies the unit in the system.


target:
-------
This is the party-id of the receiver. If the message should be received by group of receivers
then target can be:

#. '_AGN_': all units in the system. i.e. units under the same account and group.

#. '_GCS_': all GCS in the system. i.e. units under the same account and group.

#. '_GD_' all GCS & units.


There is also a special sender/target called '_SYS_', and this is the messages that is created or handled by Andruav-Communicator-Server.

if target is not existed then this is a global message. It is up to server-communicator logic how to handle this.

see: `js_andruav_chat_server.js function fn_parseMessage <https://github.com/DroneEngage/droneengage_server/blob/9f8527be7806771cd4b15f2c2b56ad32ae77c98c/server/js_andruav_chat_server.js#L199/>`_ 



message type:
-------------

field: mt

This is a numeric field that defines the message itself.

see :ref:`andruav-communication-protocol-messages`




Protocol Payload Fields 
=======================

message command:
----------------

field: ms

This field holds the text payload of the message. It is a JSON string with fields based one message_type.
The fields ends with null and then starts binary payload of the message if exists.

see: `js_andruav_chat_server.js function fn_parseMessage <https://github.com/DroneEngage/droneengage_server/blob/9f8527be7806771cd4b15f2c2b56ad32ae77c98c/server/js_andruav_chat_server.js#L199/>`_ 



binary command:
---------------

Binary command is optional based on the message type. The binary data is concatenated after the text content of the message header. 
A binary message can contain also message command in text format. Binary content length is defined by subtracting total message length from the text content that is terminated
by a null character.



