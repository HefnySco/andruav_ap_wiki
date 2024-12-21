.. _de-dev-andruav-communication-protocol-messages:


=====================
Andruav Messages Type
=====================


.. warning::
    Messages ID under constant updates. Latest version in code should be `here <https://github.com/DroneEngage/droneengage_communication/blob/master/src/messages.hpp>`_.


TYPE_AndruavMessage_GPS                     1002

TYPE_AndruavMessage_POWER                   1003

TYPE_AndruavMessage_ID 	                    1004

TYPE_AndruavMessage_RemoteExecute 		    1005

TYPE_AndruavMessage_IMG                     1006

TYPE_AndruavMessage_Error                   1008    

TYPE_AndruavMessage_FlightControl           1010

TYPE_AndruavMessage_CameraList 			    1012  

TYPE_AndruavMessage_DroneReport             1020

TYPE_AndruavMessage_Signaling               1021

TYPE_AndruavMessage_HomeLocation            1022

TYPE_AndruavMessage_GeoFence                1023

TYPE_AndruavMessage_ExternalGeoFence        1024

TYPE_AndruavMessage_WayPoints               1027

TYPE_AndruavMessage_GeoFenceAttachStatus    1029

TYPE_AndruavMessage_Arm                     1030

TYPE_AndruavMessage_ChangeAltitude          1031

TYPE_AndruavMessage_Land                    1032

TYPE_AndruavMessage_GuidedPoint             1033

TYPE_AndruavMessage_CirclePoint             1034

TYPE_AndruavMessage_DoYAW                   1035

TYPE_AndruavMessage_NAV_INFO                1036

TYPE_AndruavMessage_DistinationLocation     1037

TYPE_AndruavMessage_ConfigCOM               1038

TYPE_AndruavMessage_ConfigFCB               1039

TYPE_AndruavMessage_ChangeSpeed             1040

TYPE_AndruavMessage_Ctrl_Cameras            1041

TYPE_AndruavMessage_TrackingTarget          1042

TYPE_AndruavMessage_TargetLoackedAt         1043

TYPE_AndruavMessage_TargetLost              1044

TYPE_AndruavMessage_UploadWayPoints         1046

TYPE_AndruavMessage_RemoteControlSettings	1047

TYPE_AndruavMessage_SET_HOME_LOCATION       1048

TYPE_AndruavMessage_CameraFlash		        1051

TYPE_AndruavMessage_RemoteControl2		    1052

TYPE_AndruavMessage_FollowHim_Request       1054

TYPE_AndruavMessage_FollowMe_Guided         1055

TYPE_AndruavMessage_MAKE_SWARM              1056

TYPE_AndruavMessage_UpdateSwarm             1058

TYPE_AndruavMessage_Sync_EventFire          1061

TYPE_AndruavMessage_Prepherials             1070

TYPE_AndruavMessage_UDPProxy_Info           1071

TYPE_AndruavMessage_Unit_Name               1072

TYPE_AndruavMessage_Ping_Unit                   1073

TYPE_AndruavMessage_Upload_DE_Mission           1075

TYPE_AndruavMessage_LightTelemetry              2022

TYPE_AndruavMessage_ServoChannel                6001

TYPE_AndruavMessage_MAVLINK                     6502

TYPE_AndruavMessage_SWARM_MAVLINK               6503

TYPE_AndruavMessage_INTERNAL_MAVLINK            6504

TYPE_AndruavMessage_P2P_ACTION                  6505

TYPE_AndruavMessage_P2P_STATUS                  6506

TYPE_AndruavMessage_P2P_InRange_BSSID           6507

TYPE_AndruavMessage_P2P_InRange_Node            6508

TYPE_AndruavMessage_Communication_Line_Set          6509

TYPE_AndruavMessage_Communication_Line_Status       6510

TYPE_AndruavMessage_SOUND_TEXT_TO_SPEECH            6511

TYPE_AndruavMessage_SOUND_PLAY_FILE                 6512

TYPE_AndruavMessage_SDR_INFO                        6513

TYPE_AndruavMessage_SDR_ACTION                      6514

TYPE_AndruavMessage_SDR_STATUS                      6515

TYPE_AndruavMessage_SDR_SPECTRUM                    6516

TYPE_AndruavMessage_P2P_INFO                        6517

TYPE_AndruavMessage_Mission_Item_Sequence           6518

TYPE_AndruavMessage_DUMMY                           9999
