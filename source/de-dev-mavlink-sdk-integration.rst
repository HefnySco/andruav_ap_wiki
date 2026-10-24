.. _de-dev-mavlink-sdk-integration:

==================
Integration Guide
==================

This section covers integrating the MAVLink SDK into your C++ project using CMake or manual linking.

CMake Integration
-----------------

The recommended way to integrate the SDK is using CMake.

Add to your ``CMakeLists.txt``:

.. code-block:: cmake

   # Add MAVLink SDK
   add_subdirectory(path/to/mavlink_sdk)

   # Link against the SDK
   target_link_libraries(your_target PRIVATE mavlink_sdk)

   # Include directories
   target_include_directories(your_target PRIVATE 
       path/to/mavlink_sdk/src
       path/to/c_library_v2
   )

Complete Example
~~~~~~~~~~~~~~~~

Here's a complete example ``CMakeLists.txt`` for a project using the SDK:

.. code-block:: cmake

   cmake_minimum_required(VERSION 3.1.0)
   project(MyDroneApp CXX)

   # Set C++17 standard
   set(CMAKE_CXX_STANDARD 17)
   set(CMAKE_CXX_STANDARD_REQUIRED ON)

   # Add MAVLink SDK
   add_subdirectory(../mavlink_sdk)

   # Create your executable
   add_executable(my_drone_app
       src/main.cpp
   )

   # Link against the SDK
   target_link_libraries(my_drone_app PRIVATE mavlink_sdk)

   # Include directories
   target_include_directories(my_drone_app PRIVATE 
       ${CMAKE_CURRENT_SOURCE_DIR}/src
       ../mavlink_sdk/src
       ../c_library_v2
   )

Project Structure
~~~~~~~~~~~~~~~~~

Your project structure should look like this::

    my_project/
    ├── CMakeLists.txt
    ├── src/
    │   └── main.cpp
    ├── mavlink_sdk/              # SDK directory
    │   ├── src/
    │   ├── CMakeLists.txt
    │   └── build.sh
    └── c_library_v2/             # MAVLink C library

Manual Linking
--------------

If you prefer not to use CMake, you can manually compile and link the SDK.

Build the SDK First
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   cd path/to/mavlink_sdk
   ./build.sh

This will produce the library files in the ``bin/`` directory:
- ``libmavlink_sdk.a`` - Static library
- ``libmavlink_sdk.so`` - Shared library

Compile Your Application
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   g++ -std=c++17 your_app.cpp \
       -I/path/to/mavlink_sdk/src \
       -I/path/to/c_library_v2 \
       -L/path/to/mavlink_sdk/bin \
       -lmavlink_sdk \
       -lpthread \
       -o your_app

Using Static Library
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   g++ -std=c++17 your_app.cpp \
       -I/path/to/mavlink_sdk/src \
       -I/path/to/c_library_v2 \
       /path/to/mavlink_sdk/bin/libmavlink_sdk.a \
       -lpthread \
       -o your_app

Using Shared Library
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   g++ -std=c++17 your_app.cpp \
       -I/path/to/mavlink_sdk/src \
       -I/path/to/c_library_v2 \
       -L/path/to/mavlink_sdk/bin \
       -lmavlink_sdk \
       -lpthread \
       -o your_app

You may need to set the ``LD_LIBRARY_PATH`` to run your application:

.. code-block:: bash

   export LD_LIBRARY_PATH=/path/to/mavlink_sdk/bin:$LD_LIBRARY_PATH
   ./your_app

Or install the shared library system-wide:

.. code-block:: bash

   sudo cp /path/to/mavlink_sdk/bin/libmavlink_sdk.so /usr/local/lib/
   sudo ldconfig

Dependencies
------------

The SDK has the following dependencies:

- **pthread** - Threading support (automatically linked by CMake)
- **MAVLink C library** - Must be available at ``../c_library_v2`` relative to SDK

When using CMake, pthread is automatically linked. When manually linking, you must add ``-lpthread``.

Include Paths
-------------

Make sure the following include paths are available to your compiler:

- ``path/to/mavlink_sdk/src`` - SDK headers
- ``path/to/c_library_v2`` - MAVLink C library headers

Library Paths
-------------

When manually linking, ensure the library path is available:

- ``path/to/mavlink_sdk/bin`` - Compiled library files

Troubleshooting
---------------

**Undefined reference to pthread functions**

Make sure you're linking against pthread:

.. code-block:: cmake

   target_link_libraries(your_target PRIVATE mavlink_sdk pthread)

Or with manual linking:

.. code-block:: bash

   -lpthread

**MAVLink headers not found**

Ensure the MAVLink C library is at the correct location (``../c_library_v2`` relative to SDK) and the include path is set correctly.

**Library not found**

When using shared libraries, ensure the library path is in ``LD_LIBRARY_PATH`` or install the library system-wide.

**C++17 not supported**

Ensure your compiler supports C++17 (GCC 7+, Clang 5+). Set the C++ standard in your CMakeLists.txt:

.. code-block:: cmake

   set(CMAKE_CXX_STANDARD 17)
   set(CMAKE_CXX_STANDARD_REQUIRED ON)

Or with manual compilation:

.. code-block:: bash

   -std=c++17

Static vs Shared Library
-------------------------

**Static Library (libmavlink_sdk.a)**

- Advantages:
  - Self-contained executable
  - No runtime dependencies
  - Easier deployment
- Disadvantages:
  - Larger executable size
  - Must recompile if SDK changes

**Shared Library (libmavlink_sdk.so)**

- Advantages:
  - Smaller executable size
  - Can update SDK without recompiling application
  - Multiple applications can share the same library
- Disadvantages:
  - Runtime dependency
  - Must ensure library is available at runtime
  - Slightly more complex deployment

Choose based on your deployment requirements. For most cases, the static library is simpler for development and testing.
