.. _srv-install-airgap:

=======================================
Air-Gap RPI-4 Backend-Server Deployment
=======================================



.. youtube:: R1BedRTxuuY

    
script is available at: `prepare-airgapped-server.sh <https://raw.githubusercontent.com/HefnySco/andruav_droneengane_scripts/main/server_installation/prepare-airgapped-server.sh>`_



Prerequisits
============

1- Computer with `Ubuntu OS <https://ubuntu.com/>`_, or you can use `RPI-4 with Raspberry OS <https://www.raspberrypi.com/software/>`_. I recommend using aarch64 version. The computer should have a statis IP. The scripts assumes 192.168.1.161 put you can change this IP to any local IP you want. In case of RPI-4 you do not need to install the Desktop version. You only need to inslall the server with ssh enabled.

2- Computer should have a static local IP i.e. 192.xxx.xxx.xxx e.g.: 192.168.1.161

3- It is recommended to `boot RPI-4 from a USB-3 flash memory <https://www.tomshardware.com/how-to/boot-raspberry-pi-4-usb>`_  to get advantage of higher throughtput speed.




`Raspberry PI Imager <https://www.raspberrypi.com/software/>`_  easily enables you to setup your Raspberry.


.. youtube:: ntaXWS8Lk34



|

.. important::
    Make sure that the IP in the script matches the IP of your computer. simpley edit IP field in the script. You cannot use DHCP address with this machine.



Installation
============

Enter to your Raspberry-PI using ssh or open a terminal on your Ubuntu server.


**Download Script**

.. code-block::

    cd ~
    wget https://raw.githubusercontent.com/HefnySco/andruav_droneengane_scripts/main/server_installation/prepare-airgapped-server.sh

This command will download script `prepare-airgapped-server.sh <https://raw.githubusercontent.com/HefnySco/andruav_droneengane_scripts/main/server_installation/prepare-airgapped-server.sh>`_

You can open this script for editing to change domain name of ip address as below.


**Edit Script if needed**

You can choose the local domain name. Write any local -fake- domain name you want.
The IP address must be equal to the local static IP of the machine.

.. code-block:: bash

    DOMAIN_NAME='airgap.droneengage.com'
    IP='192.168.1.161' 


**Execute Script**

.. code-block:: bash

    sudo chmod a+x ./prepare-airgapped-server.sh
    sudo ./prepare-airgapped-server.sh


When the script finishs successfully the following will be created:

    #. a folder **~/ssl** with three files - we will see this later in :ref:`access local domain`-:

        * localssl.key
        * localssl.crt
        * root.crt
        
    #. dnsmasq a DNS server that is up running and configured in /etc/dnsmasq.conf

    #. a folder **~/droneengage_authenticator** contains `droneengage_authenticator <https://github.com/DroneEngage/droneenage_authenticator.git>`_ 

    #. a folder **~/droneengage_server** contains `droneengage_server <https://github.com/DroneEngage/droneengage_server.git>`_ 

    #. a folder **~/droneengage_webclient** contains `droneengage_webclient <https://github.com/DroneEngage/droneengage_webclient.git>`_ 

    #. a folder **~/map/cachedMap** that is empty. This folder can be filled with cached images to be used as a local map server.
        
**Your Raspberry PI-4 now is fully ready**

Access Local Domain
===================

You need two extra steps to access this local domain from your local wifi network.

#. **Use DNS on your Gateway**
    
    **dnsmasq** is  running on your RPI-4 now. you need to add its IP "192.168.1.161" or whatever IP you chave choosen as one of the DNS servers on your gateway.
    or you can add it in the phone DNS connection directly.



#. **Register CA Root**

    When the script finishs successfully the following will be created:

        a folder **~/ssl** with three files:

            * localssl.key
            * localssl.crt
            * root.crt

    you need to copy root.crt into any browser of mobile device that is part of this system.
    This is a root certificate that is used to tell those devices that localssl.crt is trusted and hence the conection will be secure and accepted. 

    The below images shows `how to do that on Chrome <https://support.google.com/chrome/a/answer/6342302?hl=en>`_ .

    .. image:: ./images/srv_certificate1.png
        :height: 400px
        :align: center
        :alt: register root certificate in Authorities section in Chrome.


    |

    .. image:: ./images/srv_certificate2.png
        :height: 400px
        :align: center
        :alt: register root certificate in Authorities section in Chrome.

    |

    Similar procedures need to be done on `Android phones <https://support.google.com/pixelphone/answer/2844832?hl=en>`_ to be able to connect Andruav.

    .. important::

        The above **ssl** is used when you want an local trusted ssl certificate. If you want your server to be exposed to Internet you can create a truely valid
        ssl certificate from a trusted provider. And you need to have **a static IP address** not a local one.







