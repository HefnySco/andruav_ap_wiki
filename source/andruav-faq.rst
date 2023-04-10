.. _andruav-faq:



===========
Andruav FAQ
===========



#. I Do Not Understand Many Terminologies in This Site and Andruav App.
    Please access glossary page.

#. Why Does Andruav App Request Alot of Permissions ?
    Andruav is a complicated application, it accesses control boards via bluetooth, and USB & Wifi. Also access sensors such as GPS, compass, camera ... etc. Andruav communicates with server over Internet & 3G/4G when available. All of these actions require permissions for an Android application to execute.

#. I Cannot Get my Accesscode.
    The first time you register in Andruav, you should set Andruav in GCS mode. Then it will go to registration screen where you can enter your email and press Register. An access code will be created and placed in the accesscode box. Also, it will be sent to you via email -it might appears in the spam section-. You can create sub-AccessCodes with limited permissions from web. Please check  :ref:`andruav-getting-started` for more details.

#. Where Does Andruav store images and Videos on my Mobile ?
    There is a folder in te mobile called AndruavKML these folders contains sub-folders for each and every flight. Each subfolder contains:
    #. A KML file of the flight path, and images are displayed over it. The file can be browsed using Google Earth app.
    #. A Folder if all images that are taken during that flight. Images are stored as jpg and are geo tagged. The flight folder can be copied to your laptop and then click on KML file, Google Earth will display the path, and the images will appear on the map as well.

#. How Many Drones and GCS Can be connected simultanously ?
    Theoretically unlimited. It depends on your network quality and type of data you transfer, it also depends on your Drone devices. For high response time you need to use better Andruav-Drone quality devices.

#. What is group and why it is 1?
    Andruav Group refers to group of drones & GCS that interact with each other. An Andruav account can have multiple groups. Different groups cannot be interacted with each other. By default, this feature is disabled in Andruav, you can enable it from the "Settings Menu", and by default you have one group and its number is "1".

#. What is Web-Plugin
    Web Plugin is a small appplication that can run on Windows or Ubuntu. It allows you to connect Andruav WebClient to Mission Planner, QGround Control or any GCS without the need to use Andruav GCS mobile app. You can use Telemetry directly from Web. Please check :ref:`webclient-web-plugin` for more details.

#. Smart Telemetry Levels
    Smart Telemetry is a feature in Andruav that enables it to use less bandwidth when sending telemetry data. This is useful for your data subscription package. It enables you to get good performance with slower networks. Different levels means lesser packets being sent and some non important packets are being almost filtered. The high the level the less the bandwidth and connection speed required as well as the less screen update on GCS.

#. Can I connect USB Camera to Andruav Mobile App ?
    You can use built-iin mobile cameras including zoom and flash. External cameras are not supported yet.