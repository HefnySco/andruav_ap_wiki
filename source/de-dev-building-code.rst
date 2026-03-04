.. _de-dev-building-code:

=========================
Building DroneEngage Code
=========================

If you want to build binaries form sourcecode in order to make it compatible with your linux platform you need to follow the following steps.
In this scenario we will use RPI-4 with Bullseye image. However you can use any version including RPI-5 and Bookworm, or you can even compile it using the same steps on your linux laptop or VM.



Preparing prerequisites 
-----------------------

The following steps assume that you know how to install a raspberry-pi and have a raspberry-pi board up and running and accessible using SSH.

.. code-block:: bash

   ssh pi@raspberrypi.local
   
   cd ~

   sudo apt update
   sudo apt install git
   sudo apt install cmake
   sudo apt-get install libcurl4-openssl-dev
   sudo apt-get install libssl-dev
   sudo apt-get install libboost-all-dev

|

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

Both projects use CMake with automated version management and support for DEBUG and RELEASE builds.

**Building droneengage_communication:**

.. code-block:: bash

    cd ~/de_code/droneengage_communication
    
    # For DEBUG build (default)
    ./build.sh
    
    # For RELEASE build (optimized, increments version)
    ./build.sh RELEASE
    
    # With additional debug options
    ./build.sh DEBUG DDEBUG=ON

|

**Building droneengage_mavlink:**

.. code-block:: bash

    cd ~/de_code/droneengage_mavlink
    
    # For DEBUG build (default)
    ./build.sh
    
    # For RELEASE build (optimized, increments version)
    ./build.sh RELEASE
    
    # With additional debug options
    ./build.sh DEBUG DDEBUG=ON

|

**Build Script Options:**

- **DEBUG**: Default build type with debug symbols (-g3, -Og)
- **RELEASE**: Optimized build (-O2) with version increment
- **DDEBUG=ON**: Enable detailed debug output
- Additional compiler flags can be passed as parameters

**Version Management:**

Both projects use automatic version management:
- Format: MAJOR.MINOR.BUGFIX.BUILD
- BUILD number auto-increments on RELEASE builds
- Version files stored in `.version` in project root
- Current versions:
  - droneengage_communication: 3.10.1.x
  - droneengage_mavlink: 5.6.8.x

Output binaries will be in ./bin


Generating Debian Packages (Optional)
------------------------------------

Both projects support generating Debian (.deb) packages for easier installation and distribution.

**Generate Debian packages:**

.. code-block:: bash

    # For droneengage_communication
    cd ~/de_code/droneengage_communication/build
    cpack -G DEB
    
    # For droneengage_mavlink  
    cd ~/de_code/droneengage_mavlink/build
    cpack -G DEB

|

**Install generated packages:**

.. code-block:: bash

    # Install communication package
    sudo dpkg -i de-communicator-pro-*.deb
    
    # Install mavlink package
    sudo dpkg -i de-mavlink-plugin-*.deb

|

**Package Information:**

- **droneengage_communication**: Installs to `$HOME/drone_engage/de_comm/`
  - Binary: `de_ardupilot` 
  - Config files: `de_comm.config.module.json`, `root.crt`, `template.json`
  - Scripts directory included
  
- **droneengage_mavlink**: Installs to `$HOME/drone_engage/de_mavlink/`
  - Binary: `de_ardupilot`
  - Config files: `de_mavlink.config.module.json`, `template.json`

Both packages include dependency information and will automatically install required system libraries if available.
