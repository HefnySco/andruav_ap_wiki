.. _de-dev-mavlink-sdk-building:

====================
Building the SDK
====================

This section covers building the MAVLink SDK from source.

Prerequisites
-------------

Before building the SDK, ensure you have the following installed:

- **C++17** compatible compiler (GCC 7+ or Clang 5+)
- **CMake** 3.1.0 or higher
- **MAVLink C library** (c_library_v2)

On Ubuntu/Debian systems, install the build tools:

.. code-block:: bash

   sudo apt update
   sudo apt install build-essential cmake

MAVLink C Library
-----------------

The SDK requires the MAVLink C library (c_library_v2). It should be placed at ``../c_library_v2`` relative to the SDK directory.

Download the MAVLink C library:

.. code-block:: bash

   # Navigate to the parent directory of mavlink_sdk
   cd path/to/droneengage_mavlink
   
   # Clone the MAVLink C library
   git clone https://github.com/mavlink/c_library_v2.git

This should create the following structure::

    droneengage_mavlink/
    ├── c_library_v2/              # MAVLink C library
    └── mavlink_sdk/               # MAVLink SDK
        ├── src/
        ├── CMakeLists.txt
        └── build.sh

Building the SDK
----------------

Using the Build Script
~~~~~~~~~~~~~~~~~~~~~~

The SDK includes a convenient build script:

.. code-block:: bash

   cd mavlink_sdk
   ./build.sh

Manual Build
~~~~~~~~~~~~

If you prefer to build manually:

.. code-block:: bash

   cd mavlink_sdk
   mkdir build
   cd build
   cmake -DCMAKE_BUILD_TYPE=RELEASE ..
   make

Build Outputs
-------------

The build produces both static and shared libraries in the ``bin/`` directory:

- ``libmavlink_sdk.a`` - Static library
- ``libmavlink_sdk.so`` - Shared library

Build Types
-----------

**DEBUG Build (default)**

.. code-block:: bash

   ./build.sh

- Includes debug symbols (``-g3``, ``-Og``)
- Suitable for development and debugging

**RELEASE Build**

.. code-block:: bash

   ./build.sh RELEASE

- Optimized build (``-O2``)
- Increments version number
- Suitable for production use

**With Additional Debug Options**

.. code-block:: bash

   ./build.sh DEBUG DDEBUG=ON

- Enables detailed debug output
- Useful for troubleshooting

Version Management
-----------------

The SDK uses automatic version management:

- Format: MAJOR.MINOR.BUGFIX.BUILD
- BUILD number auto-increments on RELEASE builds
- Version file stored in ``.version`` in project root
- Current version: 5.6.8.x

To change major or minor versions, edit the version variables in ``CMakeLists.txt``.

Troubleshooting
---------------

**MAVLink library not found**

Ensure the c_library_v2 is located at ``../c_library_v2`` relative to the SDK directory.

**CMake version too old**

Install a newer version of CMake (3.1.0 or higher):

.. code-block:: bash

   sudo apt install cmake

Or download from the CMake website if your distribution's version is too old.

**Compiler not C++17 compatible**

Ensure you have GCC 7+ or Clang 5+ installed:

.. code-block:: bash

   gcc --version
   clang --version

On older systems, you may need to install a newer compiler or use a toolchain.
