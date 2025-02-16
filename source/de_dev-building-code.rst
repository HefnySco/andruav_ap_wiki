.. _de_dev-building-code:

=========================
Building DroneEngage Code
=========================


If you want to build binaries form sourcecode in order to make it compatible with your linux platform you need to follow the following steps.
In this scenario we will use RPI-4 with Bullseye image. However you can use any version, or you can even compile it using the same steps on your linux laptop or VM.



Preparing prerequisites 
-----------------------

.. code-block:: bash

   ssh pi@raspberrypi.local
   
   cd ~

   sudo apt update
   sudo apt install git
   sudo apt install cmake
   sudo apt-get install libcurl4-openssl-dev
   sudo apt-get install libssl-dev


    cd ~
    mkdir boost
    cd boost
    get https://archives.boost.io/release/1.86.0/source/boost_1_86_0.tar.bz2
    tar -xvjf boost_1_86_0.tar.bz2
    cd boost_1_86_0
    ./bootstrap.sh
    ./b2
    sudo ./b2 install

|

Compiling boost library on RPI will take a long time.
Now you have everything ready.


Downloading Code
----------------

.. code-block:: bash

   mkdir de_code
   cd de_code
   git clone https://github.com/DroneEngage/droneengage_communication.git
   git clone https://github.com/DroneEngage/droneengage_mavlink.git  

|


Compiling Code
----------------

.. code-block:: bash

    cd ~/droneengage_communication
    ./build.sh
|

.. code-block:: bash

    cd ~/droneengage_mavlink
    ./build.sh
|


Output binaries will be in ./bin




